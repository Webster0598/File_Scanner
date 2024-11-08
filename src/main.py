from PIL import Image
from pytesseract import pytesseract
import text_data_extrac.scan_doc as sd
from text_data_extrac.Date_Manager import Date_Manager_Class
from text_data_extrac.Phone_Manager import Phone_Manager_Class
from text_data_extrac.Name_Manager import Name_Manager_Class
import os
import src.utility.pdf_convertion as pc
from os.path import exists
from src.utility.util import file_ending
import web_browsing.web_browser as wb
import auto_inputs.keyboard_mouse_auto as auto

# Creates all the files paths
script_dir = os.path.dirname(__file__)
rel_path = "../sample_docs/doc_example.png"
abs_file_path = os.path.join(script_dir, rel_path)

# Pytesseract coverts images into text data.
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path_to_tesseract

# Creates the all managers that will collect the data.
date_keywords = ["Birth"]
date_manager = Date_Manager_Class(date_keywords)

phone_keywords = ["Phone", "Fax", "Telephone"]
phone_manager = Phone_Manager_Class(phone_keywords)

name_keywords = ["Patient", "Physician"]
name_manager = Name_Manager_Class(name_keywords)

managers = [phone_manager]


def start(abs_file_path):
    # Coverts image file into a string list

    # Checks if file exist
    if exists(abs_file_path):

        ending = file_ending(abs_file_path)
        # Coverts pdf into string list
        if ending == "pdf":

            text_list = pc.convert_pdf(abs_file_path)
            text_data = sd.scan_doc(text_list[0], managers)
            print(text_data)

        # Coverts png file into to string list
        elif ending == "png":

            img = Image.open(abs_file_path)
            text = pytesseract.image_to_string(img)
            text_data = sd.scan_doc(text, managers)

        else:
            print("Error: Unknown file ending: ", ending)

    else:
        print("Error: ", abs_file_path, " can not be found")

if __name__ == '__main__':

    # start(abs_file_path)
    # wb.read_login_date("login/login_data.txt")
    # wb.start()
    auto.start()
