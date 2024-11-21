import os
import json


import pdfplumber

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    return text

def read_files_in_directory_as_json(directory_path):
    try:
        file_content_map = {}
        for filename in os.listdir(directory_path):
            file_path = os.path.join(directory_path, filename)

            if os.path.isfile(file_path):
                try:
                    text = extract_text_from_pdf(file_path)
                    print(text)
                    file_content_map[filename] = text
                except Exception as file_error:
                    print(f"Error reading file {filename}: {file_error}")

        return file_content_map
    except Exception as e:
        print(f"An error occurred while processing the directory: {e}")
        return {}

