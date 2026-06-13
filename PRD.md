# OCR Notebook: PRD

This is a notebook. It exists because every six months I find myself reinstalling `pytesseract` to pull text out of one image, and every six months I forget the Windows install quirk. So I wrote the smallest possible notebook that runs the same way on macOS, Linux, Windows, and Colab.

The whole product is: set `image_path`, run one cell, get text. There's no Layout API, no multi-language flag, no batch mode, no confidence scores. If you want any of that, you want a different project.

## Who this is for

Anyone who needs to OCR one image right now. In practice that's me, the occasional student trying to extract text from a photo of a printed page, and people on Stack Overflow who land here looking for the simplest possible Tesseract example.

## What it does and doesn't do

It does:

- Read one image from `image_path`.
- Raise `FileNotFoundError` with the path if it's missing (because the default error is confusing).
- Run `pytesseract.image_to_string` and print the result.

It doesn't:

- Preprocess. If your image is rotated, threshold it yourself.
- Handle PDFs or multi-page formats. Convert to image first.
- Detect language. English by default; pass `lang=` if you need otherwise (one-line change).
- Recognize handwriting. Tesseract is bad at it; use a different model.
- Output anything besides plain text. No bounding boxes, no confidences.

## Done means

The runnable cell is under 15 lines. A new user on a fresh Colab runtime gets their first extraction in under three minutes. No external services. That's it.

## Risk that's worth naming

The only real risk is the install. Specifically, that someone installs the Python package `pytesseract` without installing the Tesseract binary and then gets `TesseractNotFoundError`, which doesn't say "you forgot the binary". The README and the notebook's setup cell both call this out. On Windows you also need to set `pytesseract.pytesseract.tesseract_cmd` to the install path; documented.

## What I'd add later, but won't yet

A CLI wrapper (`python ocr.py image.jpg`), a folder-of-images loop, a language flag. All trivial extensions, none worth bundling into v1.
