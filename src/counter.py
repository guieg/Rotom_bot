from counter_search.genetic_algorithm import search_counters
from counter_search.simple_algorithm import simple_counters

def counter_ga(update, context):
    """
    Create a counter team using genetic algorithm.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query.
    """
    message = update.message.reply_text("Pesquisando...")
    team = []
    if len(context.args)<=6:
        try:
            for arg in context.args:
                team.append(arg.capitalize())
            result = search_counters(team)
            saida = ""
            for i in range(len(result[0])):
                saida+=result[0][i]+" ("+result[1][i]+" move set) \n"
            saida+=str(result[2])
            message.edit_text(saida)
        except:
            message.edit_text("Algum desses nomes não foi encontrado.")
    else:
        message.edit_text("Limite de time ultrapassado.")

def counter_simple(update, context):
    """
    Get the best counters against a pokémon ou a team.
    :param update: update object that contains all information about the query;
    :param context: context object that contains all arguments from the query.
    """
    message = update.message.reply_text("Pesquisando...")
    team = []
    if len(context.args)<=6:
        try:
            for arg in context.args:
                team.append(arg.capitalize())
            result = simple_counters(team)
            saida = ""
            for i in range(len(result[0])):
                saida+=result[0][i]+" ("+result[1][i]+" move set) \n"
            message.edit_text(saida)
        except:
           message.edit_text("Algum desses nomes não foi encontrado.")
    else:
        message.edit_text("Limite de time ultrapassado.")
