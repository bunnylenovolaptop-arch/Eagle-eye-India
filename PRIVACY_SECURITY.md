# Eagle Eye India — Privacy & Security Contract

This build is designed as a read-only market-analysis application. It does not request or use phone contacts, location, camera, microphone, advertising ID, device identifiers, SMS, call logs, photos, files, or other personal phone data.

## What the mobile client sends

The client sends only application actions and market-analysis inputs necessary to use Eagle Eye, such as stock symbols/tokens, selected timeframe, scan/recheck requests, and the app-session credential needed to unlock the private backend.

The client does not send a device identifier or a phone address book. Browser storage is limited to an in-session backend URL and the browser-managed HttpOnly session cookie; the app access token itself is not written to persistent browser storage.

## What stays server-side

Angel One API credentials, TOTP secret, JWT, refresh token, feed token, and AI-provider credentials are backend configuration. They are never embedded in the PWA/Android bundle and are not returned by API responses.

## Broker safety

Broker order placement is disabled. Paper trades are updated only from validated Angel One live ticks unless the explicit development-only manual revalue flag is enabled.

## Live-data safety

A tick is accepted only after structural validation, timestamp sanity checks, age checks, OHLC validation where available, and sequence-order checks where meaningful. The UI never uses socket-connect state alone to declare the market data live.

## Caching and logs

API responses are marked `no-store`. The service worker never caches `/api/` or `/ws`. The Docker deployment disables FastAPI access logs by default to avoid app-generated request-IP logging. A reverse proxy in front of the server may still maintain its own logs; that policy is outside the application.

## Network security

Remote backend URLs must use HTTPS. Same-origin is the default CORS policy. API authentication uses a short-lived HttpOnly SameSite session cookie. State-changing requests require an allowed Origin. API documentation endpoints are disabled by default.

## Fail-closed behavior

Missing or stale data is surfaced as `DATA UNAVAILABLE`, `STALE`, `TECHNICAL DATA INSUFFICIENT`, `NEWS VERIFICATION UNAVAILABLE`, or `NO QUALIFIED SETUP` rather than being replaced with guessed values.

## Production warning

No software can guarantee zero security defects, zero feed interruptions, or perfectly accurate market predictions. This contract defines defensive behavior and explicit failure modes; production deployment still requires patching the OS/runtime, TLS termination, secret rotation, monitoring, and independent security review.
