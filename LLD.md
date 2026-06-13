# OCR Notebook: LLD

The whole pipeline:

```
image_path
   |
   v
exists? --no--> raise FileNotFoundError
   |
   yes
   v
PIL.Image.open(image_path)
   |
   v
pytesseract.image_to_string(image)
   |
   v
print
```

That's it. There's nothing to architect.

## The notebook

Five cells. Two are markdown (the intro and the section header for the run cell). One is the optional Colab install. The other two are the markdown "Colab-only" header and the actual OCR cell.

The OCR cell:

```python
import os
import pytesseract
from PIL import Image

image_path = "image.jpg"

if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image not found: {image_path}")

extracted_text = pytesseract.image_to_string(Image.open(image_path))

print("----- Extracted Text -----")
print(extracted_text)
```

Fifteen lines including the print. If I add a `lang=` parameter someday, it becomes sixteen.

## Dependencies

System: Tesseract 4 or 5, installed via the OS package manager (`brew`, `apt`) or the UB Mannheim Windows build.

Python: `pytesseract`, `Pillow`. Both pinned to "latest stable" because neither has surprising minor-version churn.

Python version: 3.8 or above. Nothing here uses anything newer.

## Where it breaks

`image_path` doesn't exist: the explicit check raises `FileNotFoundError` with the path included. This is the most common user error; the default behavior (PIL raising deep inside the call) is unhelpful.

Tesseract binary not on PATH: `pytesseract.pytesseract.TesseractNotFoundError`. The fix is either an OS-level install or setting `pytesseract.pytesseract.tesseract_cmd`. README covers both.

Image PIL can't open (HEIC, TIFF without proper codec): `UnidentifiedImageError`. Convert to PNG or JPEG first.

Image is unreadably low quality: empty string or garbage. Out of scope.

## Privacy

No network calls. No env vars read. Nothing written to disk by the OCR step (the image came from disk, the text goes to stdout). Whatever you OCR stays on the machine.

## If someone extends this

Three extensions stay within ten extra lines:

1. `lang="eng+hin"` keyword to `image_to_string`.
2. Wrap the run cell in `def ocr(path): ...` and call it once.
3. Loop over a folder: `for f in os.listdir(folder): ocr(f)`.

Anything beyond that (CLI, batch with progress, multi-format input) belongs in a different project.
