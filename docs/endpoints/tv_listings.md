# TV Listings Endpoint

The `/api/data/tvlistings` endpoint provides regional broadcast and streaming information for given dates, cross-referencing against match IDs globally.

## TV Listings by Country

### Endpoint
`https://www.fotmob.com/api/data/tvlistings?countryCode={code}`

### Method
`GET`

### Required Params
- `countryCode`: The ISO 3166-1 alpha-2 country code (e.g. `US`, `GB`).

### Optional Params
None strictly required, but usually dynamically tracks the active live window.

### Example Request
```bash
# Get US broadcast networks for currently tracked matches
curl -s "https://www.fotmob.com/api/data/tvlistings?countryCode=US"
```

### [VERIFIED] Example Response
The root of the response is an object where the keys are the `matchId`, mapping to an array of broadcast station platforms valid for that region.

```json
{
  "4826055": [
    {
      "startTime": "/Date(1774710000000)/",
      "endTime": "/Date(-62135596800000)/",
      "qualifiers": ["Live"],
      "station": {
        "callSign": "Paramount+",
        "stationId": "rn_604",
        "name": "Paramount+",
        "type": "Stream"
      },
      "stationId": "rn_604",
      "matchId": 4826055,
      "leagueId": 900639,
      "program": {
        "rootId": "4826055",
        "teams": [
          {
            "name": "Stockport County",
            "isHome": true
          },
          {
            "name": "AFC Wimbledon",
            "isHome": false
          }
        ]
      },
      "affiliates": [
        {
          "langCode": "en",
          "title": "Watch on Paramount+",
          "link": "http://paramountplus.qflm.net/...",
          "callToAction": "Watch Live",
          "imageUrl": "https://images.fotmob.com/image_resources/gfx-logo/paramountsquare2.png"
        }
      ]
    }
  ],
  "4837839": [
    {
      "station": {
        "name": "ESPN Select",
        "type": "Stream"
      },
      "matchId": 4837839,
      "leagueId": 901075
    }
  ]
}
```
