from src.text_data_extrac.Data_Manager import Data_Manager_Class
from src.text_data_extrac.scan_doc import ignore_char
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


        # word  = ""
        #
        # for a in subarray:
        #
        #     if ignore_char(a):
        #         continue
        #
        #     if a == " ":
        #
        #         if self.valid_data(word):
        #             self.data.append({ keyword : word })
        #
        #         word = ""
        #     else:
        #         word += a
        #
        # if self.valid_data(word):
        #     self.data.append({keyword: word})

    def valid_data(self, str_list):
        # Checks if a given string is a date.

        if str_list == None:
            return False

        print_str = str_list.replace("\n", "")

        # Check length
        if len(str_list) != 10:
            # print(print_str, " is not correct length to be date")
            return False

        # Check if '/' is in the right place
        if str_list[2] != '/' or str_list[5] != '/':
            # print(print_str, " does not have / in correct positions")
            return False

        new_str = ""

        for c in str_list:

            if c != '/':
                new_str += c

        # Check if all the characters are numbers
        for s in new_str:
            if s.isdigit() == False:
                # print(s, "is not a digit")
                return False

        # print(">>> ", print_str, " is a date <<<")

        return True





