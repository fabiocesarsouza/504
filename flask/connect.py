from pymongo import MongoClient

def mongo_connect():
    con = MongoClient()
    return con['projeto']

def mongo_close():
    pass    