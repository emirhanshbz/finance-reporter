# Base image
FROM python:3.10-slim

# Working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Environment variables
ENV PYTHONUNBUFFERED=1

# Run script (örnek olarak scheduler çalıştırılıyor)
CMD ["python", "app/main.py"]