# Changelog

All notable changes to the Public FotMob API documentation are listed here.

---

## [Unreleased] — March 2026

### 🆕 Added

#### Documentation
- **`www.fotmob.com/api` section** — Core data API endpoints for real-time live match polling, standings, and intelligence.
- **`images.fotmob.com` section** — Static image feeds for dynamically scaling player and team crests.
- **`pub.fotmob.com` section** — Internal mobile app AWS CloudFront endpoint boundaries.
- **`data.fotmob.com` section** — Legacy firewalled telemetry mappings.
- **Site API explicit verification section** — Documenting the hard `404` verification failure of `v1`, `v2`, and `v3` paths.
- **Endpoint pattern tables** added for core sports endpoints.
- **Specialized Endpoints sections** for:
  - `matches.md` — Live event ticking, momentum data, expected goals (xG).
  - `teams.md` — Roster management, upcoming fixture graphs.
  - `leagues.md` — Top scorers, multi-season table hydration.
  - `players.md` — Individual rating assignments, physical characteristics.
  - `search.md` — Autocomplete suggest endpoints versus full entity hydration grids.
  - `news_transfers.md` — Global football transfer valuations, linked news aggregation pages.
- **`system_mobile.md`** — Explicit guidance on why mobile routes fail with `401 Unauthorized`.
- **`docs/endpoints/`** — Created structured folder organization mirroring ESPN architecture.
- **`CHANGELOG.md`** (this file)
- **`CONTRIBUTING.md`** — Robust pull-request guidance mirroring ESPN standard templates.
- **`SPONSOR.md`** — Community funding pipeline docs.

#### Code (`espn_service`)
New methods added to `FotMobClient` natively in the Django backend:
- `get_matches_by_date(date)` — Pull daily global fixture directory.
- `get_match_details(match_id)` — Fetch complete game payload including xG and lineups.
- `get_team(team_id)` — Full organizational context wrapper.
- `get_league(league_id, season)` — Standings and analytics.
- `get_player(player_id)` — Player profile.
- `search_full(term)` & `search_suggest` — Exposed discovery layers.
- `get_world_news(page)` & `get_transfers(page)` — Media routing.

### 🔧 Fixed
- **Version URI Enforcement** — Removed all implied versioning (`v2`, `v3`) across API examples as they universally trigger server failures.
- **Endpoint Structure** — Ensured all `curl` examples enforce `https://` strictly.

---

## [1.0.0] — Initial Release

### 🆕 Added
- Initial FotMob API documentation
- README with base URLs, quick start, common endpoints
- `docs/endpoints/` scaffolding for football metrics 
