import sys
import json
import pymongo
from pymongo import MongoClient
from datetime import datetime
sys.path.append('../')
from raid import Raid

class Database:
    """
    Database is the class with methods relative to MongoDB
    """
    def __init__(self):
        #Static constructor
        self.tokens_file = open("../creds/tokens.json", "r+")
        self.tokens = json.load(self.tokens_file)
        self.URL = self.tokens['AppURL']
        self.DB = self.tokens['DB']

    def post_raid(self, chat_id, raid):
        """
        Post or Update a raid on database.
        :param self: self database objects with local variables.
        :param chat_id: Chat/group ID;
        :param raid: raid object with the new data.
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['raids']
        obj = raid.__dict__
        obj['chat'] = chat_id
        target = {'chat': chat_id, 'id': obj['id']}
        db_target = db.find_one(target)
        if db_target == None:
            obj['insertedAt'] = datetime.utcnow()
            db.insert_one(obj)
        else:
            obj['insertedAt'] = db_target['insertedAt']
            db.replace_one(target, obj)

    def get_raids(self):
        """
        Get all raids from database.
        :param self: self database objects with local variables.
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['raids']
        collections = db.find()
        copy = collections.clone()
        raid_collections = {}
        if collections != None:
            for raid in collections:
                raid_collections[raid['chat']] = {}
            for raid in copy:
                raid_collections[raid['chat']][raid['id']] = Raid(raid['id'], raid['level'], raid['boss'], raid['time'], raid['gym'], raid['local'], raid['list'], raid['mentions'])       
        return raid_collections


    def post_welcome(self, chat_id, text):
        """
        Post or Update a welcome on database.
        :param self: self database objects with local variables.
        :param chat_id: Chat/group ID;
        :param text: the new welcome text.
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['welcomes']
        new = {"_id": chat_id, "text": text}
        doc = db.find_one({'_id': chat_id})
        if doc == None:
            db.insert_one(new)
        else:
            db.replace_one({'_id': chat_id}, {'text': text})
        client.close()

    def get_welcomes(self):
        """
        Get all welcomes from database.
        :param self: self database objects with local variables.
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['welcomes']
        objs = {'welcomes': []}
        for obj in db.find():
            objs['welcomes'].append(obj)
        client.close()
        with open("src/mongoclient/welcomes.json", "r+") as file:
            file.truncate()
            file.seek(0)
            json.dump(objs, file, indent=3)
            file.close()
        return objs

    def remove_welcome_from_db(self, chat_id):
        """
        Remove a welcome from database.
        :param self: self database objects with local variables.
        :param chat_id: Chat/group ID;
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['welcomes']
        db.delete_one({'_id': chat_id})
        client.close()

    def post_log(self, chat_id, log):
        """
        Post a log on database.
        :param self: self database objects with local variables.
        :param chat_id: Chat/group ID;
        :param log: log text.
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['logs']
        chat_logs = db.find_one({'_id': chat_id})
        if chat_logs == None:
            chat_logs = {'_id': chat_id, 'logs': []}
            chat_logs['logs'].append(log)
            db.insert_one(chat_logs)
        else:
            chat_logs['logs'].append(log)
            db.update_one({'_id': chat_id}, {'$set': {'logs': chat_logs['logs']}})
        client.close()
        self.get_logs()

    def get_logs(self):
        """
        Get all logs from database.
        :param self: self database objects with local variables.
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['logs']
        logs = {'chats': []}
        for chat in db.find():
            logs['chats'].append(chat)
        client.close()
        with open("src/mongoclient/logs.json", "r+") as file:
            file.truncate()
            file.seek(0)
            json.dump(logs, file, indent=3)
            file.close()

    def post_rules(self, chat_id, rules):
        """
        Post new rules of a chat on database.
        :param self: self database objects with local variables.
        :param chat_id: Chat/group ID;
        :param rules: rules text.
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['rules']
        chat_rules = db.find_one({'_id': chat_id})
        if chat_rules == None:
            chat_rules = {'_id': chat_id, 'rules': rules}
            db.insert_one(chat_rules)
        else:
            db.update_one({'_id': chat_id}, {'$set': {'rules': rules}})
        client.close()

    def get_rules(self):
        """
        Get all rules from database.
        :param self: self database objects with local variables.
        :param chat_id: Chat/group ID;
        :param rules: rules text.
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['rules']
        rules = {'rules': []}
        for rule in db.find():
            rules['rules'].append(rule)
        client.close()
        with open("src/mongoclient/rules.json", "r+") as file:
            file.truncate()
            file.seek(0)
            json.dump(rules, file, indent=3)
            file.close()
        return rules

    def remove_rules_from_db(self, id):
        """
        Remove rules of a chat from database.
        :param self: self database objects with local variables.
        :param chat_id: Chat/group ID;
        """
        client = MongoClient(self.URL)
        db = client[self.DB]['rules']
        db.delete_one({'_id': id})
        client.close()
        self.get_rules()

        

