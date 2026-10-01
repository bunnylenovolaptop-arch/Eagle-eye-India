# Eagle Eye India

Read-only Indian market intelligence terminal with a **no-broker-credentials public-data mode**.

## Public no-key mode

The default build uses a public market-data adapter for stock search, quotes and historical candles. It requires **no Angel One API key, login, PIN, OTP, JWT or feed token**. Public data is explicitly labeled delayed and is **not** treated as broker-grade live data. Trade-ready decisions remain fail-closed when a required live feed is unavailable.

## Optional broker mode

Angel One SmartAPI support remains in the backend as an optional provider for deployments that intentionally configure broker credentials server-side. The mobile client never stores broker secrets and broker order execution remains disabled.

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open `http://localhost:8000`.

## Vercel

This project is structured as a FastAPI application and can be deployed to Vercel's Python runtime. Vercel documents zero-configuration FastAPI deployment and current support for serving FastAPI-mounted static frontend assets.

## Safety

No automatic broker orders are enabled. Public delayed data must not be represented as live execution data, and unavailable data is surfaced rather than guessed.
