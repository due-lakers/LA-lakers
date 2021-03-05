import pymongo

db_name = 'lakers'
col_name = 'predict'
uri = "mongodb://localhost:27017/"


def connect():
    client = pymongo.MongoClient(uri)
    return client


def initDB(db_name, col_name):
    client = connect()
    mydb = client[db_name]
    mycol = mydb[col_name]


def getCol(db_name, col_name):
    return connect()[db_name][col_name]


def getResult(result):
    return getCol(db_name, col_name).count_documents({"result": result})


def getAll(db_name, col_name):
    return getCol(db_name, col_name).count_documents({})


def getRecentNums(db_name, col_name):
    pipeline = [
        {"$sort": {"createTime": 1}},
        {"$project": {"_id": 1, "createTime": {"$substr": ["$createTime", 0, 10]}}},
        {"$group": {"_id": {"createTime": "$createTime"}, "count": {"$sum": 1}}}
    ]
    res = []
    for info in getCol(db_name, col_name).aggregate(pipeline):
        res.append([info['_id']['createTime'], info['count']])
    return res


def insert(col_name, new_doc):
    try:
        coll = getCol(db_name, col_name)
        result = coll.insert_one(new_doc)
        print('inserted_id %s' % repr(result.inserted_id))
        return 'ok'
    except Exception as e:
        print(e)
        return str(e)
