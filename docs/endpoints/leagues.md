# Competition / Standings Endpoints

These endpoints are used to hydrate league overview pages, retrieving table standings, team lists, upcoming rounds, and season metrics.

---

## All Leagues List (Global Directory)

Fetches the complete directory of tournaments, leagues, and international competitions tracked by FotMob. 

### Endpoint
`https://www.fotmob.com/api/allLeagues`

### Method
`GET`

### Version
`Unversioned`

### Required Params
None

### Example Request
```bash
curl "https://www.fotmob.com/api/allLeagues"
```

### Example Response
```json
{
  "international": [
    {
      "name": "Champions League",
      "id": 42
    },
    {
      "name": "Europa League",
      "id": 73
    }
  ],
  "countries": [
    {
      "name": "England",
      "ccode": "ENG",
      "leagues": [
        {
          "name": "Premier League",
          "id": 47,
          "pageUrl": "/leagues/47/overview/premier-league"
        },
        {
          "name": "Championship",
          "id": 48
        }
      ]
    }
  ]
}
```

### Verification Status
**VERIFIED**

### Notes
- Categorized into `international` and `countries` arrays.
- This is the master index map for translating country code or league names into the `.id` values needed for the `leagues` endpoint.

---

## League Hub / Standings

Retrieve the comprehensive structural data for a specific league, including full standings, active form, stats leaders (goals, assists), and specific round fixtures.

### Endpoint
`https://www.fotmob.com/api/leagues`

### Method
`GET`

### Version
`Unversioned`

### Required Params
- `id`: The league ID (`47` for Premier League, `42` for Champions League)

### Optional Params
- `season`: Fetch historical season data (e.g. `2022%2F2023`).

### Example Request
```bash
curl "https://www.fotmob.com/api/leagues?id=47"
```

### Example Response
```json
{
  "details": {
    "id": 47,
    "type": "league",
    "name": "Premier League",
    "selectedSeason": "2023/2024"
  },
  "seasons": [
    { "id": "2023/2024", "name": "23/24" },
    { "id": "2022/2023", "name": "22/23" }
  ],
  "table": [
    {
      "data": {
        "ccode": "ENG",
        "leagueId": 47,
        "pageUrl": "/leagues/47/overview/premier-league",
        "table": {
          "all": [
            {
              "idx": 1,
              "name": "Arsenal",
              "id": 9825,
              "played": 28,
              "wins": 20,
              "draws": 4,
              "losses": 4,
              "scoresStr": "70-24",
              "goalConDiff": 46,
              "pts": 64
            },
            {
              "idx": 2,
              "name": "Liverpool",
              "id": 8650,
              "played": 28,
              "wins": 19,
              "draws": 7,
              "losses": 2,
              "scoresStr": "65-26",
              "goalConDiff": 39,
              "pts": 64
            }
          ]
        }
      }
    }
  ],
  "stats": {
    "players": [
      {
        "header": "Goals",
        "topThree": [
          { "id": 69696, "name": "E. Haaland", "value": 18, "teamId": 8456 }
        ]
      }
    ]
  }
}
```

### Verification Status
**VERIFIED**

### Notes
- **Heavy Payload:** Includes `table`, `matches`, `overview`, `stats`, and `transfers` nodes natively. No need for secondary calls for league leaders.
- Returns a `table.all`, `table.home`, and `table.away` struct mapping the respective splits.
- League logos can be fetched directly from: `images.fotmob.com/image_resources/logo/leaguelogo/{id}.png`
