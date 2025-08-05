# 1. Base image
FROM python:3.10-slim

# 2. Çalışma dizini
WORKDIR /app

# 3. Tüm dosyaları kopyala
COPY . .

# 4. Gereken paketleri yükle
RUN pip install --no-cache-dir -r requirements.txt

# 5. Ortam değişkeni
ENV PYTHONUNBUFFERED=1

# 6. FastAPI sunucusunu başlat
CMD ["uvicorn", "app.web.server:app", "--host", "0.0.0.0", "--port", "8000"]
