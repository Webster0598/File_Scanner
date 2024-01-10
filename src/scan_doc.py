def ignore_char(arg):
    ignored_chars = ['\n', '|']

    if arg in ignored_chars:
        return True

    return False


def contains_numbers(str):

    for s in str:
        if s.isdigit() == True:
            return True

    return False

def is_keyword(search_word, kw_array):

    # O(km)
    for kw in kw_array:
        if search_word == kw:
            return True

    return False

def sub_search(center_index, radius, text_array, manager):

    start = center_index - radius
    end = center_index + radius

    if start < 0:
        print("Error: Search out of lower bounds")
        return None
    if end > len(text_array):
        print("Error: Search out of upper bounds")
        return None

    subarray = text_array[start:end]

    print("")
    print(">>> Start of subarray <<<")
    print(subarray)
    print(">>> end of subarray <<<")
    print("")

    i = 0
    word = ""

    for t in subarray:

        if ignore_char(t):
            continue

        if t == " ":

            manager.extract_data(word)

            word = ""

        else:
            word += t

    print(manager.get_data())

def scan_doc(doc_text, kws, manager):
    word = ""
    i = 0

    for t in doc_text:

        if ignore_char(t):
            continue

        if t == " ":
            if word != "":
                # print(word, i)

                if is_keyword(word, kws):
                    print(word, " is a keyword ", " index ", i)
                    sub_search(i, 50, doc_text, manager)

                word = ""

        else:
            word += t

        i += 1