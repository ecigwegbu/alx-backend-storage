#!/usr/bin/env python3
"""15. Log stats - new version"""
import pymongo
from pymongo import MongoClient
# from bson.son import SON


if __name__ == '__main__':
    # setup workspace
    logdata = MongoClient().logs.nginx
    # print header
    print('{} logs'.format(logdata.count_documents({})))
    print('Methods:')
    # loop over all documents
    print('\tmethod GET: {}'.format(logdata.count_documents(
          {"method": "GET"})))
    print('\tmethod POST: {}'.format(logdata.count_documents(
          {"method": "POST"})))
    print('\tmethod PUT: {}'.format(logdata.count_documents(
          {"method": "PUT"})))
    print('\tmethod PATCH: {}'.format(logdata.count_documents(
          {"method": "PATCH"})))
    print('\tmethod DELETE: {}'.format(logdata.count_documents(
          {"method": "DELETE"})))
    print('{} status check'.format(logdata.count_documents(
          {"method": "GET", "path": "/status"})))
    print('IPs:')
    pipeline = [
        {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": -1}},
        {"$limit": 10}
    ]
    result = logdata.aggregate(pipeline)
    for record in result:
        print('\t{}: {}'.format(record["_id"], record["count"]))
