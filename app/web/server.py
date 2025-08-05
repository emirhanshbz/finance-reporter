from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory="app/web/templates")

REPORTS_DIR = "reports"

@app.get("/")
def home():
    return {"message": "Rapor görüntüleyiciye hoş geldiniz. /reports sayfasına gidin"}


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