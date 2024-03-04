from pdf2image import convert_from_path
from pytesseract import pytesseract
from src.utility.util import file_ending

def covert_image(pdf_file_path):
    # Coverts a pdf files into data that pytesseract can convert into text arrays.

    images = convert_from_path(pdf_file_path, poppler_path = r"C:\Program Files (x86)\poppler-23.11.0\Library\bin")

    return images


def convert_pdf(abs_file_path):

    ending = file_ending(abs_file_path)
    text_list = []

    if ending == "pdf":

        imgs = covert_image(abs_file_path)

        # Goes through each converted pdf data and has pytesseract
        # changes it into a text array. An array of arrays is created and returned.
        for i in imgs:

            text = pytesseract.image_to_string(i)
            text_list.append(text)

        return text_list


    return None
