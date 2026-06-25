"""
OCR web app: extract text from an uploaded image using Tesseract.

This is the deployable web version of the project's notebook pipeline
(Pillow -> pytesseract). It runs on a free CPU Hugging Face Space:
`packages.txt` installs the `tesseract-ocr` system binary, and Gradio
provides the upload UI (replacing the desktop tkinter dialog).
"""

import os

import gradio as gr
import pytesseract
from PIL import Image


def ocr_image(image, lang):
    if image is None:
        return "Please upload an image first."
    try:
        text = pytesseract.image_to_string(image, lang=lang or "eng")
    except Exception as e:
        return f"OCR error: {e}"
    return text.strip() or "No text detected."


demo = gr.Interface(
    fn=ocr_image,
    inputs=[
        gr.Image(type="pil", label="Image"),
        gr.Textbox(value="eng", label="Tesseract language code (e.g. eng, fra, deu, hin)"),
    ],
    outputs=gr.Textbox(label="Extracted text", lines=15),
    title="OCR: Image to Text",
    description="Upload an image and extract its text with Tesseract OCR.",
    flagging_mode="never",
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=int(os.getenv("PORT", "7860")))
