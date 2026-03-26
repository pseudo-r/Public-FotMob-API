"""FotMob proxy views."""
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from clients.fotmob_client import FotMobClient, FotMobClientError, FotMobNotFoundError


class BaseFotMobView(APIView):
    """Base proxy view — initialises FotMobClient per request."""

    def dispatch(self, request: Request, *args, **kwargs):
        self.client = FotMobClient()
        try:
            return super().dispatch(request, *args, **kwargs)
        finally:
            self.client.close()

    def _err(self, exc: Exception) -> Response:
        if isinstance(exc, FotMobNotFoundError):
            return Response({"detail": str(exc)}, status=status.HTTP_404_NOT_FOUND)
        if isinstance(exc, FotMobClientError):
            return Response({"detail": str(exc)}, status=status.HTTP_502_BAD_GATEWAY)
        return Response({"detail": "Unexpected error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class MatchesView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        date = request.query_params.get("date")
        if not date:
            return Response({"detail": "date is required (YYYYMMDD)"}, status=400)
        try:
            return Response(self.client.get_matches_by_date(date).data)
        except Exception as e:
            return self._err(e)


class MatchDetailView(BaseFotMobView):
    def get(self, request: Request, match_id: str) -> Response:
        try:
            return Response(self.client.get_match_details(match_id).data)
        except Exception as e:
            return self._err(e)


class MatchScoreView(BaseFotMobView):
    def get(self, request: Request, match_id: str) -> Response:
        try:
            return Response(self.client.get_match_score(match_id).data)
        except Exception as e:
            return self._err(e)


class AllLeaguesView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        try:
            return Response(self.client.get_all_leagues().data)
        except Exception as e:
            return self._err(e)


class LeagueView(BaseFotMobView):
    def get(self, request: Request, league_id: str) -> Response:
        try:
            return Response(self.client.get_league(league_id).data)
        except Exception as e:
            return self._err(e)


class TeamView(BaseFotMobView):
    def get(self, request: Request, team_id: str) -> Response:
        try:
            return Response(self.client.get_team(team_id).data)
        except Exception as e:
            return self._err(e)


class PlayerView(BaseFotMobView):
    def get(self, request: Request, player_id: str) -> Response:
        try:
            return Response(self.client.get_player(player_id).data)
        except Exception as e:
            return self._err(e)


class SearchView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        term = request.query_params.get("q") or request.query_params.get("term")
        if not term:
            return Response({"detail": "q is required"}, status=400)
        try:
            return Response(self.client.search_full(term).data)
        except Exception as e:
            return self._err(e)


class SearchSuggestView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        term = request.query_params.get("q") or request.query_params.get("term")
        if not term:
            return Response({"detail": "q is required"}, status=400)
        try:
            return Response(self.client.search_suggest(term).data)
        except Exception as e:
            return self._err(e)


class WorldNewsView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        page = request.query_params.get("page", "1")
        try:
            return Response(self.client.get_world_news(page=page).data)
        except Exception as e:
            return self._err(e)


class TrendingNewsView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        try:
            return Response(self.client.get_trending_news().data)
        except Exception as e:
            return self._err(e)


class TransfersView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        page = request.query_params.get("page", "1")
        try:
            return Response(self.client.get_transfers(page=page).data)
        except Exception as e:
            return self._err(e)


class TvListingsView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        country = request.query_params.get("countryCode", "US")
        try:
            return Response(self.client.get_tv_listings(country_code=country).data)
        except Exception as e:
            return self._err(e)


class DataProvidersView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        try:
            return Response(self.client.get_data_providers().data)
        except Exception as e:
            return self._err(e)


class AudioMatchesView(BaseFotMobView):
    def get(self, request: Request) -> Response:
        date = request.query_params.get("date")
        if not date:
            return Response({"detail": "date is required (YYYYMMDD)"}, status=400)
        try:
            return Response(self.client.get_audio_matches(date).data)
        except Exception as e:
            return self._err(e)
