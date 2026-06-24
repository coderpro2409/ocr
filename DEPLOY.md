# Deploying the OCR app

Fully open-source, no AI service: a **Gradio** web app using **Tesseract**
(`pytesseract`). This is the web version of the notebook pipeline
(Pillow -> pytesseract). It needs no LLM and no GPU.

> Note: Vercel cannot host this. Tesseract is a system binary that must be
> installed, which serverless functions don't support. The original `ot4.py`
> (tkinter + Surya + local llama-server) is a desktop/GPU script, left in the
> repo for reference only; it is not the deployed app.

## Deploy with Docker (any VM / host with Docker)
```bash
docker build -t ocr-app .
docker run -d -p 7860:7860 ocr-app
```
Open `http://<host-ip>:7860` (open port 7860 in the firewall).

This can share the same VM as the BFSI app. No API key, no Ollama needed.

## Run locally
```bash
pip install -r requirements.txt   # plus the tesseract binary (see README.md)
python app.py                      # serves on http://localhost:7860
```
