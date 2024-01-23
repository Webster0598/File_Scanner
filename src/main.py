from pytesseract import pytesseract
from PIL import Image
from pdf2image import convert_from_path

import text_data_extrac.scan_doc as sd
from text_data_extrac.Date_Manager import Date_Manager_Class
from text_data_extrac.Phone_Manager import Phone_Manager_Class
from text_data_extrac.Name_Manager import Name_Manager_Class
import os

def covert_image(pdf_file_path):

    images = convert_from_path(pdf_file_path, poppler_path = r"C:\Program Files (x86)\poppler-23.11.0\Library\bin")

    # for i in range(len(images)):
    #     # Save pages as images in the pdf
    #     images[i].save('page' + str(i) + '.jpg', 'JPEG')

    return images

def file_ending(file_path):

    if(len(file_path) < 3):
        print("Error: File path too short")
        return None

    return file_path[len(file_path) - 3:]



script_dir = os.path.dirname(__file__)
rel_path = "../sample_docs/text_example.pdf"
abs_file_path = os.path.join(script_dir, rel_path)

path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

date_keywords = ["Birth"]
date_manager = Date_Manager_Class(date_keywords)

phone_keywords = ["Phone", "Fax"]
phone_manager = Phone_Manager_Class(phone_keywords)

name_keywords = ["Patient", "Physician", "Name"]
name_manager = Name_Manager_Class(name_keywords)

managers = [date_manager, phone_manager, name_manager]

if __name__ == '__main__':

    ending = file_ending(abs_file_path)

    if ending == "pdf":

        img = covert_image(abs_file_path)

        file_ending(abs_file_path)

        for i in img:
            text = pytesseract.image_to_string(i)

            text_data = sd.scan_doc(text, managers)
            print(text_data)

    else:

        img = Image.open(abs_file_path)
        text = pytesseract.image_to_string(img)

        text_data = sd.scan_doc(text, managers)
        print(text_data)
