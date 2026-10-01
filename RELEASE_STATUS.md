# Eagle Eye India — Release Status

## Current state

- Default market source: public no-key market-data adapter for search, quotes and charts.
- Default data label: `PUBLIC_DELAYED`; no Angel One credentials are required.
- Angel One SmartAPI support: optional, server-side only.
- Broker execution: disabled.
- Mobile permissions: INTERNET only.
- Secrets: never packaged in the APK.

## Verification

- Python test suite: 54/54 passing.
- Python compileall: PASS.
- Frontend JavaScript syntax: PASS.
- Public-mode API smoke test: PASS (search, quote, candles and root page with mocked provider responses).
- Android source/configuration: packaged and CI-buildable.

## Data limitation

Public no-key market data can be delayed, rate-limited or unavailable. The app therefore labels the source and keeps execution-grade decision gates fail-closed when live data is required.

## APK status

A byte-for-byte compiled APK is not included in this source release because the current build environment does not contain the Android SDK/build-tools or Gradle distribution and has no external package-download access. The repository includes the Android GitHub Actions workflow for building the APK on a hosted runner.
