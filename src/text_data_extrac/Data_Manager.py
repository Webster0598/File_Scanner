class Data_Manager_Class:
    def __init__(self, keywords):
        self.keywords = keywords
        self.data = []

    def keyword_match(self, word):

        for k in self.keywords:
            if k in word:
                # print("Match", k, word)
                return k

        return None

    def get_data(self):
        return self.data

    def clear_data(self):
        self.data = []

    def valid_data(self, arg):
        print(self, "Warning: Calling abstract parent class function. Should be overriden by child class.")
        return False

    def add_data(self, subarray, keyword):
        print(self, "Warning: Calling abstract parent class function. Should be overriden by child class.")
        pass

