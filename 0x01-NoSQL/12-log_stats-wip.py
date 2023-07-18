#!/usr/bin/env python3
"""
    Write a Python script that provides some stats about Nginx logs
    stored in MongoDB:

    Database: logs
    Collection: nginx
    Display (same as the example):
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
    5 lines with the number of documents with the method = ["GET", "POST",
    "PUT", "PATCH", "DELETE"] in this order (see example below - warning:
    it's a tabulation before each line)
    one line with the number of documents with:
    method=GET
    path=/status
    You can use this dump as data sample: dump.zip

    The output of your script must be exactly the same as the example
"""
import pymongo
from pymongo import MongoClient


# setup workspace
logdata = MongoClient().logs.nginx

# print header
print('{} logs'.format(logdata.count_documents({})))
print('Methods:')

# loop over all documents


if __name__ == '__main__':
    pass
