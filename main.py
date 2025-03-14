def get_book_text(filename):
    with(open(filename)) as f:
        book_text = f.read()

    return book_text

def main():
    import sys
    from stats import get_word_count, get_char_count, sort_dict_by_value
    print(len(sys.argv))
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
    print(filepath)
    book_text = get_book_text(filepath)

    num_words = get_word_count(book_text)

    char_dict = get_char_count(book_text)

    sorted_dict = sort_dict_by_value(char_dict)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")

    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for item in sorted_dict:
        print(f"{item['name']}: {item['count']}")
    print(f"============= END ===============")

main()