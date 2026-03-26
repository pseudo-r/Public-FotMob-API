# System, Mobile, and Versioning Endpoints

Because FotMob's API isn't formally documented by the developers, it is critical to understand the boundaries of what is public and what triggers security blocks. This document outlines the behavior of versioned routes and backend mobile domains.

---

## The Versioning Myth (v1 / v2 / v3)

Unlike traditional sports APIs that transition schemas gracefully via URLs `(/api/v1/..., /api/v2/...)`, FotMob utilizes an entirely **unversioned** strategy on their primary domain.

### Endpoint Tests
*   `https://www.fotmob.com/api/v1/matches` -> **HTTP 404 Not Found**
*   `https://www.fotmob.com/api/v2/matches` -> **HTTP 404 Not Found**
*   `https://www.fotmob.com/api/v3/matches` -> **HTTP 404 Not Found**

### Conclusion
Do not attempt to append versions to the paths. FotMob iterates their JSON payload schema dynamically in-place under `/api/...`. If properties change, clients must fail gracefully rather than locking to an older version string.

---

## Mobile Telemetry (`pub.fotmob.com`)

The mobile Android and iOS apps frequently hit `pub.fotmob.com` for rapid CloudFront delivery of push notifications, match configurations, and user settings. 

### Endpoint Tests
*   `https://pub.fotmob.com/prod/pub/match/{id}` -> **HTTP 401 Unauthorized**

### Conclusion
While these endpoints technically exist, they are enforced through strict tokenization or signed app payloads. Stateless reverse-engineering scripts (like `curl` or `requests`) without complete session mirroring will fail with `401 Unauthorized`. It is highly recommended to rely strictly on the `www.fotmob.com` paths instead.

---

## Historical Feeds (`data.fotmob.com`)

Often spotted in internal redirects or older application versions.

### Endpoint Tests
*   `https://data.fotmob.com/api` -> **HTTP 403 Forbidden**

### Conclusion
This subdomain is actively firewalled against unauthenticated generic traffic and refuses connection.

---

## Valid Asset Pipeline (`images.fotmob.com`)

The only secondary subdomain safely accessible without spoofing mobile app credentials is the static CDN for imagery.

*   `https://images.fotmob.com/image_resources/logo/teamlogo/{teamId}.png`
*   `https://images.fotmob.com/image_resources/playerimages/{playerId}.png`
*   `https://images.fotmob.com/image_resources/logo/leaguelogo/{leagueId}.png`

### Verification Status
**VERIFIED CURRENT**
