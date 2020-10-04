import re
from raid import Raid
from mongoclient.database import Database
from creds import *
from telegram import User, InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup

def update_raid(chat_id, raid):
    """
    Update a raid on database.
    :param chat_id: group/chat ID;
    :param raid: raid object with the updated information.
    """
    database = Database()
    database.post_raid(chat_id, raid)

def set_raid_parameters(args):
    """
    Return a list with the raid arguments.
    :param args: given arguments.
    """
    params = []
    for index in range(5):
        try:
            params.append(args[index].replace("_", " "))
        except:
            params.append("?"*(index+1))
    return params 

def raid(update, context, raid_collections):
    """
    Create a raid object and insert it in the raid_collections.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    
    if not update.message.chat.id in raid_collections:
        raid_collections[update.message.chat.id] = {}
    raids = raid_collections[update.message.chat.id]

    RAID_ID = len(raids) + 1
    while str(RAID_ID) in raids:
        RAID_ID+=1

    params = set_raid_parameters(context.args)
    level = params[0]
    boss = params[1]
    time = params[2]
    gym = params[3]
    local = params[4]

    raids[str(RAID_ID)] = Raid(str(RAID_ID), level, boss, time, gym, local, [], [])
    update.message.reply_text(raids[str(RAID_ID)].get_text(), reply_markup=button_raid(raids[str(RAID_ID)].get_id()), parse_mode="Markdown")
    update_raid(update.message.chat.id, raids[str(RAID_ID)])
    return raid_collections

def button_raid(raid_id):
    """
    Button to get_in or get_out of a raid
    :param raid_id: raid ID.
    """
    bt = [[InlineKeyboardButton(text="Entrar/Sair", callback_data=raid_id)]]
    return InlineKeyboardMarkup(bt)


def get_in_byButton(update, raid_list, mentions):
    """
    Insert a chat member in a raid list when the button is pressed by him.
    :param update: update object that contains all information about the query;
    :param raid_list: list of chat members in a raid;
    :param mentions: list of mentions in a raid.
    """
    raid_list.append(update.callback_query.from_user.first_name)
    mentions.append(getMention_callback_query(update))
    return raid_list, mentions

def get_out_byButton(update, raid_list, mentions):
    """
    Remove a chat member in a raid list when the button is pressed by him.
    :param update: update object that contains all information about the query;
    :param raid_list: list of chat members in a raid;
    :param mentions: list of mentions in a raid.
    """
    raid_list.remove(update.callback_query.from_user.first_name)
    mentions.remove(getMention_callback_query(update))
    return raid_list, mentions

def raid_button_pressed(update, context, raid_collections):
    """
    Insert or remove a chat member in a raid list when the button is pressed by him.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.callback_query.message.chat.id]
    raid_id = update.callback_query.data
    mentions = raids[raid_id].get_mentions()
    raid_list = raids[raid_id].get_list()

    if not getMention_callback_query(update) in mentions:
        raid_list, mentions = get_in_byButton(update, raid_list, mentions)
    else:
        raid_list, mentions = get_out_byButton(update, raid_list, mentions)

    raids[raid_id].set_list(raid_list)
    raids[raid_id].set_mentions(mentions)
    update.callback_query.message.reply_text(raids[raid_id].get_text(), reply_markup=button_raid(raid_id), parse_mode="Markdown")
    update_raid(update.callback_query.message.chat.id, raids[raid_id])
    return  raid_collections

def raid_level(update, context, raid_collections):
    """
    Changes the level of a specific raid.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    level = ""
    for arg in context.args[1:]:
        level+= arg+" "
    raids[context.args[0]].set_level(level)
    update.message.reply_text(raids[context.args[0]].get_text(), reply_markup=button_raid(context.args[0]), parse_mode="Markdown")
    update_raid(update.message.chat.id, raids[context.args[0]])
    return raid_collections

def raid_boss(update, context, raid_collections):
    """
    Changes the boss of a specific raid.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    boss = ""
    for arg in context.args[1:]:
        boss+= arg+" "
    raids[context.args[0]].set_boss(boss)
    update.message.reply_text(raids[context.args[0]].get_text(), reply_markup=button_raid(context.args[0]), parse_mode="Markdown")
    update_raid(update.message.chat.id, raids[context.args[0]])
    return raid_collections

def raid_time(update, context, raid_collections):
    """
    # Changes the time of a specific raid.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    time = ""
    for arg in context.args[1:]:
        time+= arg+" "
    raids[context.args[0]].set_time(time)
    update.message.reply_text(raids[context.args[0]].get_text(), reply_markup=button_raid(context.args[0]), parse_mode="Markdown")
    update_raid(update.message.chat.id, raids[context.args[0]])
    return raid_collections

def raid_gym(update, context, raid_collections):
    """
    Changes the gym of a specific raid.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    gym = ""
    for arg in context.args[1:]:
        gym+= arg+" "
    raids[context.args[0]].set_gym(gym)
    update.message.reply_text(raids[context.args[0]].get_text(), reply_markup=button_raid(context.args[0]), parse_mode="Markdown")
    update_raid(update.message.chat.id, raids[context.args[0]])    
    return raid_collections

