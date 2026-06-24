# OCR web app (Gradio + Tesseract). Fully open-source, no AI service.
FROM python:3.11-slim

# Tesseract OCR engine (the system binary pytesseract calls)
RUN apt-get update && apt-get install -y --no-install-recommends \
    tesseract-ocr \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENV PORT=7860
EXPOSE 7860
CMD ["python", "app.py"]
