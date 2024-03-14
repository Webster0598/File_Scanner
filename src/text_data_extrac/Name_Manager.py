from src.text_data_extrac.Data_Manager import Data_Manager_Class
import re
import spacy

class Name_Manager_Class(Data_Manager_Class):

    def __init__(self, keywords):
        super().__init__(keywords)

        # Load the English language model
        self.nlp = spacy.load("en_core_web_sm")

    def is_text_a_person(self, text):

        # Process the text with SpaCy
        doc = self.nlp(text)

        for ent in doc.ents:

            if ent.label_ == "PERSON":
                return True

        return False

    def add_data(self, subarray):

        chuck_1 = "[A-Z]"
        chuck_2 = "[a-z]+"
        chuck_3 = "\s"

        name_pattern = f"{chuck_1}{chuck_2}{chuck_3}{chuck_1}{chuck_2}"
        name_pattern_regex = re.compile(name_pattern)

        names = name_pattern_regex.findall(subarray)

        print()
        print(names)

        for n in names:
            if self.is_text_a_person(n):
                print(n, "is a person")

        return names