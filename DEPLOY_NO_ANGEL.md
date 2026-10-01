# Deploy Eagle Eye India without Angel One

This release defaults to `EAGLE_PUBLIC_DATA_ONLY=true` and `EAGLE_REQUIRE_AUTH=false`.

### Vercel

Vercel currently supports FastAPI with zero-configuration on its Python runtime, and FastAPI-mounted static files can be promoted to the Vercel CDN.

1. Create a Vercel project from this folder/repository.
2. Deploy with the default settings.
3. Open the deployment URL.
4. For the Android shell, enter that HTTPS URL once in the APK.

No Angel One variables are required for the public mode.

### Optional AI

`OPENAI_API_KEY` is optional and server-side. The market-data path does not need an API key.

### Data behavior

Stock search, quotes and candles use the public market-data adapter. The UI labels this data `DELAYED`. When data is unavailable, the app shows an unavailable state instead of inventing values. Do not treat this source as broker-grade live execution data.
