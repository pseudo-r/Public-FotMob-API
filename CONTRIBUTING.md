# Contributing to Public-FotMob-API

First off, thank you for considering contributing to this API documentation project! It's people like you that make these reverse-engineering efforts accurate and complete.

## How Can I Contribute?

### 1. Document New Endpoints
If you've discovered a new FotMob endpoint (e.g., hidden mobile endpoints, analytics routing, or historical routes), submit a PR to add it to the relevant `.md` file in `docs/endpoints`. 
- Provide a `curl` example or the `URL`
- Provide a sample JSON response
- List required/optional parameters

### 2. Update Broken/Modified Endpoints
FotMob doesn't release version updates. They just change paths or modify the JSON payload. If you notice a documented feature breaking or missing fields, update the docs.

### 3. Add Django Client Support
If you discover a new endpoint, please update the Django service wrapper inside `espn_service` to support it. Add the method to `FotMobClient`.

## Writing Documentation

Please try to match the short, practical, markdown-friendly style of the existing documentation. 

* Use **VERIFIED**, **PARTIALLY VERIFIED**, or **UNVERIFIED** tags.
* Keep explanations minimal.
* Use real payload examples (trimmed JSON ONLY).

## Pull Requests

1. Fork the repo and create your branch from `main`.
2. Format your markdown properly.
3. Make sure to update the `CHANGELOG.md`.

Thank you!
