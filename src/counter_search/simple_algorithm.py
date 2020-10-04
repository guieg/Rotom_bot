from pandas import read_csv, Index
from .dataset import PokemonsData
from .utils import get_true_pokename, lstr_to_lint, best_typeset_against

def get_CP(row):
    return row[2]

def simple_search(team, db, size):
    weakness = []
    counters = []
    team_counter = []
    for pokemon in team:
        weakness = []
        counters = []
        weaks = db.loc[Index(db.pokedex_number).get_loc(pokemon)][9:]
        for i in range(len(weaks)):
            if weaks[i] == weaks.max():
                weakness.append(db.columns[9+i].replace("against_", ""))
        for pokenumber in db.pokedex_number:
            if (db.loc[Index(db.pokedex_number).get_loc(pokenumber), "type1"] in weakness) or (db.loc[Index(db.pokedex_number).get_loc(pokenumber), "type2"] in weakness):
                counters.append(list(db.loc[Index(db.pokedex_number).get_loc(pokenumber)]))
        counters.sort(reverse=True, key=get_CP)
        if size == 1:
            for k in counters[:12]:
                team_counter.append(float(k[0]))
        else:
            team_counter.append(float(counters[0][0]))
    return team_counter



def simple_counters(team, return_names=True):
    """
    "team" - param1 : the team to be countered
    return_names - param2: if true return the counter team by the names, else return counter team by pokedex number

    application of ga to counter a "team"  and return a tuple:
    tuple[0] -> counter team of "team"
    tuple[1] -> best type for move sets of counter[k] against "team"[k]
    tuple[2] -> fitness, how good is the counter team against "team"
    """
    df = PokemonsData().get_df()
    team_target = lstr_to_lint(team.copy(), df)
    size = len(team_target)

    best_team = simple_search(team_target, df, size)
    best_move_sets = []
    for i in range(len(best_team)):
        if size > 1:
            best_move_sets.append(best_typeset_against(best_team[i], team_target[i], df))
        else:
            best_move_sets.append(best_typeset_against(best_team[i], team_target[0], df))
        if return_names:
            best_team[i] = get_true_pokename(best_team[i], df)
    return best_team, best_move_sets
