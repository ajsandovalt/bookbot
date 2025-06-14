#!/usr/bin/env python3


from stats import count_words, classify_characters


def get_book_text(file_path):
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content


def main():
    book_string = get_book_text("books/frankenstein.txt")
    print(f"{count_words(book_string)} words found in the document")
    print(classify_characters(book_string))


main()
