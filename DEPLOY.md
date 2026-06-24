# Deploying the OCR app

Deployed as a **Gradio web app on Hugging Face Spaces** (free CPU). This is the
web version of the notebook pipeline (Pillow -> pytesseract). `app.py` is the
entrypoint; `packages.txt` installs the Tesseract system binary.

> Note: Vercel cannot host this. Tesseract is a system binary that must be
> apt-installed, which serverless functions don't support. The original
> `ot4.py` (tkinter + Surya + local llama-server) is a desktop/GPU script and
> is left in the repo for reference only; it is not the deployed app.

## Steps (Hugging Face Spaces)
1. Create a Space at https://huggingface.co/new-space → **SDK: Gradio**, hardware **CPU basic** (free).
2. Push this repo's contents to the Space (or connect the GitHub repo). The
   Space needs `app.py`, `requirements.txt`, and `packages.txt`.
3. Add this YAML to the **top of the Space's `README.md`** so HF builds it correctly:
   ```yaml
   ---
   title: OCR Image to Text
   sdk: gradio
   app_file: app.py
   ---
   ```
4. The Space builds (apt-installs `tesseract-ocr`, pip-installs deps) and serves
   the upload UI. No API key needed.

## Run locally
```bash
pip install -r requirements.txt   # plus the tesseract binary (see README.md)
python app.py
```
