# Eagle Eye India — Hardened full-stack build Hardening Report

## Scope

This phase hardens the two areas that can directly invalidate money-related analysis: the live market-data path and the paper-trading state machine. Privacy/security controls are part of the same trust boundary.

## Live-data controls

- Angel One SmartAPI WebSocket 2.0 remains server-side; credentials never enter the mobile bundle.
- Provider authentication is paced to 1 request/second and serialized so reconnect storms cannot create concurrent login/refresh races.
- WebSocket sessions are allocated with no more than 1,000 desired tokens per session and no more than three configured sessions.
- Dynamic subscriptions are idempotent and never add a 1,001st token to an existing session.
- Dynamic subscriptions are attached to a mutable desired-token set so a reconnect re-subscribes the full current allocation instead of silently losing symbols.
- Live packet decoding uses Angel One's documented 64-bit LTP and SnapQuote/depth field offsets.
- Best-five records reject unknown side flags, negative quantities/orders, and invalid prices.
- Tick validation checks exchange type, positive finite price, timestamp sanity, maximum tick age, sequence ordering where meaningful, and OHLC consistency.
- The UI does not mark a socket connection as LIVE; it waits for fresh validated ticks.
- API status reports LIVE only when critical NIFTY and BANK NIFTY ticks are fresh. Otherwise it reports STALE/UNAVAILABLE and exposes DEGRADED critical status separately.
- Provider heartbeat status is tracked independently and is not fabricated at WebSocket connect time.
- REST quote/candle calls are separately paced below the documented provider limits.
- API responses use `Cache-Control: no-store`; the service worker never caches `/api/` or `/ws` traffic.

## Paper-trading controls

- Default paper valuation source is `ANGEL_ONE_LIVE` validated ticks only.
- Manual paper revaluation is disabled by default.
- Market-event timestamps are rejected when too far in the future or older than 60 seconds.
- Out-of-order market timestamps cannot rewrite an existing paper state.
- LONG/SHORT trigger-stop-target geometry is validated before insertion.
- Duplicate identical paper setups are suppressed for one minute.
- A tick that gaps through the final target on the entry trigger is recorded as `SKIPPED / ENTRY_GAP_THROUGH_TARGET`, not as a phantom win.
- Paper outcomes are not sent to the broker, and broker order execution remains disabled.
- Paper database uses SQLite WAL, full synchronous durability, foreign keys, busy timeout and restrictive file permissions.
- Paper metrics count only closed trades with an observed R multiple; skipped/unresolved states are not counted as wins.

## Privacy and security

- The PWA contains no phone-data APIs for geolocation, contacts, camera, microphone, motion/orientation, USB, Bluetooth, analytics, telemetry, advertising ID or device identifiers.
- No third-party tracking SDK is bundled.
- The client keeps only the backend URL in session storage; the app access token is not written to browser storage and is exchanged for an HttpOnly SameSite session cookie.
- Remote backend URLs must use HTTPS; plain HTTP is allowed only for localhost development.
- State-changing API calls require a valid Origin check.
- API documentation is disabled by default.
- The backend does not forward raw broker control/auth frames to the phone.
- Docker runs read-only, uses a private data volume and disables Uvicorn access logging by default.

## Tests

Automated test suite: **54/54 passing**.

Additional checks:
- Python compilation: PASS
- Frontend JavaScript syntax check: PASS when Node is available
- ASGI security smoke test: PASS
- Static privacy/API scan: PASS
- No provider credential values present in frontend or environment template: PASS

## Residual risk

No application can guarantee zero bugs, zero outages, zero third-party feed errors or perfectly accurate market predictions. Secure deployment still requires TLS termination, OS/runtime patching, strong server access controls, secret rotation, backups, monitoring and an independent security review before real-money use.

The feature-coverage matrix in `PROMPT_COVERAGE.md` explicitly identifies the prompt features that are still PARTIAL/PENDING. Those gaps are not represented as complete functionality.
