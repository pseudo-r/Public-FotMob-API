# Player Endpoints

These endpoints retrieve career statistics, bio data, season tracking, and recent form for individual players.

---

## Player Profile

Retrieve the comprehensive player bio, current club details, international caps, and recent match performance ratings.

### Endpoint
`https://www.fotmob.com/api/playerData`

### Method
`GET`

### Version
`Unversioned`

### Required Params
- `id`: FotMob internal player ID (`174543` for Kevin De Bruyne)

### Example Request
```bash
curl "https://www.fotmob.com/api/playerData?id=174543"
```

### Example Response
```json
{
  "id": 174543,
  "name": "Kevin De Bruyne",
  "primaryTeam": {
    "teamId": 8456,
    "teamName": "Man City",
    "role": "Midfielder"
  },
  "position": "Midfielder",
  "positionRow": {
    "Positions": ["Midfielder"]
  },
  "playerInformation": [
    {
      "value": { "fallback": "BEL" },
      "title": "Country",
      "translationKey": "country"
    },
    {
      "value": { "fallback": "32" },
      "title": "Age",
      "translationKey": "age"
    },
    {
      "value": { "fallback": "181 cm" },
      "title": "Height",
      "translationKey": "height"
    }
  ],
  "recentMatches": [
    {
      "teamId": 8456,
      "teamName": "Man City",
      "opponentTeamId": 8634,
      "opponentTeamName": "Chelsea",
      "isHome": true,
      "matchDate": "2024-03-26T14:00:00.000Z",
      "rating": { "num": "7.8", "bgcolor": "#0e87e0" },
      "minutesPlayed": 90,
      "goals": 0,
      "assists": 1
    }
  ],
  "careerHistory": {
    "careerItems": [
      {
        "teamId": 8456,
        "teamName": "Man City",
        "startDate": "2015-08-30",
        "endDate": null,
        "active": true
      }
    ]
  }
}
```

### Verification Status
**VERIFIED**

### Notes
- Extensively detailed payload containing a snapshot of `recentMatches` along with their statistical ratings (`rating.num`).
- Bio block is somewhat abstracted through a `playerInformation` array that uses `title` and `translationKey` mappings for i18n support.
- Image assets for player headshots can be fetched from `images.fotmob.com/image_resources/playerimages/{id}.png`.
