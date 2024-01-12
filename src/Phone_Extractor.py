import Data_Manager as dm
class Phone_Extractor(dm.Data_Manager):

    def __init__(self, keywords):
        super().__init__(keywords)

    def valid_data(self, str_list):
        return False