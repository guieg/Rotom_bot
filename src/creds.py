from mongoclient.database import Database
import asyncio

async def my_debug(update):
    """
    Save every query that Rotom receive.
    :param update: update object that contains all information about the query;
    """
    database = Database()
    try:
        user = str(update.message.from_user.first_name)+" "+str(update.message.from_user.last_name)
        id = str(update.message.from_user.id)
        command = str(update.message.text)
        log = "\nuser: {} | id: {} | comando: {} (Rotom)".format(user, id, command)
        database.post_log(update.message.chat.id, log)
        print(log)
    except:
        user = str(update.callback_query.from_user.first_name)+" "+str(update.callback_query.from_user.last_name)
        id = str(update.callback_query.from_user.id)
        log = "\nuser: {} | id: {} | entrou/saiu\n (Rotom)".format(user, id)
        database.post_log(update.callback_query.message.chat.id, log)
        print(log)

def getMention(update):
    """
    Create a mention for a chat member from his message.
    :param update: update object that contains all information about the query;
    """
    #mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    name = str(update.message.from_user.first_name)
    name = name.replace(" ", "_")
    print(name)
    return "["+name+"](tg://user?id="+str(update.message.from_user.id)+")"

def getMention_callback_query(update):
    """
    Create a mention for a chat member from his callback query.
    :param update: update object that contains all information about the query;
    """
    #mention = "["+user_name+"](tg://user?id="+str(user_id)+")"
    name = str(update.callback_query.from_user.first_name)
    name = name.replace(" ", "_")
    print(name)
    return "["+name+"](tg://user?id="+str(update.callback_query.from_user.id)+")"

def getMention_byUser(user):
    return "["+user.first_name+"](tg://user?id="+str(user.id)+")"

