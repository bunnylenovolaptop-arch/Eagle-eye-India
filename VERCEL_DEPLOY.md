# Eagle Eye India — Vercel deployment

This version is prepared for Vercel's FastAPI runtime.

## Important

- No Angel One credentials are required for public-data mode.
- Vercel's deployment filesystem is read-only except for `/tmp`.
- Paper-trading SQLite state is therefore stored in `/tmp/eagle_eye_paper.sqlite3` when the `VERCEL` environment variable is present.
- Do not add Angel One API keys to a public GitHub repository.

## Deploy

1. Upload the contents of this folder to the GitHub repository root.
2. In Vercel, import that GitHub repository.
3. Use `./` as Root Directory.
4. Let Vercel detect FastAPI automatically.
5. Leave Build Command and Output Directory at their defaults.
6. Deploy.

The root `main.py` exposes the FastAPI application as `app` and serves the `frontend/` directory.
