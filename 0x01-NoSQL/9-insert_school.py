#!/usr/bin/env python3
''' python function MongoDB '''


def insert_school(mongo_collection, **kwargs):
    ''' inserts a new doc in collection based on kwargs '''
    insert = mongo_collection.insert_one(kwargs)
    return insert.inserted_id
