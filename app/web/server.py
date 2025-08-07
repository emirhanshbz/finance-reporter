from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from app.web.api import router as api_router
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/web/templates")

app.include_router(api_router)

REPORTS_DIR = "reports"

@app.get("/")
def home():
    return {"message": "Finance-Reporter <=> /reports <=> /ask"}


@app.get("/reports")
def list_reports(request: Request):
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    files = sorted(os.listdir(REPORTS_DIR), reverse=True)
    return templates.TemplateResponse("index.html", {"request": request, "files": files})


@app.get("/reports/{filename}")
def get_report(filename: str):
    file_path = os.path.join(REPORTS_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="text/html")
    return {"error": "Dosya bulunamadı"}

@app.get("/ask-page")
def ask_page(request: Request):
    return templates.TemplateResponse("ask.html", {"request": request})
