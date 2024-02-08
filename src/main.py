from pytesseract import pytesseract
from PIL import Image
import text_data_extrac.scan_doc as sd
from text_data_extrac.Date_Manager import Date_Manager_Class
from text_data_extrac.Phone_Manager import Phone_Manager_Class
from text_data_extrac.Name_Manager import Name_Manager_Class
import web_browsing.web_browser as wb
import os
import text_data_extrac.pdf_convertion as pc

script_dir = os.path.dirname(__file__)
rel_path = "../sample_docs/referral_form.pdf"
abs_file_path = os.path.join(script_dir, rel_path)
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract
# img = Image.open(abs_file_path)
# text = pytesseract.image_to_string(img)


date_keywords = ["Birth"]
date_manager = Date_Manager_Class(date_keywords)

phone_keywords = ["Phone", "Fax", "Telephone"]
phone_manager = Phone_Manager_Class(phone_keywords)

name_keywords = ["Patient", "Physician"]
name_manager = Name_Manager_Class(name_keywords)

managers = [phone_manager]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    text_list = pc.convert_pdf(abs_file_path)
    print(len(text_list))
    print(text_list)

    text_data = sd.scan_doc(text_list[0], managers)

    print(text_data)

    # wb.start()









# See PyCharm help at https://www.jetbrains.com/help/pycharm/
