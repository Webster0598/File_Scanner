class Data_Manager_Class:
    # This class is used as base for other data management class.
    # Contains common functions used by all datat management classes which
    # reduces redundant code.
    def __init__(self, keywords):
        self.keywords = keywords

    def keyword_match(self, word):
        # Checks if word matches the keywords associated with a data management class.
        # For example: "Phone" with is associated the Phone Manager class.

        for k in self.keywords:
            if k in word:
                # print("Match", k, word)
                return k

        return None

    def add_data(self, subarray):
        print(self, "Warning: Calling abstract parent class function. Should be overriden by child class.")
        pass

