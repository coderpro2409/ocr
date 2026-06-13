# OCR Notebook: Low-Level Design

> Version 1.0 - describes `OCR.ipynb` as it stands today.

## 1. Architecture

Three concrete steps and one branch:

```
image_path
    |
    v
[exists?] -- no --> raise FileNotFoundError
    |
    yes
    |
    v
PIL.Image.open(image_path)
    |
    v
pytesseract.image_to_string(image)
    |
    v
print(extracted_text)
```

## 2. Files in the repo

| File | Purpose |
|---|---|
| `OCR.ipynb` | The notebook itself. Three markdown cells and two code cells |
| `requirements.txt` | `pytesseract`, `pillow` |
| `README.md` | Per-OS install steps, Colab instructions, troubleshooting for `TesseractNotFoundError` |
| `LICENSE` | License |

## 3. Notebook cells

| Cell ID | Type | Contents |
|---|---|---|
| `intro` | markdown | Title, setup table per OS, link to `requirements.txt` |
| `colab-setup` | markdown | "Colab-only install" header |
| `colab-install` | code | `!apt-get install -y tesseract-ocr` and `!pip install pytesseract pillow` |
| `run-header` | markdown | "Run OCR on an image" |
| `ocr-run` | code | The four steps in section 1 |

## 4. Dependencies

| Layer | Component | Version range |
|---|---|---|
| System | Tesseract OCR binary | 4.x or 5.x (any modern build) |
| Python | `pytesseract` | latest stable |
| Python | `Pillow` | latest stable |
| Runtime | Python | 3.8 and above |

## 5. Failure modes

| Condition | Behavior | User action |
|---|---|---|
| `image_path` does not exist | `FileNotFoundError` is raised by the notebook (explicit check) | Verify the path; for Colab, re-upload and use `/content/<file>` |
| Tesseract binary not on `PATH` | `pytesseract.pytesseract.TesseractNotFoundError` from the OCR call | Install via the OS package manager, or set `pytesseract.pytesseract.tesseract_cmd` to the install path |
| Image file is unsupported by PIL | PIL raises `UnidentifiedImageError` | Convert to PNG or JPEG before passing in |
| Image is blank or very low quality | Output is an empty string or garbage text | Out of scope; preprocess externally |

## 6. Security and privacy

- The notebook reads only the file at `image_path`. No network calls.
- No environment variables are read.
- Nothing is written to disk by the OCR step itself.

## 7. Cross-platform considerations

| OS | Tesseract install | Path override needed? |
|---|---|---|
| macOS | `brew install tesseract` | No |
| Ubuntu / Debian | `sudo apt-get install -y tesseract-ocr` | No |
| Windows | UB Mannheim installer | Often yes: set `pytesseract.pytesseract.tesseract_cmd` to `C:\Program Files\Tesseract-OCR\tesseract.exe` |
| Google Colab | Run the `colab-install` cell | No |

## 8. Extension hooks

If a future contributor wants to extend the notebook without breaking the one-screen contract:

1. Add a `lang` parameter to `pytesseract.image_to_string(image, lang="eng+hin")` (one new keyword).
2. Wrap the run cell in `def ocr(image_path): ...` and call it once. Keeps the notebook one cell longer.
3. Loop over a folder of images. The current cell becomes a function call inside a `for` loop.

Each option stays within ten additional lines of code.
