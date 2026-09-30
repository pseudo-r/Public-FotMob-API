"""FotMob API client — wraps the unofficial www.fotmob.com/api endpoints."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any

import httpx
from tenacity import retry, retry_if_exception_type, stop_after_attempt, wait_exponential

logger = logging.getLogger(__name__)

BASE_URL = "https://www.fotmob.com/api"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
    "Accept": "application/json, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.fotmob.com/",
}


class FotMobClientError(Exception):
    """Raised when FotMob returns an unexpected status."""


class FotMobTransientError(FotMobClientError):
    """Retryable network or upstream server failure."""


class FotMobNotFoundError(FotMobClientError):
    """Raised when FotMob returns 404."""


@dataclass
class FotMobResponse:
    data: Any
    status_code: int


class FotMobClient:
    """Thread-safe, retry-enabled HTTP client for the FotMob API."""

    def __init__(self, base_url: str = BASE_URL, timeout: float = 30.0) -> None:
        self._base_url = base_url.rstrip("/")
        self._client = httpx.Client(headers=HEADERS, timeout=timeout, follow_redirects=True)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> FotMobClient:
        return self

    def __exit__(self, *_) -> None:
        self.close()

    @retry(
        retry=retry_if_exception_type(FotMobTransientError),
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=10),
        reraise=True,
    )
    def _get(self, path: str, params: dict | None = None) -> FotMobResponse:
        url = f"{self._base_url}/{path.lstrip('/')}"
        logger.debug("fotmob_request url=%s params=%s", url, params)
        try:
            resp = self._client.get(url, params=params)
        except httpx.RequestError as exc:
            raise FotMobTransientError(f"Request failed: {exc}") from exc

        if resp.status_code == 404:
            raise FotMobNotFoundError(f"Not found: {url}")
        if resp.status_code >= 500:
            raise FotMobTransientError(f"HTTP {resp.status_code}: {url}")
        if resp.status_code >= 400:
            raise FotMobClientError(f"HTTP {resp.status_code}: {url}")

        try:
            data = resp.json()
        except Exception as exc:
            raise FotMobClientError(f"Failed to parse JSON from {url}") from exc

        return FotMobResponse(data=data, status_code=resp.status_code)

    # ------------------------------------------------------------------ #
    # Matches
    # ------------------------------------------------------------------ #
    def get_matches_by_date(self, date: str) -> FotMobResponse:
        """Get all matches for a date (YYYYMMDD)."""
        return self._get("data/matches", params={"date": date})

    def get_match_details(self, match_id: str | int) -> FotMobResponse:
        """Full match payload — lineups, stats, incidents, xG."""
        return self._get("data/matchDetails", params={"matchId": match_id})

    def get_match_score(self, match_id: str | int) -> FotMobResponse:
        """Lightweight live score — faster than matchDetails."""
        return self._get("data/match-score", params={"matchId": match_id})

    # ------------------------------------------------------------------ #
    # Leagues
    # ------------------------------------------------------------------ #
    def get_all_leagues(self) -> FotMobResponse:
        """Directory of all available leagues."""
        return self._get("data/allLeagues")

    def get_league(self, league_id: str | int, season: str | None = None) -> FotMobResponse:
        """League standings, fixtures, and leaders."""
        params: dict = {"id": league_id}
        if season:
            params["season"] = season
        return self._get("data/leagues", params=params)

    # ------------------------------------------------------------------ #
    # Teams
    # ------------------------------------------------------------------ #
    def get_team(self, team_id: str | int) -> FotMobResponse:
        """Full team profile — roster, fixtures, form."""
        return self._get("data/teams", params={"id": team_id})

    # ------------------------------------------------------------------ #
    # Players
    # ------------------------------------------------------------------ #
    def get_player(self, player_id: str | int) -> FotMobResponse:
        """Player bio, ratings, and recent match stats."""
        return self._get("data/playerData", params={"id": player_id})

    # ------------------------------------------------------------------ #
    # Search
    # ------------------------------------------------------------------ #
    def search_full(self, term: str) -> FotMobResponse:
        """Full entity search — teams, players, leagues."""
        return self._get("searchData", params={"term": term})

    def search_suggest(self, term: str) -> FotMobResponse:
        """Autocomplete suggestions."""
        return self._get("search/suggest", params={"term": term})

    # ------------------------------------------------------------------ #
    # News & Transfers
    # ------------------------------------------------------------------ #
    def get_world_news(self, page: str | int = 1) -> FotMobResponse:
        """Paginated global football news feed."""
        return self._get("worldnews", params={"page": page})

    def get_trending_news(self) -> FotMobResponse:
        """Top trending news carousel."""
        return self._get("trendingnews")

    def get_transfers(self, page: str | int = 1) -> FotMobResponse:
        """Transfer market moves."""
        return self._get("transfers", params={"page": page})

    # ------------------------------------------------------------------ #
    # Broadcast / Data
    # ------------------------------------------------------------------ #
    def get_tv_listings(self, country_code: str = "US") -> FotMobResponse:
        """Regional broadcast listings keyed by matchId."""
        return self._get("data/tvlistings", params={"countryCode": country_code})

    def get_data_providers(self) -> FotMobResponse:
        """Directory of all broadcast provider IDs."""
        return self._get("data/dataproviders")

    def get_audio_matches(self, date: str) -> FotMobResponse:
        """Audio-commentary-eligible matches for a date."""
        return self._get("data/audio-matches", params={"date": date})


    def get_league_match_context(self, match_id: int, league_id: int) -> FotMobResponse:
        """League context used by the current match-detail page."""
        return self._get("data/leagueDataForMatch", params={"matchId": match_id, "leagueId": league_id})

    def get_entity_news(self, entity_id: int, entity_type: str, language: str = "en", start_index: int = 0) -> FotMobResponse:
        """Current team/league news feed; start_index controls pagination."""
        if entity_type not in {"team", "league"} or start_index < 0:
            raise ValueError("Use team or league and a non-negative start_index")
        return self._get("data/tlnews", params={"id": entity_id, "type": entity_type, "language": language, "startIndex": start_index})
