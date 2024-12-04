#!/usr/bin/env python3
"""Module with bubble sort function
that sorts a list by ascending order"""

def bubble_sort(my_list):
    """function that sorts a list by ascending order"""

    for i in range(len(my_list)):
        for j in range(0, len(my_list) - i - 1):
            if my_list[j] > my_list[j + 1]:
                # Swap if elements are in the wrong order
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
