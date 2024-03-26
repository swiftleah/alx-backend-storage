#!/usr/bin/env python3
''' lists all documents in collection '''


def list_all(mongo_collection):
    ''' function '''
    docs = mongo_collection.find()

    return docs
