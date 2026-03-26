# Audio, Data Providers & Match Score Endpoints

These endpoints were discovered via analysis of the FotMob frontend JavaScript bundle chunks (`/_next/static/chunks/`) and are accessible without authentication.

---

## Audio Matches

A feed of commentary audio-ready matches for a given date.

### Endpoint
`https://www.fotmob.com/api/data/audio-matches?date={YYYYMMDD}`

### Method
`GET`

### Required Params
- `date`: Date in `YYYYMMDD` format (e.g. `20240326`)

### Example Request
```bash
# Get audio match listings for a date
curl "https://www.fotmob.com/api/data/audio-matches?date=20240326"
```

### [VERIFIED] Example Response
Returns a JSON array of match objects with provider language availability.
```json
[
  {"id": "4837401", "langs": ["ENG"]},
  {"id": "4837404", "langs": ["ENG"]},
  {"id": "4826055", "langs": ["ENG", "ESP"]}
]
```

### Verification Status
**VERIFIED** — Returns `HTTP 200` with a list of audio-enabled match IDs and their supported language codes.

---

## Data Providers

Returns a directory of all supported data provider integrations (TV/broadcast/streaming platforms) keyed by provider ID.

### Endpoint
`https://www.fotmob.com/api/data/dataproviders`

### Method
`GET`

### Required Params
None

### Example Request
```bash
curl "https://www.fotmob.com/api/data/dataproviders"
```

### [VERIFIED] Example Response
Returns a JSON object keyed by numeric provider IDs.
```json
{
  "14": { "name": "ESPN", "type": "TV" },
  "38": { "name": "BBC Sport", "type": "Stream" },
  "39": { "name": "Sky Sports", "type": "TV" }
}
```

### Verification Status
**VERIFIED** — Returns `HTTP 200` with a mapping of broadcast provider IDs to their full metadata.

### Notes
- The provider IDs returned here are the `stationId` values in the [TV Listings](tv_listings.md) endpoint responses.
- Cross-reference these IDs to decode which network is airing each match.

---

## Match Score (Lightweight)

A lightweight match score endpoint returning a single `match` object — useful for polling live results without fetching full `matchDetails`.

### Endpoint
`https://www.fotmob.com/api/data/match-score?matchId={matchId}`

### Method
`GET`

### Required Params
- `matchId`: The numeric FotMob match ID

### Example Request
```bash
# Get lightweight live score for a match
curl "https://www.fotmob.com/api/data/match-score?matchId=4310531"
```

### [VERIFIED] Example Response
```json
{
  "match": {
    "id": 4310531,
    "status": { "finished": true, "started": true, "cancelled": false },
    "home": { "id": 8456, "name": "Man City", "score": 3 },
    "away": { "id": 8650, "name": "Arsenal", "score": 1 }
  }
}
```

### Verification Status
**VERIFIED** — Returns `HTTP 200` with a lightweight `match` key.

### Notes
- Much lighter than `/api/matchDetails` — ideal for polling live score updates.
- Keys include `status`, `home`, and `away` with team name and score.
