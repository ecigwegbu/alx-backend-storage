#!/usr/bin/env python3
"""14. Top students sorted by average score"""
import pymongo


def top_students(mongo_collection):
    """
    Write a Python function that returns all students sorted by average score:
    Prototype: def top_students(mongo_collection):
    mongo_collection will be the pymongo collection object
    The top must be ordered
    The average score must be part of each item returns with key = averageScore
    """
    pipeline = [
        {"$unwind": '$topics'},
        {"$group": {"_id": "$_id", "averageScore": {"$avg": '$topics.score'}}},
        # {$group: { '_id': '$_id', averageScore: {$avg: '$topics.score' }}},
        # {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"averageScore": -1, "_id": -1}},
        {"$limit": 10}
    ]
    result = mongo_collection.aggregate(pipeline)
    # print(result)
    for record in result:
        print("[{}] {} => {}".format(record.get("_id"), record.get("name"),
                                     record.get("averageScore")))
    return result
