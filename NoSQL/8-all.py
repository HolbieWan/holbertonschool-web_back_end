#!/usr/bin/env python3
"""Function to list all documents in a collection"""

from pymongo import MongoClient


def list_all(mongo_collection):
    """Function to list all documents in a collection"""
    documents = mongo_collection.find()
    return documents
