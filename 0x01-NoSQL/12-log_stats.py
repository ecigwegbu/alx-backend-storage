#!/usr/bin/env python3
"""12. Log Stats - provide some stats about a Mongo database dump"""
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
