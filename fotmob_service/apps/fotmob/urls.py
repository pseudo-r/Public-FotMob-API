"""FotMob app URL configuration."""
from django.urls import path

from .views import (
    AllLeaguesView,
    AudioMatchesView,
    DataProvidersView,
    LeagueView,
    MatchDetailView,
    MatchesView,
    MatchScoreView,
    PlayerView,
    SearchSuggestView,
    SearchView,
    TeamView,
    TransfersView,
    TrendingNewsView,
    TvListingsView,
    WorldNewsView,
)

urlpatterns = [
    # Matches
    path("matches/", MatchesView.as_view(), name="fotmob-matches"),
    path("matches/<str:match_id>/", MatchDetailView.as_view(), name="fotmob-match-detail"),
    path("matches/<str:match_id>/score/", MatchScoreView.as_view(), name="fotmob-match-score"),
    # Leagues
    path("leagues/", AllLeaguesView.as_view(), name="fotmob-all-leagues"),
    path("leagues/<str:league_id>/", LeagueView.as_view(), name="fotmob-league"),
    # Teams
    path("teams/<str:team_id>/", TeamView.as_view(), name="fotmob-team"),
    # Players
    path("players/<str:player_id>/", PlayerView.as_view(), name="fotmob-player"),
    # Search
    path("search/", SearchView.as_view(), name="fotmob-search"),
    path("search/suggest/", SearchSuggestView.as_view(), name="fotmob-search-suggest"),
    # News & Transfers
    path("news/", WorldNewsView.as_view(), name="fotmob-news"),
    path("news/trending/", TrendingNewsView.as_view(), name="fotmob-trending-news"),
    path("transfers/", TransfersView.as_view(), name="fotmob-transfers"),
    # Broadcast
    path("tv/", TvListingsView.as_view(), name="fotmob-tv-listings"),
    path("data/providers/", DataProvidersView.as_view(), name="fotmob-data-providers"),
    path("data/audio/", AudioMatchesView.as_view(), name="fotmob-audio-matches"),
]
