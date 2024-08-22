#!/usr/bin/env python3
"""Python Mongodb"""

from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """function that inserts a new document in a collection based on kwargs:"""
    inseted_object = mongo_collection.insert_one(kwargs)
    return inseted_object.inserted_id
