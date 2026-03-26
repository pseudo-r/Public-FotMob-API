# Event / Match Endpoints

FotMob's match endpoints deliver live scores, lineups, expected goals (xG), momentum graphs, and play-by-play commentary.

---

## Matches List (By Date)

Retrieve all scheduled or completed matches for a specific date across all covered leagues.

### Endpoint
`https://www.fotmob.com/api/matches`

### Method
`GET`

### Version
`Unversioned`

### Required Params
- `date`: System date in `YYYYMMDD` format (e.g. `20240326`)

### Example Request
```bash
curl "https://www.fotmob.com/api/matches?date=20240326"
```

### Example Response
```json
{
  "leagues": [
    {
      "primaryId": 47,
      "ccode": "ENG",
      "name": "Premier League",
      "matches": [
        {
          "id": 4310531,
          "leagueId": 47,
          "time": "14:00",
          "home": { "id": 8456, "name": "Man City", "score": 2 },
          "away": { "id": 8634, "name": "Chelsea", "score": 1 },
          "status": {
            "utcTime": "2024-03-26T14:00:00.000Z",
            "started": true,
            "cancelled": false,
            "finished": true,
            "scoreStr": "2 - 1"
          }
        }
      ]
    }
  ],
  "date": "20240326"
}
```

### Verification Status
**VERIFIED**

### Notes
- Grouped by `leagues`, not just a flat list of matches.
- `id` inside a match object is the `matchId` used for subsequent detailed queries.
- Cannot query a date range, only single dates.

---

## Match Details (Comprehensive)

The primary endpoint for everything inside a match page — from lineups and incidents to aggregate statistics and pitch momentum tracking.

### Endpoint
`https://www.fotmob.com/api/matchDetails`

### Method
`GET`

### Version
`Unversioned`

### Required Params
- `matchId`: FotMob internal match ID (`4310531`)

### Example Request
```bash
curl "https://www.fotmob.com/api/matchDetails?matchId=4310531"
```

### Example Response
```json
{
  "general": {
    "matchId": "4310531",
    "matchName": "Man City vs Chelsea",
    "matchTimeUTCDate": "2024-03-26T14:00:00.000Z",
    "homeTeam": { "name": "Man City", "id": 8456 },
    "awayTeam": { "name": "Chelsea", "id": 8634 }
  },
  "header": {
    "status": { "finished": true, "scoreStr": "2 - 1" },
    "events": [
      { "type": "Goal", "timeStr": "52'", "player": { "name": "De Bruyne" }, "isHome": true }
    ]
  },
  "content": {
    "matchFacts": {
      "infoBox": { "DisplayTime": "14:00", "Referee": "Michael Oliver" },
      "momentum": {
        "main": { "data": [ {"minute": 1, "value": 5.4}, {"minute": 2, "value": 15.1} ] }
      }
    },
    "stats": {
      "Periods": {
        "All": {
          "stats": [
            { "title": "Expected goals (xG)", "stats": [1.84, 0.72] },
            { "title": "Ball possession", "stats": [65, 35] }
          ]
        }
      }
    },
    "lineup": {
      "lineups": [
        { "teamId": 8456, "teamName": "Man City", "formation": "4-2-3-1", "players": [...] }
      ]
    }
  }
}
```

### Verification Status
**VERIFIED**

### Notes
- Extensively nested payload containing UI layout nodes (e.g. `header`, `nav`). Drop these and focus on `content`.
- **Football-Specific Feature:** Provides `momentum` tracking over the 90 minutes.
- **Football-Specific Feature:** Exposes `Expected goals (xG)` directly in the stats summary.
- Player ratings and deep position structures are provided inside the `lineup` object per player.
