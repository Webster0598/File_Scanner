from src.text_data_extrac.Data_Manager import Data_Manager_Class
# import enchant
# import nltk
# from nltk.tag.stanford import StanfordNERTagger

# nltk.download('popular') Installs datasets/models for nltk to work.
# Only needs to be runs once. Probably should be ran from command line instead of code.

class Name_Manager_Class(Data_Manager_Class):

    def __init__(self, keywords):
        super().__init__(keywords)

    def is_capitalized(self, str):

        if str == "":
            return False

        if str[0].isupper():
            return True

        return False

    def add_data(self, subarray, keyword):

        proper_noun = []
        word = ""
        count = 0
        keyword_index = -1

        # print(subarray)
        for s in subarray:

            if s == " ":

                if self.is_capitalized(word):
                    proper_noun.append(word)
                    count += 1

                    if self.keyword_match(word):
                        keyword_index = count - 1


                word = ""

            else:

                if s.isalpha():
                    word += s

        if self.is_capitalized(word):
            proper_noun.append(word)

        # print(proper_noun, "keyword_index", keyword_index)

        name = proper_noun[keyword_index + 1] + " " + proper_noun[keyword_index + 2]

        # print("Name: ", name)

        self.data.append({keyword : name})



