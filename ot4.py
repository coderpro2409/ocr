#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Semantic OCR using Surya (Windows)
- File dialog to pick an image
- Automatically spawns llama.cpp backend
- Returns text in semantic reading order
"""

import tkinter as tk
from tkinter import filedialog
from PIL import Image
from surya.inference import SuryaInferenceManager
from surya.recognition import RecognitionPredictor
import streamlit as st

# Set your language (supports 90+ languages)
OCR_LANG = "en"   # e.g., "fr", "de", "es", "hi", or "en,fr" for mixed

def extract_text_with_surya(image_path: str, lang: str = "en") -> str:
    # 1. Create the inference manager – this will auto-spawn llama-server
    manager = SuryaInferenceManager()  # auto-spawns vllm or llama-server[reference:6]

    # 2. Create the recognition predictor
    recognizer = RecognitionPredictor(manager)

    # 3. Open the image
    img = Image.open(image_path)

    # 4. Run OCR – call the predictor directly with the image[reference:7]
    predictions = recognizer([img])

    # 5. Extract text from each block in reading order
    lines = []
    for page_result in predictions:
        # page_result.blocks contains the recognised text blocks in reading order[reference:8]
        for block in page_result.blocks:
            lines.append(block.html)  # block.html contains the extracted text

    return "\n".join(lines)

def select_file_and_ocr():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.tiff")]
    )
    if not file_path:
        print("No file selected.")
        return

    print(f"Processing: {file_path}")
    print("First run will download the model (~1.3GB) and start the server – please wait...")

    try:
        text = extract_text_with_surya(file_path, lang=OCR_LANG)
        print("\n" + "=" * 60)
        print("EXTRACTED TEXT (Semantic Order)")
        print("=" * 60)
        print(text if text.strip() else "No text detected.")
        st.write(text if text.strip() else "No text detected.",unsafe_allow_html=True)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    select_file_and_ocr()