#!/usr/bin/env python3

def count_words(string_input):

    word_list = string_input.split()
    word_count = 0

    for word in word_list:
        word_count += 1

    return word_count


def classify_characters(string_input):

    string_input = string_input.lower()
    word_list = string_input.split()
    char_count = dict()

    for word in word_list:
        for char in word:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
    return char_count
