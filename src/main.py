from pytesseract import pytesseract
from PIL import Image
from src.date_extration import Date_Extractor
import os

script_dir = os.path.dirname(__file__)
rel_path = "../sample_docs/doc_example.png"
abs_file_path = os.path.join(script_dir, rel_path)
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.tesseract_cmd = path_to_tesseract
img = Image.open(abs_file_path)
text = pytesseract.image_to_string(img)
date_manager = Date_Extractor()

keywords = ["Birth:", "Phone:", "Physician:"]

def ignore_char(arg):
    ignored_chars = ['\n', '|']

    if arg in ignored_chars:
        return True

    return False


def contains_numbers(str):

    for s in str:
        if s.isdigit() == True:
            return True

    return False

def is_keyword(search_word, kw_array):

    # O(km)
    for kw in kw_array:
        if search_word == kw:
            return True

    return False

def sub_search(center_index, radius, text_array):

    start = center_index - radius
    end = center_index + radius

    if start < 0:
        print("Error: Search out of lower bounds")
        return None
    if end > len(text_array):
        print("Error: Search out of upper bounds")
        return None

    subarray = text_array[start:end]

    print("")
    print(">>> Start of subarray <<<")
    print(subarray)
    print(">>> end of subarray <<<")
    print("")

    i = 0
    word = ""

    while i < len(subarray):

        t = subarray[i]

        if ignore_char(t):
            continue

        if t == " ":
            continue

        else:
            word += t


        i += 1



def scan_doc(doc_text, kws):
    word = ""
    i = 0

    for t in doc_text:
        if ignore_char(t):
            continue

        if t == " ":
            if word != "":
                # print(word, i)

                if is_keyword(word, keywords):
                    print(word, " is a keyword ", " index ", i)

                if contains_numbers(word):
                    date_manager.add_date(word)

                word = ""

        else:
            word += t

        i += 1

    print(date_manager.dates)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(text[:-1])
    # print()
    # print()
    # print()
    # print("<<<<<<<<<<>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>")
    scan_doc(text, keywords)








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
