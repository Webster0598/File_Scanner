from src.text_data_extrac.Data_Manager import Data_Manager_Class
import re

class Phone_Manager_Class(Data_Manager_Class):

    def __init__(self, keywords):
        super().__init__(keywords)


    def add_data(self, subarray):

        # Adds phone number to class data if there is reg exp match.

        chunk_1 = "\+?\d{0,1}-?"
        chunk_2 = "\(?" + "\d{3}" + "\)?" + "(?:-|\s)?"
        chunk_3 = "\d{3}" + "(?:-|\s)?"
        chunk_4 = "\d{4}"

        phone_pattern = f"{chunk_1}{chunk_2}{chunk_3}{chunk_4}"
        phone_pattern_regex = re.compile(phone_pattern)

        phone_numbers = phone_pattern_regex.findall(subarray)

        print()
        print(phone_numbers, " found in ")
        print(subarray)

        return phone_numbers
