# fotmob_service

Production-ready **Django REST Framework** proxy service for the unofficial [FotMob API](https://www.fotmob.com).

## Quick Start (Docker)

```bash
cp .env.example fotmob_service/.env
docker compose up
```

API: **http://localhost:8000**  
Swagger UI: **http://localhost:8000/api/docs/**  
Health: **http://localhost:8000/healthz**

## Endpoints

| Route | Method | Description |
|-------|--------|-------------|
| `GET /api/v1/fotmob/matches/?date=YYYYMMDD` | GET | Daily match list |
| `GET /api/v1/fotmob/matches/{id}/` | GET | Full match details (lineups, xG, stats) |
| `GET /api/v1/fotmob/matches/{id}/score/` | GET | Lightweight live score |
| `GET /api/v1/fotmob/leagues/` | GET | All leagues directory |
| `GET /api/v1/fotmob/leagues/{id}/` | GET | League standings & fixtures |
| `GET /api/v1/fotmob/teams/{id}/` | GET | Team profile |
| `GET /api/v1/fotmob/players/{id}/` | GET | Player data |
| `GET /api/v1/fotmob/search/?q=messi` | GET | Full entity search |
| `GET /api/v1/fotmob/search/suggest/?q=ron` | GET | Autocomplete suggestions |
| `GET /api/v1/fotmob/news/` | GET | Global news feed |
| `GET /api/v1/fotmob/news/trending/` | GET | Trending news |
| `GET /api/v1/fotmob/transfers/` | GET | Transfer market |
| `GET /api/v1/fotmob/tv/?countryCode=US` | GET | Regional broadcast listings |
| `GET /api/v1/fotmob/data/providers/` | GET | Broadcast provider directory |
| `GET /api/v1/fotmob/data/audio/?date=YYYYMMDD` | GET | Audio-enabled matches |

## Structure

```
fotmob_service/
├── manage.py
├── pyproject.toml
├── Dockerfile
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── test.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/          # Health check, middleware, exception handler
│   └── fotmob/        # Proxy views + URL routing
└── clients/
    └── fotmob_client.py  # httpx client with retries
```
