file = 'frankenstein.txt'
path = 'books'
char_set = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'

def get_book(p, f):
    full_path = './' + p + '/' + f
    with open(full_path) as opened_file:
        file_contents = opened_file.read()
        return file_contents

full_text = get_book(path, file)


def wordcount(t):
    count = t.split()
    return len(count)

final_wordcount = wordcount(full_text)

def create_dictionary(t):
    initialized_dictionary = {}
    chars = t.split()
    for i in chars:
        initialized_dictionary[i] = 0
    return initialized_dictionary

initialized_dictionary = create_dictionary(char_set)

def charcount(t, d):
    lowercase_text = t.lower()
    for i in d:
        updated_count = lowercase_text.count(i)
        d[i] = updated_count
    return d

chars_dict = charcount(full_text, initialized_dictionary)

def main(p, f, wc, cd):
    print(f"--- Begin report of {p}/{f} ---")
    print(f"{wc} words found in the document")
    print("")
    for i in sorted(cd, key=cd.get, reverse=True):
        print(f"The \'{i}\' character was found {cd[i]} times")
    print("--- End report ---")





main(path, file, final_wordcount, chars_dict)