def raid_location(update, context, raid_collections):
    """
    Changes the location of a specific raid.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    local = ""
    for arg in context.args[1:]:
        local+= arg+" "
    raids[context.args[0]].set_local(local)
    update.message.reply_text(raids[context.args[0]].get_text(), reply_markup=button_raid(context.args[0]), parse_mode="Markdown")
    update_raid(update.message.chat.id, raids[context.args[0]])    
    return raid_collections

def notify(update, context, raid_collections):
    """
    Notify everyone in a raid list.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    saida = ""
    counter = 0

    for membro in raids[context.args[0]].get_mentions():
        saida += " {}".format(str(membro))
        counter+=1
        if counter >= 7:
            update.message.reply_text(saida, parse_mode="Markdown")
            saida = ""
            counter = 0

    if saida != "":
        update.message.reply_text(saida, parse_mode="Markdown")

def get_in(update, context, raid_collections):
    """
    Insert a chat member in a raid list. 
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    raid_id = context.args[0]
    mentions = raids[raid_id].get_mentions()
    raid_list = raids[raid_id].get_list()
    mention = getMention(update)
    try:
        if not context.args[1] in raid_list:
            raid_list.append(context.args[1])
            new_mention = "["+context.args[1].replace(" ", "_")+"](tg://user?id="+str(update.message.from_user.id)+")"
            mentions.append(new_mention)
            raids[raid_id].set_list(raid_list)
            raids[raid_id].set_mentions(mentions)
            update.message.reply_text(raids[raid_id].get_text(), reply_markup=button_raid(raid_id), parse_mode="Markdown")
    except:
        if not mention in mentions:
            raid_list.append(update.message.from_user.first_name)
            mentions.append(mention)
            raids[raid_id].set_list(raid_list)
            raids[raid_id].set_mentions(mentions)
            update.message.reply_text(raids[raid_id].get_text(), reply_markup=button_raid(raid_id), parse_mode="Markdown")
    update_raid(update.message.chat.id, raids[raid_id])
    return raid_collections

def get_out(update, context, raid_collections):
    """
    Remove a chat member from a raid list. 
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    raid_id = context.args[0]
    mentions = raids[raid_id].get_mentions()
    raid_list = raids[raid_id].get_list()
    mention = getMention(update)
    raid_list.remove(update.message.from_user.first_name)
    mentions.remove(mention)
    raids[raid_id].set_list(raid_list)
    raids[raid_id].set_mentions(mentions)
    update.message.reply_text(raids[context.args[0]].get_text(), reply_markup=button_raid(raid_id), parse_mode="Markdown")
    update_raid(update.message.chat.id, raids[raid_id])
    return raid_collections

def put(update, context, raid_collections):
    """
    Insert another chat member in a raid list. 
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    raid_id = context.args[1]
    mentions = raids[raid_id].get_mentions()
    raid_list = raids[raid_id].get_list()
    mention = "["+context.args[0].replace(" ", "_")+"](tg://user?id="+str(update.message.from_user.id)+")"
    if not context.args[0] in raid_list:
        raid_list.append(context.args[0])
        mentions.append(mention)
        raids[raid_id].set_list(raid_list)
        raids[raid_id].set_mentions(mentions)
        update.message.reply_text(raids[raid_id].get_text(), reply_markup=button_raid(raid_id), parse_mode="Markdown")
        update_raid(update.message.chat.id, raids[raid_id])
    return raid_collections

def show(update, context, raid_collections):
    """
    Show the raid list. 
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    try:
        update.message.reply_text(raids[context.args[0]].get_text(), reply_markup=button_raid(context.args[0]), parse_mode="Markdown")
    except:
        text = ""
        for id_key in raids:
            text += "ℹ️ ID " + id_key + "; Chefe: " + raids[id_key].boss + '\n'
        update.message.reply_text(text)

def remove(update, context, raid_collections):
    """
    Remove another chat member from a raid list. 
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param raid_collections: dict (where each key is a chat id) of 
    dicts (where each key is a raid id) contaning all raids of all chats.
    """
    raids = raid_collections[update.message.chat.id]
    raid_id = context.args[1]
    mentions = raids[raid_id].get_mentions()
    raid_list = raids[raid_id].get_list()
    index = int(context.args[0])
    if index <= len(raid_list) and index > 0:
        raid_list.pop(index-1)
        mentions.pop(index-1)
        raids[raid_id].set_list(raid_list)
        raids[raid_id].set_mentions(mentions)
        update.message.reply_text(raids[raid_id].get_text(), reply_markup=button_raid(raid_id), parse_mode="Markdown")
        update_raid(update.message.chat.id, raids[raid_id])
    return raid_collections