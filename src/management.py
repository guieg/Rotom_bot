import json
from creds import my_debug, getMention_byUser
from mongoclient.database import Database

def delete_rules(update, context, bot):
    """
    Delete the chat rules.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param bot: Telegram bot object, to verify if who made the query is admin.
    """
    database = Database()
    admins = [admin.user.id for admin in bot.get_chat_administrators(update.message.chat.id)]
    is_user_admin = update.message.from_user.id in admins
    if is_user_admin:
        database.remove_rules_from_db(update.message.chat.id)
        update.message.reply_text("Feito.")
    else:
        update.message.reply_text("O uso desse comando é restrito a admins.")

def set_rules(update, context, bot):
    """
    Set the chat rules, the rules needed to be passed in the message replied (update.message.reply_to_message.text).
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param bot: Telegram bot object, to verify if who made the query is admin.
    """
    database = Database()
    admins = [admin.user.id for admin in bot.get_chat_administrators(update.message.chat.id)]
    is_user_admin = update.message.from_user.id in admins
    if is_user_admin:
        database.post_rules(update.message.chat.id, update.message.reply_to_message.text)
        update.message.reply_text("Feito.")
    else:
        update.message.reply_text("O uso desse comando é restrito a admins.")

def rules(update, context, rules):
    """
    Get and response the chat rules.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    """
    for rule in rules['rules']:
        if rule['_id'] == update.message.chat.id:
            update.message.reply_text(rule['rules'])


def set_welcome(update, context, bot):
    """
    Set the group welcome, the welcome text needed to be passed in the message replied (update.message.reply_to_message.text).
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param bot: Telegram bot object, to verify if who made the query is admin.
    """
    database = Database()
    admins = [admin.user.id for admin in bot.get_chat_administrators(update.message.chat.id)]
    is_user_admin = update.message.from_user.id in admins
    if is_user_admin:
        database.post_welcome(update.message.chat.id, update.message.reply_to_message.text)
        update.message.reply_text("Feito.")
    else:
        update.message.reply_text("O uso desse comando é restrito a admins.")

def get_welcome(update, context, bot, welcomes):
    """
    Welcome the new chat member.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param bot: Telegram bot object, to verify if who made the query is admin.
    """
    for newer in update.message.new_chat_members:
        for welcome in welcomes['welcomes']:
            if welcome['_id'] == update.message.chat.id:
                text = welcome['text'].format(getMention_byUser(newer))
                bot.send_message(chat_id=update.message.chat_id, text=text, parse_mode="Markdown")

def delete_welcome(update, context, bot):
    """
    Delete the chat welcome.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param bot: Telegram bot object, to verify if who made the query is admin.
    """
    database = Database()
    admins = [admin.user.id for admin in bot.get_chat_administrators(update.message.chat.id)]
    is_user_admin = update.message.from_user.id in admins
    if is_user_admin:
        database.remove_welcome_from_db(update.message.chat.id)
        update.message.reply_text("Feito.")
    else:
        update.message.reply_text("O uso desse comando é restrito a admins.")

def get_bot_leave(update, context, bot):
    """
    Get when the bot is removed from a chat and delete chat information.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param bot: Telegram bot object, to verify if who made the query is admin.
    """
    database = Database()
    leaver = update.message.left_chat_member
    if bot.get_me().id == leaver.id:
        database.remove_welcome_from_db(update.message.chat.id)
        database.remove_rules_from_db(update.message.chat.id)

def ban(update, context, bot):
    """
    Ban a chat member relative a message replied (update.message.reply_to_message).
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query;
    :param bot: Telegram bot object, to verify if who made the query is admin.
    """
    chat_id = update.message.chat.id
    target_id = update.message.reply_to_message.from_user.id
    target_name = update.message.reply_to_message.from_user.first_name
    admins = [admin.user.id for admin in bot.get_chat_administrators(update.message.chat.id)]
    is_target_admin = target_id in admins
    is_user_admin = update.message.from_user.id in admins
    if bot.get_me().id in admins:
        if not is_target_admin:
            if is_user_admin:
                bot.kick_chat_member(chat_id, target_id)
                update.message.reply_text("Nome: {} | ID: {} (BANIDO)".format(target_name, target_id))
                bot.send_animation(chat_id, 'https://38.media.tumblr.com/ca82188b968717aa9944939cad8caaf2/tumblr_nr89md488N1rc3jkko4_500.gif')
            else:
                update.message.reply_text("O uso desse comando é restrito a admins.")
        else:
            update.message.reply_text("Não posso banir um admin.")
            bot.send_animation(chat_id, 'https://thumbs.gfycat.com/ScaryFlickeringBrahmanbull-small.gif')
    else:
        update.message.reply_text("Não sou admin.")
        bot.send_animation(chat_id, 'https://thumbs.gfycat.com/ScaryFlickeringBrahmanbull-small.gif')