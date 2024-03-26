#!/usr/bin/env python3
''' python function mongodb '''


def top_students(mongo_collection):
    ''' returns all students sorted by average score '''
    topStudent = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
                }
            },
        {"$sort": {"averageScore": -1}}
        ])
    return topStudent
