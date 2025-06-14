#!/usr/bin/env python3

def count_words(string_input):
    # Get the total number of words present in a string

    word_list = string_input.split()
    word_count = 0

    for word in word_list:
        word_count += 1

    return word_count


def classify_characters(string_input):
    # Classifies characters present in a string in a unordered dictionary
    # returns {char: num_of_chars}

    string_input = string_input.lower()
    word_list = string_input.split()
    char_count = dict()

    for word in word_list:
        for char in word:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
    return char_count


def get_val(dict):
    # Why????
    return dict["num"]


def sort_dict(dict):
    # Makes a list of dictionaries, and orders the elements by "num".
    # returns [{"char": char, "num": num_of_chars}, {...}]
    sorted_list = []

    for key in dict:
        if key.isalpha():
            sorted_list.append({"char": key, "num": dict[key]})
    sorted_list.sort(reverse=True, key=get_val)
    return sorted_list
