import pathlib
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from backend.main import app
root=pathlib.Path(__file__).parent/'frontend'
app.mount('/', StaticFiles(directory=str(root), html=True), name='frontend')
