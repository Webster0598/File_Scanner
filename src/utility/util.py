def file_ending(file_path):
    # Returns that last 3 characters of a string in order
    # to get its file ending.

    if(len(file_path) < 3):
        print("Error: File path too short")
        return None

    return file_path[len(file_path) - 3:]