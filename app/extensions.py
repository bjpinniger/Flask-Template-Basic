from flask_pymongo import PyMongo
from flask import jsonify
from datetime import date, datetime, timedelta
import json
from config import Config
import pprint as pp

mongo = PyMongo()

class Extensions:

    #add database functions below

    def get_users():
        collection = mongo.db.users
        users_list = []
        for user in collection.find():
            user_object = {}
            user_object['name'] = user["Name"]
            user_object['avatar'] = user["Picture"]
            user_object['email'] = user["Email"]
            users_list.append(user_object)
        return users_list
