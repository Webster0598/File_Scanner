class Date_Extractor:

    def __init__(self):
        self.dates = []

    def add_date(self, new_date):
        if self.is_date(new_date):
            self.dates.append(new_date)

    def is_date(self, str_list):

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





