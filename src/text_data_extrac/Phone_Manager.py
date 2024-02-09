from src.text_data_extrac.Data_Manager import Data_Manager_Class
import re

class Phone_Manager_Class(Data_Manager_Class):

    def __init__(self, keywords):
        super().__init__(keywords)

        self.reg_exps = [r'\+\d\d\d\d\d\d\d\d\d\d\d', r'\d\d\d-\d\d\d\d-\d\d\d\d']
        self.max_phone_digits = 10
        self. extra_phone_char = ["(", ")", "-", "+"]


    def is_extra_phone_char(self, arg):

        for c in self.extra_phone_char:

            if c == arg:
                return True

        return False

    def contains_extra_phone_char(self, arg):

        for a in arg:
            if a in self.extra_phone_char:
                return True

        return False

    def valid_data(self, str_list):

        phone = ""
        count = 0

        for s in str_list:

            if s.isdigit():
                phone += s
                count += 1

            elif self.is_extra_phone_char(s):
                continue

            else:
                return False

        if count != self.max_phone_digits:
            return False

        return True


    def find_rex_expprestion(self, reg, subarray, keyword):

        phoneNumRegex = re.compile(reg)
        match = phoneNumRegex.search(subarray)

        if match:
            print('found', match.group())

            self.data.append({keyword: match.group()})


    def add_data(self, subarray, keyword):

        for r in self.reg_exps:
            self.find_rex_expprestion(r, subarray, keyword)

        # self.find_rex_expprestion(r'\+\d\d\d\d\d\d\d\d\d\d\d', subarray, keyword)
        # self.find_rex_expprestion(r'\d\d\d-\d\d\d\d-\d\d\d\d', subarray, keyword)

                # extract_numbers = False
        # count = 0
        # phone = ""
        # phones_dic = {}
        # i = 0
        #
        # print(subarray)
        #
        # for s in subarray:
        #
        #     if s == " ":
        #         continue
        #
        #     if extract_numbers == False:
        #
        #         if s.isdigit():
        #             extract_numbers = True
        #             phone = s
        #             count = 1
        #
        #     else:
        #
        #         if self.is_extra_phone_char(s):
        #             phone += s
        #
        #         elif s.isdigit():
        #             phone += s
        #             count += 1
        #             # print(phone)
        #             if count == self.max_phone_digits:
        #
        #                 if self.contains_extra_phone_char(phone):
        #                     phones_dic[i] = phone
        #
        #                 extract_numbers = False
        #                 phone = ""
        #                 count = 0
        #
        #         else:
        #             extract_numbers = False
        #             phone = ""
        #             count = 0
        #
        #
        #     i +=1
        #
        # subarray_midpoint = len(subarray) // 2
        # smallest_delta = 999999
        # smallest_key = -1
        #
        # for key, value in phones_dic.items():
        #     delta = abs(subarray_midpoint - key)
        #
        #     if delta < smallest_delta:
        #         smallest_key = key
        #         smallest_delta = delta
        #
        # if smallest_key != -1:
        #     self.data.append({keyword : phones_dic[smallest_key]})