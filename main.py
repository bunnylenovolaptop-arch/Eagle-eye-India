from pathlib import Path
from fastapi.staticfiles import StaticFiles
from backend.main import app

root = Path(__file__).parent / "frontend"
app.mount("/", StaticFiles(directory=str(root), html=True), name="frontend")
