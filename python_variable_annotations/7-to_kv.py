#!/usr/bin/env python3
"""Module with a function that takes 2 arguments
and returns them in a tuple"""


def to_kv(k: str, v: int | float) -> tuple:
    """type-annotated function to_kv that takes a string k
    and an int OR float v as arguments and returns a tuple"""
    return (k, float(v**2))
