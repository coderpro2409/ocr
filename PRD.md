# OCR Notebook: Product Requirements Document

> Version 1.0 - matches the v1 notebook at `OCR.ipynb`.

## 1. Problem

A common everyday task: pull text out of a single image quickly. A phone photo of a printed page, a screenshot of a non-selectable PDF, a scanned receipt. Existing tools fall into two camps:

1. Heavy desktop applications (Adobe Acrobat, ABBYY FineReader) that are overkill for one image.
2. Full Python pipelines that bundle preprocessing, layout detection, multi-language handling, and PDF support, when the user just wants raw text.

This project sits in the gap between them: a Jupyter notebook with one image in and one string out.

## 2. Target users

| User | Need |
|---|---|
| Student | Extract text from a photo of a printed page or a whiteboard |
| Developer prototyping | Sanity-check Tesseract on their image before adopting a heavier stack |
| Anyone curious about OCR | Run an end-to-end OCR pipeline in under three minutes |

## 3. Goals

1. The whole runnable pipeline fits on one screen.
2. Setup takes under three minutes from a fresh environment.
3. The same notebook runs without code changes on macOS, Linux, Windows, and Google Colab.

## 4. Non-goals

1. Layout-aware extraction (tables, columns, reading order).
2. Multi-page documents (PDF, TIFF stacks).
3. Handwriting recognition.
4. Multi-language auto-detection.
5. Pre-processing (deskew, threshold, denoise). The user controls image quality before passing it in.
6. Confidence scores, bounding boxes, or word-level output. Plain text only.

## 5. User journeys

### 5.1 Run on Colab (zero local setup)

1. Open the notebook on Colab.
2. Run the Colab install cell (installs `tesseract-ocr` and `pytesseract`).
3. Upload an image via the Files pane.
4. Set `image_path = "/content/<filename>"`.
5. Run the OCR cell. Extracted text prints below.

### 5.2 Run locally

1. Install the Tesseract binary via the system package manager (`brew`, `apt`, or the UB Mannheim Windows build).
2. `pip install -r requirements.txt`.
3. Set `image_path` to an absolute or relative path to the image.
4. Run the cell.

## 6. Functional requirements

- **F1.** Read a single image file from the variable `image_path`.
- **F2.** Raise `FileNotFoundError` with the missing path if the file does not exist.
- **F3.** Run Tesseract OCR via `pytesseract.image_to_string`.
- **F4.** Print the extracted text to the notebook output.

## 7. Non-functional requirements

- **N1. Offline by default.** No network calls after Tesseract is installed.
- **N2. Cross-platform.** No code paths branch on operating system; the user adjusts only the Tesseract install method.
- **N3. Readability.** The runnable cell stays under 15 lines of Python.

## 8. Success metrics

| Metric | Target |
|---|---|
| Time from a fresh Colab runtime to the first extraction | under 3 minutes |
| Lines of executable Python | under 15 |
| External services required at runtime | 0 |

## 9. Risks

| Risk | Mitigation |
|---|---|
| User installs only the Python package, not the Tesseract binary, and hits `TesseractNotFoundError` | README and notebook setup cell call this out explicitly |
| Image rotation or low contrast gives poor results | Out of scope; the README notes that image quality is the user's responsibility |
| Windows install path differs from `PATH` | README documents the `pytesseract.pytesseract.tesseract_cmd` override |

## 10. Future work (explicitly deferred)

1. CLI wrapper (`python ocr.py image.jpg`).
2. Multi-image batch mode.
3. Language flag passthrough (`lang="eng+hin"`).
4. Output to file instead of stdout.
