#!/usr/bin/env python3
"""8. List all documents in Python"""


def list_all(mongo_collection):
    """
    Write a Python function that lists all documents in a collection:

    Prototype: def list_all(mongo_collection):
    Return an empty list if no document in the collection
    mongo_collection will be the pymongo collection object
    """
    return mongo_collection.find()
