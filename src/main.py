from pytesseract import pytesseract
from PIL import Image
from src.Date_Manager import Date_Manager
from Phone_Manager import Phone_Manager
from Name_Manager import Name_Manager
import os
import scan_doc as sd

script_dir = os.path.dirname(__file__)
rel_path = "../sample_docs/doc_example.png"
abs_file_path = os.path.join(script_dir, rel_path)
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(abs_file_path)
text = pytesseract.image_to_string(img)


date_keywords = ["Birth:"]
date_manager = Date_Manager(date_keywords)

phone_keywords = ["Phone:", "Fax:"]
phone_manager = Phone_Manager(phone_keywords)

name_keywords = ["Patient:"]
name_manager = Name_Manager(name_keywords)

managers = [date_manager, phone_manager]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # test1 = "(510) 922-8611"
    # test2 = "(510) 922-8611abc (510) 922-8611"
    # test3 = "(510) 92k2-8611abc (510) 922-8611"
    # phone_manager.add_data(test1)
    # print(sd.scan_doc(text, managers))

    name_manager.test()








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
