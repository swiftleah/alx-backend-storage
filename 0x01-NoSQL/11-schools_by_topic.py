#!/usr/bin/env python3
''' python function MongoDB '''


def schools_by_topic(mongo_collection, topic):
    ''' returns list of school having specific topic '''
    docs = mongo_collection.find({"topics": topic})
    return list(docs)
