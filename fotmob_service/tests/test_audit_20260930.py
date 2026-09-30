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
    ("leagues/47/table/?season=2025%2F2026", "leagues?id=47&season=2025%2F2026", {"table": []}),
    ("teams/8456/fixtures/", "teams?id=8456", {"fixtures": {"allFixtures": {"fixtures": []}}}),
])
def test_derived_routes(httpx_mock, path, url, data):
    httpx_mock.add_response(url="https://www.fotmob.com/api/" + url, json=data)
    response = APIClient().get("/api/v1/fotmob/" + path)
    assert response.status_code == 200
    assert response.json() == data

def test_missing_table_is_not_empty_success(httpx_mock):
    httpx_mock.add_response(json={})
    assert APIClient().get("/api/v1/fotmob/leagues/47/table/").status_code == 502
