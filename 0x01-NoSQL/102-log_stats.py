#!/usr/bin/env python3
"""12. Log Stats - provide some stats about a Mongo database dump"""
import pymongo
from pymongo import MongoClient


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
