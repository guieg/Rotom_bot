import logging
import os

from uuid import uuid4
from telegram import User, InlineQueryResultArticle, ParseMode, \
    InputTextMessageContent, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, InlineQueryHandler, CallbackQueryHandler, CommandHandler, MessageHandler, CallbackQueryHandler, Filters
from telegram.ext.dispatcher import run_async
from telegram.utils.helpers import escape_markdown

from mongoclient.database import Database

from rotom import RotomBot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title="Caps",
            input_message_content=InputTextMessageContent(
                query.upper())),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Bold",
            input_message_content=InputTextMessageContent(
                "*{}*".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN)),
        InlineQueryResultArticle(
            id=uuid4(),
            title="Italic",
            input_message_content=InputTextMessageContent(
                "_{}_".format(escape_markdown(query)),
                parse_mode=ParseMode.MARKDOWN))]

    update.inline_query.answer(results)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

if __name__ == '__main__':
    """
    Main code: 
        -Get data from MongoDB;
        -Start the bot;
        -Add handlers;
    """

    #Geting data
    database = Database()

    #Starting the bot
    print('Starting...')
    Rotom = RotomBot(database)
    updater = Updater(Rotom.botToken, use_context=True)
    dp = updater.dispatcher
    print('The bot is up! Press Ctrl-C to stop.')
    #adding handlers
    # Informations
    dp.add_handler(CommandHandler("help", Rotom._help, pass_user_data=True))
    dp.add_handler(CommandHandler("info", Rotom._info, pass_user_data=True))
    dp.add_handler(CommandHandler("regras", Rotom._rules, pass_user_data=True))

    # Management
    dp.add_handler(CommandHandler("setwelcome", Rotom._set_welcome))
    dp.add_handler(CommandHandler("delwelcome", Rotom._delete_welcome))
    dp.add_handler(CommandHandler("setrules", Rotom._set_rules))
    dp.add_handler(CommandHandler("delrules", Rotom._delete_rules))
    dp.add_handler(CommandHandler("ban", Rotom._ban, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.status_update.new_chat_members, Rotom._get_welcome))
    dp.add_handler(MessageHandler(Filters.status_update, Rotom._get_bot_leave))

    # Raids
    dp.add_handler(CommandHandler("raid", Rotom._raid, pass_args=True))
    dp.add_handler(CommandHandler("mudarLevel", Rotom._raid_level, pass_args=True))
    dp.add_handler(CommandHandler("mudarChefe", Rotom._raid_boss, pass_args=True))
    dp.add_handler(CommandHandler("mudarHora", Rotom._raid_time, pass_args=True))
    dp.add_handler(CommandHandler("mudarGym", Rotom._raid_gym, pass_args=True))
    dp.add_handler(CommandHandler("mudarLocal", Rotom._raid_location, pass_args=True))
    dp.add_handler(CommandHandler("entrar", Rotom._get_in, pass_args=True))
    dp.add_handler(CommandHandler("sair", Rotom._get_out, pass_args=True))
    dp.add_handler(CommandHandler("notificar", Rotom._notify, pass_args=True))
    dp.add_handler(CommandHandler("colocar", Rotom._put, pass_args=True))
    dp.add_handler(CommandHandler("retirar", Rotom._remove, pass_args=True))
    dp.add_handler(CommandHandler("mostrar", Rotom._show, pass_args=True))
    dp.add_handler(CallbackQueryHandler(Rotom._raid_button_pressed))
    # Counter
    dp.add_handler(CommandHandler("counter", Rotom._counter_ga, pass_args=True))
    dp.add_handler(CommandHandler("counter2", Rotom._counter_simple, pass_args=True))

    # Others
    dp.add_handler(CommandHandler("start", Rotom._start))


    dp.add_handler(CommandHandler("os", Rotom.osi, pass_args=True))
    dp.add_handler(CommandHandler("allow", Rotom.allow, pass_args=True))
    dp.add_handler(CommandHandler("deallow", Rotom.deallow, pass_args=True))
    dp.add_handler(CommandHandler("getuser", Rotom.get_user, pass_args=True))
    dp.add_handler(InlineQueryHandler(inlinequery))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling(clean=True)
    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

