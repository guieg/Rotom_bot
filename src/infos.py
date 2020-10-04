from creds import my_debug
from texts import startText, infoText, helpText, helpTexts

def start(update, context):
    """
    Response with the start text (startText) from texts.py
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query.
    """
    update.message.reply_text(startText)

def info(update, context):
    """
    Response with the info text (infoText) from texts.py
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query.
    """
    update.message.reply_text(infoText)

def help(update, context):
    """
    Response the help text (helpText) from texts.py if no arguments were passed.
    Or else response a the specifc text of a command in the first argument.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query.
    """
    if len(context.args)==0:
        update.message.reply_text(helpText)
    else:
        try:
            update.message.reply_text(helpTexts[context.args[0]])
        except:
            pass

        