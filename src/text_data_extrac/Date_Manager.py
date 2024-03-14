from src.text_data_extrac.Data_Manager import Data_Manager_Class
import re

class Date_Manager_Class(Data_Manager_Class):

    def __init__(self, keywords):
        super().__init__(keywords)

    def add_data(self, subarray):
        # Checks each word in a string array to see if it is a date.
        # If it is, then that data is stored within the class.

        chuck_1 = "\d{2}" + "\/"
        chuck_2 = "\d{2,4}"

        date_pattern = f"{chuck_1}{chuck_1}{chuck_2}"
        date_pattern_regex = re.compile(date_pattern)

        dates = date_pattern_regex.findall(subarray)

        print()
        print(dates, " found in ")
        print(subarray)

        return dates
