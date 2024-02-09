def file_ending(file_path):

    if(len(file_path) < 3):
        print("Error: File path too short")
        return None

    return file_path[len(file_path) - 3:]