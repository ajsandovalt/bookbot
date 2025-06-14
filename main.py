#!/usr/bin/env python3


from stats import count_words, classify_characters, sort_dict


def get_book_text(file_path):
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content


def full_report(file_path):
    book_string = get_book_text(file_path)
    sorted_characters_dict = sort_dict(classify_characters(book_string))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book_string)} total words")
    print("--------- Character Count -------")
    for dict in sorted_characters_dict:
        print(f"{dict['char']}: {dict['num']}")
    pass


def main():
    file_path = "books/frankenstein.txt"
    full_report(file_path)


main()
