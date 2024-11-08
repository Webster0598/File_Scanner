import shelve

def save(file_path, doc_data):

    shelfFile = shelve.open(file_path)

    for key, value in doc_data.items():
        shelfFile[key] = value

    shelfFile.close()

def open(file_path):

    shelfFile = shelve.open(file_path)
    print(type(shelfFile))
    print(shelfFile['Name'])
    shelfFile.close()