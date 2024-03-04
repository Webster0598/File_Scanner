def ignore_char(arg):
    # Checks if string needs to ignored while iterating through
    # document data.

    ignored_chars = ['\n', '|']

    if arg in ignored_chars:
        return True

    return False


def contains_numbers(str):
    # Checks if a string contains any numbers.

    for s in str:
        if s.isdigit() == True:
            return True

    return False

def sub_search(center_index, radius, text_array, manager, keyword):

    # Preforms search on a smaller part of the text array.
    # The radius value determines of large the search area is.
    # The center index determines the point search area should start in the text array.

    start = center_index - radius
    end = center_index + radius

    # Ensures the search area remains within valid array boundaries.
    if start < 0:
        start = 0

    if end > len(text_array) :
        end = len(text_array)

    subarray = text_array[start:end]

    # Chosen manager will attempt to extract data from the subarray
    manager.add_data(subarray, keyword)



def scan_doc(doc_text, managers):

    # Iterates through the entire text array trying to find keywords associated with
    # the different data managers. Once a key word is found then a sub search is
    # started on a small section of the text array where the keyword was found.
    # The appropriate manager will look through this subarray for any data that is related
    # to that manager and save it.

    word = ""
    i = 0

    # Removes any new lines from the text array
    doc_text = doc_text.replace("\n", "")

    for t in doc_text:

        # Skips over certain characters in the text array
        if ignore_char(t):
            continue

        if t == " ":
            if word != "":

                # Checks each manager for a keyword match
                for mag in managers:
                    kw = mag.keyword_match(word)

                    if kw:
                        # If a keyword is found then subsearch is started.
                        sub_search(i, 50, doc_text, mag, kw)
                        break

                word = ""

        else:
            word += t

        i += 1

    doc_data = []

    # Goes through all the data collected by the different managers,
    # then appends the data together to create the final output.
    for mag in managers:
        doc_data.append(mag.data)

    return doc_data