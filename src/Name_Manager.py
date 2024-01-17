import Data_Manager as dm
import nltk

class Name_Manager(dm.Data_Manager):

    def __init__(self, keywords):
        super().__init__(keywords)

    def test(self):

        sentence = """At eight o'clock on Thursday morning
        ... Arthur didn't feel very good."""

        tokens = nltk.word_tokenize(sentence)
        tagged = nltk.pos_tag(tokens)

        print(tagged)