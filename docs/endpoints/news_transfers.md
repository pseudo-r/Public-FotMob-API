# News & Transfers Endpoints

These endpoints retrieve editorial content, transfer market updates, and aggregated football journalism globally.

---

## Global News Feed

A paginated endpoint returning editorial pieces, match summaries, and generated articles.

### Endpoint
`https://www.fotmob.com/api/worldnews`

### Method
`GET`

### Version
`Unversioned`

### Optional Params
- `page`: Pagination integer (`1`, `2`, `3`)
- `lang`: Article language (`en`, `es`)

### Example Request
```bash
curl "https://www.fotmob.com/api/worldnews?page=1"
```

### Example Response
```json
[
  {
    "imageUrl": "https://images.fotmob.com/image_resources/news/...",
    "title": "De Bruyne masterclass guides City past Chelsea",
    "sourceStr": "FotMob",
    "page": {
      "url": "/news/xyz123"
    }
  }
]
```

### Verification Status
**VERIFIED**

### Notes
- Often returns an array directly rather than a wrapped JSON object.
- Re-routed articles (`sourceStr`) contain external URLs inside `page.url` or FotMob hosted slugs.
- Language negotiation depends somewhat on request headers as well as query string.

---

## Transfer Center

Fetches the latest global transfer market moves.

### Endpoint
`https://www.fotmob.com/api/transfers`

### Method
`GET`

### Version
`Unversioned`

### Optional Params
- `page`: Pagination integer (`1`)

### Example Request
```bash
curl "https://www.fotmob.com/api/transfers"
```

### Example Response
```json
{
  "transfers": [
    {
      "name": "Kylian Mbappé",
      "playerId": 688658,
      "position": "Attacker",
      "transferType": { "text": "fee", "localizationKey": "fee" },
      "fromClub": "PSG",
      "fromClubId": 9847,
      "toClub": "Real Madrid",
      "toClubId": 8633,
      "fee": { "feeText": "€100M", "localizedFeeText": "€100M" },
      "transferDate": "2024-07-01T00:00:00.000Z",
      "marketValue": "€180M"
    }
  ]
}
```

### Verification Status
**VERIFIED**

### Notes
- A very rich data structure defining strict `playerId`, `fromClubId`, and `toClubId` properties allowing straightforward mapping across the internal API.
- Includes perceived `marketValue` and the actual `fee`.
