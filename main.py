#!/usr/bin/env python3

import sys
from pathlib import Path
from stats import count_words, classify_characters, sort_dict


def get_book_text(file_path):
    # Get the plain text from the txt file as a String
    content = ""
    with open(file_path) as f:
        content = f.read()
    return content


def full_report(file_path):
    # Print a pretty report
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
    try:
        # Check if there are more than 1 argument
        if len(sys.argv) != 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)
        # Check if extension is txt
        elif Path(sys.argv[1]).suffix.lower() != ".txt":
            raise Exception("Only txt files are allowed")
        else:
            # Run report!
            full_report(sys.argv[1])

    except Exception as e:
        print(f"Error, the following exception was encountered:\n{e}")
        print(":(")
        sys.exit(1)


main()
