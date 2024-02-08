from pdf2image import convert_from_path
from pytesseract import pytesseract

def covert_image(pdf_file_path):

    images = convert_from_path(pdf_file_path, poppler_path = r"C:\Program Files (x86)\poppler-23.11.0\Library\bin")

    return images

def file_ending(file_path):

    if(len(file_path) < 3):
        print("Error: File path too short")
        return None

    return file_path[len(file_path) - 3:]


def convert_pdf(abs_file_path):

    ending = file_ending(abs_file_path)
    text_list = []

    if ending == "pdf":

        imgs = covert_image(abs_file_path)

        for i in imgs:

            text = pytesseract.image_to_string(i)
            text_list.append(text)

        return text_list


    return None
