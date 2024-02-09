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

script_dir = os.path.dirname(__file__)
rel_path = "../sample_docs/doc_example.png"
abs_file_path = os.path.join(script_dir, rel_path)
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract

date_keywords = ["Birth"]
date_manager = Date_Manager_Class(date_keywords)

phone_keywords = ["Phone", "Fax", "Telephone"]
phone_manager = Phone_Manager_Class(phone_keywords)

name_keywords = ["Patient", "Physician"]
name_manager = Name_Manager_Class(name_keywords)

managers = [phone_manager]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    if exists(abs_file_path):

        ending = file_ending(abs_file_path)

        if ending == "pdf":
            text_list = pc.convert_pdf(abs_file_path)
            print(len(text_list))
            print(text_list)

            text_data = sd.scan_doc(text_list[0], managers)
            print(text_data)

        elif ending == "png":

            print("png file ending")
            img = Image.open(abs_file_path)
            text = pytesseract.image_to_string(img)
            print(text)

        else:
            print("Error: Unknown file ending: ", ending)

    else:
        print("Error: ", abs_file_path, " can not be found")

    # wb.start()









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
