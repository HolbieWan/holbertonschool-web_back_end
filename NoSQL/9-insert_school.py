#!/usr/bin/env python3
"""Python Mongodb"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs:"""
    inserted_object = mongo_collection.insert_one(kwargs)
    return inserted_object.inserted_id
