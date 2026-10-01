# Eagle Eye India — Prompt Coverage Matrix

Status meanings:
- IMPLEMENTED: present in the current Phase 6 codebase and tested.
- HARDENED: implemented with additional fail-safe/security controls in this phase.
- PARTIAL: a conservative subset exists; broader provider/asset coverage remains.
- PENDING: not yet complete and therefore blocked from being called production-complete.

| Prompt section | Status | Notes |
|---|---|---|
| 1 Core philosophy | HARDENED | Evidence-first, no-force, fail-closed decision flow. |
| 2 Stock universe | IMPLEMENTED WITH PROVIDER GATE | Live scan supports all subscribed Angel One equities; current Nifty/cap membership must come from a permitted current universe map. |
| 3 Market data | HARDENED | Angel One WebSocket/REST with freshness and validation guards. |
| 4 News intelligence | IMPLEMENTED | Primary-first and permitted public/aggregated feeds. |
| 5 News depth | IMPLEMENTED | Timing, source, materiality and prior-knowledge checks are represented. |
| 6 Catalyst classification | IMPLEMENTED | Catalyst taxonomy in news engine. |
| 7 Three-source verification | IMPLEMENTED | Independent-source de-duplication and explicit unavailable state. |
| 8 Market regime | IMPLEMENTED WITH PROVIDER GATE | Nifty/Bank Nifty/Midcap/Smallcap/VIX/breadth/sector plus optional server-side global/FII/DII/FX/commodity context; never inferred. |
| 9 Technical analysis | IMPLEMENTED | 1m/3m/5m/15m/30m/1H/1D/1W timeframe support with calendar-week resampling. |
| 10 Indicators | IMPLEMENTED | VWAP, EMA/SMA, RSI, MACD, ADX, ATR, Bollinger, OBV/relative volume where data exists. |
| 11 Volume | IMPLEMENTED | Volume, relative volume, traded value/depth; delivery% requires provider data. |
| 12 Relative strength | IMPLEMENTED WITH PROVIDER GATE | NIFTY, sector and peer relative strength when the sector/peer mappings and live ticks exist. |
| 13 Sector engine | IMPLEMENTED WITH PROVIDER GATE | Built-in liquid-name mapping plus explicit server-side extension; unknown stays unavailable. |
| 14 F&O engine | IMPLEMENTED | Contract discovery, futures/option OI context and PCR where quotes exist. |
| 15 Liquidity engine | IMPLEMENTED | Traded value, spread/depth and rejection gates. |
| 16 Manipulation detection | IMPLEMENTED | Deterministic red flags; advanced social/promo intelligence remains limited. |
| 17 News-price relationship | IMPLEMENTED | Catalyst timing and recent price-response context are retained. |
| 18 Fundamental context | IMPLEMENTED WITH PROVIDER GATE | Schema and server-side provider adapter exist; no values are invented when no permitted current feed is configured. |
| 19 Intraday time engine | HARDENED | Current cash CAS timing and F&O window modeled conservatively. |
| 20 Setup score | IMPLEMENTED | Requested 100-point weighted score. |
| 21 Evidence confidence | IMPLEMENTED | Separate from setup score. |
| 22 Adversarial skeptic | IMPLEMENTED | Independent disproof logic plus optional AI skeptic. |
| 23 Three-pass self-correction | IMPLEMENTED | Data freshness → logic/gate validation → contradiction + skeptic pass; changed conclusions are not defended. |
| 24 Hard no-force rule | IMPLEMENTED | Any failed mandatory gate blocks TRADE-READY. |
| 25 Penny-stock rule | IMPLEMENTED WITH PROVIDER GATE | Dedicated stricter traded-value, relative-volume, evidence and manipulation floors for explicit penny/micro/SME tiers. |
| 26 Trade setup | IMPLEMENTED | Trigger/stop/targets/R:R/invalidation. |
| 27 Output | IMPLEMENTED | Concise setup result and no-qualified state. |
| 28 Source display | IMPLEMENTED | Source metadata and verification state. |
| 29 Timestamps | IMPLEMENTED | Exchange/received/news/analysis timestamps. |
| 30 App design | IMPLEMENTED | Mobile terminal UI. |
| 31 Home screen | IMPLEMENTED | Market snapshot + Eagle Scan. |
| 32 Stock card | IMPLEMENTED | Price, volume, VWAP/technical/evidence/status fields. |
| 33 Stock detail | IMPLEMENTED | Chart, technicals, evidence, news, F&O, AI/skeptic panels. |
| 34 WHY button | IMPLEMENTED | Evidence/reasons + contradiction context. |
| 35 RECHECK | IMPLEMENTED | Refreshes status, chart/evidence/F&O; scan can be rerun. |
| 36 Market-wide scan | IMPLEMENTED WITH PROVIDER GATE | Universe, cap tier, F&O, sector, score and traded-value filters are applied; feed capacity remains broker-bounded. |
| 37 Historical learning | IMPLEMENTED | Immutable paper journal + regime/evidence/verification grouped performance analytics. |
| 38 Backtest/paper mode | IMPLEMENTED | Fail-closed replay with ambiguous-bar skips plus paper lifecycle/metrics. |
| 39 Notifications | IMPLEMENTED | Opt-in browser notifications and in-app websocket events; native push provider remains optional. |
| 40 Performance/cost optimization | IMPLEMENTED | Staged filtering, rate pacing and news caching. |
| 41 Privacy/security | HARDENED | No phone PII permissions, server-side secrets, auth, CSP, no API caching. |
| 42 Architecture | IMPLEMENTED WITH NATIVE WRAPPER | FastAPI/PWA + secure native Android WebView shell; secrets stay server-side. |
| 43 Free-first | IMPLEMENTED | No paid institutional data dependency for the prototype. |
| 44 Error handling | HARDENED | Explicit unavailable/stale/fail-closed states. |
| 45 User experience | IMPLEMENTED | Market → setup → why → risks → recheck flow. |
| 46 No automatic trading | HARDENED | Broker order execution disabled. |
| 47 Quality control | HARDENED | Automated parser, paper, auth, indicator and API tests. |
| 48 Development process | IMPLEMENTED | Sequential phases maintained. |
| 49 First build requirement | IMPLEMENTED | UI/search/chart/news/evidence/skeptic/recheck/no-qualified state exist. |
| 50 Final AI behavior | IMPLEMENTED | Evidence + uncertainty + explicit skeptic direction. |

The build is feature-complete at the application layer, while provider-gated inputs remain explicitly unavailable until a permitted current provider is configured. The code never presents unavailable inputs as live or verified.
