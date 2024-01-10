from pytesseract import pytesseract
from PIL import Image
from src.date_extration import Date_Extractor
import os
import scan_doc as sd

script_dir = os.path.dirname(__file__)
rel_path = "../sample_docs/doc_example.png"
abs_file_path = os.path.join(script_dir, rel_path)
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(abs_file_path)
text = pytesseract.image_to_string(img)
date_manager = Date_Extractor()

keywords = ["Birth:"]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(text[:-1])

    sd.scan_doc(text, keywords, date_manager)








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
