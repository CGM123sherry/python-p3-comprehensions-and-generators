#!/usr/bin/env python3

# def return_evens(num_list):
def return_evens(num_list):
    """
    This function takes a list of numbers and returns a list of even numbers from the input list.
    """
    # List comprehension to filter even numbers
    return [num for num in num_list if num % 2 == 0]




def make_exclamation(sentence_list):
    """
    This function takes a list of sentences and returns a new list where each sentence
    ends with an exclamation mark.
    """
    # Add an exclamation mark to each sentence in the list
    return [sentence + "!" for sentence in sentence_list]
