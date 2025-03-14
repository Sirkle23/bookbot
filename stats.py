def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_char_count(book_text):
    char_count = {}

    for char in book_text:
        if char.isalpha() == False:
            continue

        if char_count.get(char.lower()) == None:
            char_count[char.lower()] = 1
        else:
            char_count[char.lower()] += 1
    
    return char_count

def sort_on(dict):
    return dict["count"]

def sort_dict_by_value(dict):
    new_dict = []

    for item in dict:
        new_dict.append({"name": item, "count": dict[item]})

    sorted_dict = new_dict.sort(reverse=True, key=sort_on)
    
    return new_dict
        