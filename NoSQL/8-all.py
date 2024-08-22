#!/usr/bin/env python3
"""Function to list all documents in a collection"""

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

def list_all(mongo_collection):
    documents = mongo_collection.find()
    return documents