import json
import os
import asyncio
from mongoclient.database import Database
from telegram import Bot
from telegram.ext.dispatcher import run_async
from counter import counter_ga, counter_simple
from creds import my_debug
from raids import *
from infos import *
from management import *

class RotomBot:
    """
    Class for Rotom, contains all data, tokens and methods that are directly used
    by Rotom.
    """
    def __init__(self, database):
        """
        :param self: self object, python default;
        :param database: object that contains all database data and methods.
        """
        #Autentication
        self.tokens_file = open("creds/tokens.json", "r+")
        self.tokens = json.load(self.tokens_file)
        self.botToken = self.tokens['Rotom']
        self.OP = self.tokens['OP']
        self.bot = Bot(self.botToken)
        #Initializing data
        self.database = database
        self.raid_collections = self.database.get_raids()
        self.welcomes = self.database.get_welcomes()
        self.rules = self.database.get_rules()
        self.allowed = set()

    """
    The following methods are routing methods, they start the real methods
    asynchronously and they pass all data relative to the debug method    
    """
    @run_async
    def _help(self, update, context):
        """help method is in info.py"""
        asyncio.run(my_debug(update))
        help(update, context)
    
    @run_async
    def _info(self, update, context):
        """info method is in info.py"""
        asyncio.run(my_debug(update))
        info(update, context)

    @run_async
    def _set_rules(self, update, context):
        """set_rules method is in management.py"""
        asyncio.run(my_debug(update))
        set_rules(update, context, self.bot)
        self.rules = self.database.get_rules()

    @run_async
    def _delete_rules(self, update, context):
        """delete_rules method is in management.py"""
        asyncio.run(my_debug(update))
        delete_rules(update, context, self.bot)
        self.rules = self.database.get_rules()

    @run_async
    def _rules(self, update, context):
        """rules method is in management.py"""
        asyncio.run(my_debug(update))
        rules(update, context, self.rules)

    @run_async
    def _set_welcome(self, update, context):
        """set_welcome method is in management.py"""
        asyncio.run(my_debug(update))
        set_welcome(update, context, self.bot)
        self.welcomes = self.database.get_welcomes()

    @run_async
    def _delete_welcome(self, update, context):
        """delete_welcome method is in management.py"""
        asyncio.run(my_debug(update))
        delete_welcome(update, context, self.bot)
        self.welcomes = self.database.get_welcomes()

    @run_async
    def _ban(self, update, context):
        """ban method is in management.py"""
        asyncio.run(my_debug(update))
        ban(update, context, self.bot)
    
    @run_async
    def _get_welcome(self, update, context):
        """get_welcome method is in management.py"""
        get_welcome(update, context, self.bot, self.welcomes)

    @run_async
    def _get_bot_leave(self, update, context):
        """get_bot_leave method is in management.py"""
        get_bot_leave(update, context, self.bot)
    
    @run_async
    def _raid(self, update, context):
        """raid method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = raid(update, context, self.raid_collections)

    @run_async
    def _raid_level(self, update, context):
        """raid_level method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = raid_level(update, context, self.raid_collections)

    @run_async
    def _raid_boss(self, update, context):
        """raid_boss method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = raid_boss(update, context, self.raid_collections)

    @run_async
    def _raid_time(self, update, context):
        """raid_time method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = raid_time(update, context,  self.raid_collections)

    @run_async
    def _raid_gym(self, update, context):
        """raid_gym method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = raid_gym(update, context, self.raid_collections)

    @run_async
    def _raid_location(self, update, context):
        """raid_location method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = raid_location(update, context, self.raid_collections)

    @run_async
    def _get_in(self, update, context):
        """get_in method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = get_in(update, context, self.raid_collections)
    @run_async
    def _get_out(self, update, context):
        """get_out method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = get_out(update, context, self.raid_collections)

    @run_async
    def _notify(self, update, context):
        """notify method is in raids.py"""
        asyncio.run(my_debug(update))
        notify(update, context, self.raid_collections)

    @run_async
    def _put(self, update, context):
        """put method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = put(update, context, self.raid_collections)

    @run_async
    def _remove(self, update, context):
        """remove method is in raids.py"""
        asyncio.run(my_debug(update))
        self.raid_collections = remove(update, context, self.raid_collections)

    @run_async
    def _show(self, update, context):
        """show method is in raids.py"""
        asyncio.run(my_debug(update))
        show(update, context, self.raid_collections)

    @run_async
    def _raid_button_pressed(self, update, context):
        """get_in_byButton method is in raids.py"""
        asyncio.run(my_debug(update))
        raid_button_pressed(update, context, self.raid_collections)

    @run_async
    def _counter_ga(self, update, context):
        """counter_ga method is in counter.py"""
        asyncio.run(my_debug(update))
        counter_ga(update, context)

    @run_async
    def _counter_simple(self, update, context):
        """counter_simple method is in counter.py"""
        asyncio.run(my_debug(update))
        counter_simple(update, context)

    @run_async
    def _start(self, update, context):
        """start method is in info.py"""
        asyncio.run(my_debug(update))
        start(update, context)

    #The following methods are develop support methods
    @run_async
    def allow(self, update, context):
        asyncio.run(my_debug(update))
        if str(update.message.from_user.id)==self.OP:
            self.allowed.add(context.args[0])
        else:
            update.message.reply_text("NOPE")

    @run_async
    def deallow(self, update, context):
        asyncio.run(my_debug(update))
        if str(update.message.from_user.id)==self.OP:
            self.allowed.remove(context.args[0])
        else:
            update.message.reply_text("NOPE")

    @run_async
    def osi(self, update, context):
        asyncio.run(my_debug(update))
        if str(update.message.from_user.id)==self.OP:
            entrada = ""
            for arg in context.args:
                entrada += arg+" "
            os.system(entrada+" > saida")
            log = open("saida", "r+")
            update.message.reply_text(log.read())
            log.close()
        else:
            update.message.reply_text("NOPE")

    @run_async
    def get_user(self, update, context):
        asyncio.run(my_debug(update))
        if str(update.message.from_user.id)==self.OP:
            update.message.reply_text("[target](tg://user?id="+str(context.args[0])+")", parse_mode="Markdown")
        else:
            update.message.reply_text("NOPE")
        