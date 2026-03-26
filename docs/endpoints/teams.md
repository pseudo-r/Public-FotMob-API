# Team Endpoints

These endpoints retrieve comprehensive details about football clubs, national teams, and other playing squads.

---

## Team Profile & Hub

Retrieve the full team center profile, including general information, current squad rosters, recent fixtures, tournament standings context, and historical trajectory.

### Endpoint
`https://www.fotmob.com/api/teams`

### Method
`GET`

### Version
`Unversioned`

### Required Params
- `id`: FotMob internal team ID (`8456` for Man City)

### Optional Params
- `tab`: Controls default active section (`overview`, `roster`, `fixtures`, `transfers`), though the payload often includes all anyway.
- `type`: Sometimes structured as `league` vs `team`, but generally `id` handles scope.

### Example Request
```bash
curl "https://www.fotmob.com/api/teams?id=8456"
```

### Example Response
```json
{
  "details": {
    "id": 8456,
    "type": "team",
    "name": "Man City",
    "shortName": "Man City",
    "country": "ENG",
    "faqJSONLD": {}
  },
  "overview": {
    "nextMatch": {
      "id": 4310532,
      "pageUrl": "/matches/man-city-vs-arsenal/xxxx",
      "home": { "name": "Man City" },
      "away": { "name": "Arsenal" },
      "status": { "utcTime": "2024-03-31T15:30:00.000Z" }
    },
    "form": [
      { "result": "W", "score": "2 - 1", "opponent": "Chelsea" },
      { "result": "D", "score": "1 - 1", "opponent": "Liverpool" }
    ]
  },
  "squad": [
    {
      "title": "Goalkeepers",
      "members": [
        { "id": 137326, "name": "Ederson", "cname": "Ederson", "role": "Keeper" }
      ]
    },
    {
      "title": "Defenders",
      "members": [
        { "id": 204935, "name": "Rúben Dias", "cname": "Rúben Dias", "role": "Defender" }
      ]
    }
  ],
  "fixtures": {
    "allFixtures": {
      "fixtures": [
        { "id": 4310531, "home": "Man City", "away": "Chelsea" }
      ]
    }
  }
}
```

### Verification Status
**VERIFIED**

### Notes
- **Extremely Heavy Payload:** This endpoint hydrates the entire team page in one go. It includes the entire `squad` matrix, months of `fixtures`, current `form` run, and tournament statistics depending on context.
- Uses `www.fotmob.com/api/teams`, surprisingly pluralized `teams` despite taking a singular `id` query parameter.
- Image assets for team crests should be fetched from `images.fotmob.com/image_resources/logo/teamlogo/{teamId}.png`.
