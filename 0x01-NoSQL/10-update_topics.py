#!/usr/bin/env python3
''' python script for MongoDB '''


def update_topics(mongo_collection, name, topics):
    ''' updates topics of school doc based on name '''
    mongo_collection.update_many(
            {'name': name},
            {"$set": {"topics": topics}}
)
