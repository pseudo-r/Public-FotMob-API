<!-- GitAds-Verify: 44FZ4IWPYGNOY6XFRMCK946T5LOIFT23 -->

# FotMob Public API Documentation

**Disclaimer:** This is documentation for FotMob's undocumented public API. I am not affiliated with FotMob. Use responsibly and follow their terms of service.

[![CI](https://github.com/pseudo-r/Public-FotMob-API/actions/workflows/ci.yml/badge.svg?branch=Public-Api)](https://github.com/pseudo-r/Public-FotMob-API/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/pseudo-r/Public-FotMob-API/branch/Public-Api/graph/badge.svg)](https://codecov.io/gh/pseudo-r/Public-FotMob-API)

---

## ☕ Support This Project

If this documentation has saved you time, consider supporting ongoing development and maintenance:

| Platform | Link |
|----------|------|
| ☕ Buy Me a Coffee | [buymeacoffee.com/pseudo_r](https://buymeacoffee.com/pseudo_r) |
| 💖 GitHub Sponsors | [github.com/sponsors/Kloverdevs](https://github.com/sponsors/Kloverdevs) |
| 💳 PayPal Donate | [PayPal (CAD)](https://www.paypal.com/donate/?business=H5VPFZ2EHVNBU&no_recurring=0&currency_code=CAD) |

Every contribution helps keep this project updated as FotMob changes their API.

---

## 📱 Real-World Apps Built With This API

These apps are live examples of what you can build using this documentation and the included Django service wrapper in the broader sports backend:

### ⚽ [Sportly: Soccer Live](https://play.google.com/store/apps/details?id=com.sportly.soccer)
> Premier League, La Liga, Bundesliga, Serie A, MLS, and more — live scores, tables, fixtures, and news powered by comprehensive soccer data.

[![Get it on Google Play](https://img.shields.io/badge/Google_Play-Sportly_Soccer-3DDC84?logo=google-play&logoColor=white)](https://play.google.com/store/apps/details?id=com.sportly.soccer)

## Table of Contents

- [Overview](#overview)
- [Base Domains & Versions](#base-domains--versions)
- [Quick Start](#quick-start)
- [Search & Discovery Endpoints](docs/endpoints/search.md)
- [Event & Match Endpoints](docs/endpoints/matches.md)
- [Team Endpoints](docs/endpoints/teams.md)
- [Player Endpoints](docs/endpoints/players.md)
- [Competition & Standings Endpoints](docs/endpoints/leagues.md)
- [Football-Specific Features](#football-specific-features)
- [Additional Domains / Endpoint Families](#additional-domains--endpoint-families)
- [Notes & Quirks](#notes--quirks)
- [CHANGELOG](CHANGELOG.md)

---

## Overview

FotMob's primary web API exposes deep statistical data, live scores, lineups, player ratings, and detailed team intelligence without requiring API keys or authentication headers. The endpoints fuel their core website experience (`fotmob.com`) and return rich JSON structures covering the global football landscape.

---

## Base Domains & Versions

There are several structural domains that serve data:

| Domain | Versioning | Purpose | Known Status |
|--------|---------|---------|-------------|
| `www.fotmob.com/api` | **Unversioned** | Primary data endpoints (matches, leagues, teams) | **CURRENT / VERIFIED** |
| `images.fotmob.com` | **Unversioned** | Static image feeds, kit rendering, player faces | **CURRENT / VERIFIED** |
| `pub.fotmob.com` | **Unversioned** | Often used for mobile telemetry or cached feed delivery | **UNVERIFIED / INTERNAL** |

> **Note on Versioning:** FotMob's API is almost entirely **unversioned** within the URL space. They do not use `/v1/`, `/v2/`, or `/v3/` paths. Instead, schema changes are deployed directly to the `/api/` base route.

---

## Quick Start

```bash
# Get Match Details (Lineups, incidents, stats)
curl "https://www.fotmob.com/api/matchDetails?matchId=4310531"

# Get League/Standings Data (e.g., Premier League = 47)
curl "https://www.fotmob.com/api/leagues?id=47"

# Get Team Data (e.g., Man City = 8456)
curl "https://www.fotmob.com/api/teams?id=8456"

# Get Player Profile (e.g., De Bruyne = 174543)
curl "https://www.fotmob.com/api/playerData?id=174543"

# Search for Teams/Players
curl "https://www.fotmob.com/api/searchData?term=messi"
```

---

## Endpoint References

Full granular documentation for each endpoint family:

* **[Search & Discovery Endpoints](docs/endpoints/search.md)** - `searchData`, `search/suggest`
* **[Event & Match Endpoints](docs/endpoints/matches.md)** - `matches`, `matchDetails`
* **[Player Endpoints](docs/endpoints/players.md)** - `playerData`
* **[Team Endpoints](docs/endpoints/teams.md)** - `teams`
* **[Competition & Standings](docs/endpoints/leagues.md)** - `leagues`, `allLeagues`
* **[News & Transfers](docs/endpoints/news_transfers.md)** - `worldnews`, `transfers`, `trendingnews`
* **[TV & Broadcast Listings](docs/endpoints/tv_listings.md)** - `tvlistings`

---

## Football-Specific Features

FotMob's JSON payloads frequently expose unique football metrics missing from standard statistical feeds. When consuming `matchDetails` and `playerData`, look for:

- **Expected Goals (xG) & Expected Assists (xA):** Frequently appended natively to player match logs and team totals.
- **Momentum Graphs:** Supplied as an array of numerical values mapping momentum over 90 minutes.
- **Player Ratings:** Both live auto-ratings and final match ratings are exposed granularly per match.
- **Shot Maps:** Detailed X/Y coordinates for goals, misses, and saves connected to the pitch SVG UI.

---

## Additional Domains / Endpoint Families

While `www.fotmob.com/api/` handles 95% of the data ingestion, other domains and versioned routes exist but present challenges:

### Versioned Routes (`/v1/`, `/v2/`, `/v3/`)
- **Pattern Example:** `https://www.fotmob.com/api/v1/matches`
- **Status:** **DOES NOT EXIST / 404 NOT FOUND**
- **Notes:** Unlike the ESPN or NFL APIs, FotMob does not maintain distinct versioned routes. All attempts to query `/v1/`, `/v2/`, or `/v3/` variants of standard endpoints explicitly return HTTP 404 errors. Schema updates are simply deployed to the base unversioned route.

### `images.fotmob.com`
- **Purpose:** Centralized asset delivery for dynamically sizing player headshots, team crests, and league logos.
- **Pattern Example:** `https://images.fotmob.com/image_resources/playerimages/{playerId}.png`
- **Status:** **CURRENT / VERIFIED**

### `pub.fotmob.com`
- **Purpose:** Connected to their mobile app ecosystem, often passing through AWS CloudFront. 
- **Pattern Example:** `https://pub.fotmob.com/prod/pub/match/{id}`
- **Status:** **UNVERIFIED / BLOCKED (401 UNAUTHORIZED)**
- **Notes:** Attempting to query the mobile domain directly via generic stateless scripts generally yields a 401 Unauthorized response. It requires specific mobile authentication or session cookies that are not necessary on the `www.fotmob.com` domain.

### `data.fotmob.com`
- **Purpose:** Older legacy historical feed or internal big-data cache.
- **Pattern Example:** `https://data.fotmob.com/api`
- **Status:** **UNVERIFIED / BLOCKED (403 FORBIDDEN)**
- **Notes:** General `GET` requests fail outright with HTTP 403 Forbidden.

> For more details on interacting with these alternate subdomains, see [docs/endpoints/system_mobile.md](docs/endpoints/system_mobile.md).

---

## Notes & Quirks

- **No Date Range in Match List:** The `/api/matches?date=YYYYMMDD` endpoint only supports retrieving exactly *one* day of data natively.
- **Hydrated Responses:** Endpoints like `/api/teams` and `/api/leagues` return enormous, deeply nested JSON objects containing complete rosters, multi-season fixture lists, and historical tables all in a single response, instead of paginating them by default. This makes initial fetching simple but payloads very large.
- **Search Splits:** `searchData` returns full object arrays for `squadMember`, `team`, and `tournament`, whereas `search/suggest` focuses on autocomplete indexing.

---

## Contributing

Found a new endpoint or schema change? Please open an issue or PR! See `CONTRIBUTING.md` for guidelines.

## License

MIT License — See LICENSE file

---

*Last Updated: March 2026 · Unversioned Architecture · 2 API Domains Documented*
