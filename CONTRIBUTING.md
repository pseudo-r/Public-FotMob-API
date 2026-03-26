# Contributing to Public-FotMob-API

Thank you for your interest in contributing! This project documents the unofficial FotMob API and provides a Django-based service integration for consuming it.

## Ways to Contribute

### 📖 Documentation
- Add or correct endpoint URLs
- Discover new mobile-specific or internal routing metrics
- Improve or add `curl` examples
- Add response schema examples to `docs/endpoints/`
- Fix errors, typos, or outdated information

### 🐛 Report a Bug
Open an issue using the **🐛 Bug Report** template. Please include:
- The endpoint URL you used
- What you expected
- What you actually received (status code, response snippet)

### 🆕 Report a Missing Endpoint
Open an issue using the **🔍 Missing Endpoint** template. If you've found a FotMob API endpoint not documented here (e.g. historical data, betting integrations), we want to know!

### 💻 Code (Football Integration)
Fix bugs or add features to the Django service wrapper. Please include tests for any code changes. (Note: The active Django fotmob implementation resides within the unified `espn_service` backend).

---

## Development Setup

### 🐳 Docker (recommended — one command)

```bash
git clone https://github.com/pseudo-r/Public-FotMob-API.git
cd Public-FotMob-API

# Copy env file
cp .env.example .env

# Note: The FotMob Django app is structurally initialized in the broader sports backend docker context.
docker compose up
```

API at **http://localhost:8000** · Swagger UI at **http://localhost:8000/api/schema/swagger-ui/**

---

### 🐍 Local (without Docker)

Prerequisites: Python 3.12+, PostgreSQL 14+, Redis 6+.

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -e ".[dev]"

# Copy and edit env
cp .env.example .env

python manage.py migrate
python manage.py runserver
```

---

## Pull Request Guidelines

1. **Branch off `main`** — this is the default documentation branch
2. **One concern per PR** — keep changes focused
3. **Write clear commit messages** — reference the endpoint or file you changed
4. **Add tests** for any backend code changes
5. **Update docs** if you change endpoints or add new features

### Commit message format

```
type: short description

- Bullet detail if needed
```

Types: `docs`, `feat`, `fix`, `test`, `chore`

---

## Documentation Style Guide

### Endpoint Blocks

Use the existing markdown format in the endpoints:

```markdown
### Endpoint
`https://www.fotmob.com/api/leagues`

### Method
`GET`

### Required Params
- `id`
```

### Curl examples

- Use `https://` always (never `http://`)
- Add a `# comment` above each example describing what it does
- Use real, working IDs in examples (e.g., `47` for Premier League)

### File locations

| What | Where |
|------|-------|
| Specific endpoint collections | `docs/endpoints/*.md` |
| System / Mobile routing | `docs/endpoints/system_mobile.md` |
| Site-wide docs | `README.md` |
| Change history | `CHANGELOG.md` |

---

## Code of Conduct

Be kind and respectful. This is a community resource — everyone is welcome.

---

## License

By contributing, you agree that your contributions will be licensed under the same [MIT License](LICENSE) as this project.
