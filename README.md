# OCR

A minimal Jupyter notebook that extracts text from an image using
[Tesseract](https://github.com/tesseract-ocr/tesseract) via the
[`pytesseract`](https://pypi.org/project/pytesseract/) Python binding.

Designed to run **locally** (macOS / Linux / Windows) **or** on
**Google Colab** with no code changes.

---

## What it does

Given an image file (`.jpg`, `.png`, etc.), the notebook:

1. Loads the image with Pillow (`PIL`).
2. Runs Tesseract OCR via `pytesseract.image_to_string`.
3. Prints the extracted text.

That's the whole pipeline — one Pillow call, one Tesseract call.

---

## Requirements

- **Python 3.8+**
- **Tesseract** (the OCR engine itself, not the Python package):
  | OS | Install |
  | --- | --- |
  | macOS | `brew install tesseract` |
  | Ubuntu / Debian | `sudo apt-get install -y tesseract-ocr` |
  | Windows | [UB Mannheim installer](https://github.com/UB-Mannheim/tesseract/wiki) |
  | Google Colab | run the install cell in the notebook |
- **Python packages** (see `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```

---

## Usage

### Locally (Jupyter / VS Code)

```bash
git clone https://github.com/coderpro2409/ocr.git
cd ocr
pip install -r requirements.txt
jupyter notebook OCR.ipynb
```

Drop your image next to the notebook (or update `image_path` in the last
cell) and run all cells.

### On Google Colab

1. Open `OCR.ipynb` in Colab.
2. Run the **Colab install** cell first (`!apt-get install ...`).
3. Upload your image via the Files pane in the sidebar.
4. Set `image_path = "/content/<your-file>"` and run the OCR cell.

---

## Project structure

```
ocr/
├── OCR.ipynb         # The notebook
├── requirements.txt  # pytesseract, Pillow
├── .gitignore
├── LICENSE           # MIT
└── README.md
```

---

## Notes & limitations

- Tesseract works best on **clear, high-contrast text**. Photos of
  handwritten or skewed pages will need pre-processing (binarization,
  deskewing, denoising) for good results.
- The notebook uses the default Tesseract language (English). To OCR
  other languages, install the relevant language pack and pass
  `lang="..."` to `image_to_string`.

---

## License

[MIT](./LICENSE)
