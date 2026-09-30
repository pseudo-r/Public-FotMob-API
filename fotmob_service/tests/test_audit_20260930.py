import pytest
from rest_framework.test import APIClient

from clients.fotmob_client import FotMobClient, FotMobClientError


@pytest.mark.parametrize("status", [400, 403, 404, 429])
def test_terminal_errors_once(httpx_mock, status):
    httpx_mock.add_response(status_code=status)
    with FotMobClient() as client, pytest.raises(FotMobClientError):
        client.get_all_leagues()
    assert len(httpx_mock.get_requests()) == 1

@pytest.mark.parametrize("path,url,data", [
    ("leagues/47/table/?season=2025%2F2026", "data/leagues?id=47&season=2025%2F2026", {"table": []}),
    ("teams/8456/fixtures/", "data/teams?id=8456", {"fixtures": {"allFixtures": {"fixtures": []}}}),
])
def test_derived_routes(httpx_mock, path, url, data):
    httpx_mock.add_response(url="https://www.fotmob.com/api/" + url, json=data)
    response = APIClient().get("/api/v1/fotmob/" + path)
    assert response.status_code == 200
    assert response.json() == data

def test_missing_table_is_not_empty_success(httpx_mock):
    httpx_mock.add_response(json={})
    assert APIClient().get("/api/v1/fotmob/leagues/47/table/").status_code == 502


@pytest.mark.parametrize("method,args,path", [
    ("get_matches_by_date", ("20260930",), "data/matches?date=20260930"),
    ("get_match_details", (4310531,), "data/matchDetails?matchId=4310531"),
    ("get_all_leagues", (), "data/allLeagues"),
    ("get_player", (174543,), "data/playerData?id=174543"),
    ("get_league_match_context", (4310531, 47), "data/leagueDataForMatch?matchId=4310531&leagueId=47"),
    ("get_entity_news", (8456, "team"), "data/tlnews?id=8456&type=team&language=en&startIndex=0"),
])
def test_current_routes(httpx_mock, method, args, path):
    httpx_mock.add_response(url="https://www.fotmob.com/api/"+path, json={"ok": True})
    with FotMobClient() as client:
        assert getattr(client, method)(*args).data == {"ok": True}
