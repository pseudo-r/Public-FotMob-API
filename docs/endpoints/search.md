# Search & Discovery Endpoints

FotMob uses separate endpoints for quick autocomplete suggestions versus full search data retrieval.

---

## Global Search (Full Data)

Returns complete object matches across players, teams, leagues, and ongoing matches. Useful for deep querying.

### Endpoint
`https://www.fotmob.com/api/searchData`

### Method
`GET`

### Version
`Unversioned`

### Required Params
- `term`: URL-encoded search string (`messi`, `man+city`)

### Example Request
```bash
curl "https://www.fotmob.com/api/searchData?term=messi"
```

### Example Response
```json
{
  "squadMember": [
    {
      "id": 83713,
      "name": "Lionel Messi",
      "localizedName": "Lionel Messi",
      "isCurrentSponsor": false
    }
  ],
  "team": [
    {
      "id": 9855,
      "name": "Messina",
      "localizedName": "Messina",
      "isCurrentSponsor": false
    }
  ],
  "tournament": []
}
```

### Verification Status
**VERIFIED**

### Notes
- Results are heavily bucketed into arrays (`squadMember`, `team`, `tournament`).
- Does not contain metadata about the entities (no images, no current teams), just lookup IDs and names to hydrate into a `/api/playerData` call.

---

## Autocomplete Suggest

Typically fuels mobile app drop-downs or web nav-bar quick searches. Provides slightly differently shaped data, optimized for speed.

### Endpoint
`https://www.fotmob.com/api/search/suggest`

### Method
`GET`

### Version
`Unversioned`

### Required Params
- `term`: URL-encoded search string (`ronaldo`, `barcelona`)

### Example Request
```bash
curl "https://www.fotmob.com/api/search/suggest?term=ronaldo"
```

### Example Response
```json
{
  "players": [
    { "id": 20496, "name": "Cristiano Ronaldo", "info": "Al Nassr FC" },
    { "id": 203841, "name": "Ronaldo", "info": "Rostov" }
  ],
  "teams": [],
  "leagues": []
}
```

### Verification Status
**VERIFIED**

### Notes
- Much leaner response than `searchData`.
- Includes a helpful `info` key (usually the player's team) out of the box so you don't need a secondary lookup to distinguish identically named players in front-end displays.
