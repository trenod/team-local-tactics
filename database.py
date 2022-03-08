#initially use a cvs file updating, based on champlistloader.py,
#then implement mongoDB features using the cloud solution

from core import Champion, ChampionStats
import os
import json


def _parse_champ(champ_text: str) -> json:
    name, wins, losses = champ_text.split(sep=',')
    return json(name, int(wins), int(losses))


def from_csv(filename: str) -> json:
    championsstats = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            champ = _parse_champ(line)
            championsstats[champ.name] = champ

    return championsstats

def to_csv(filename: str, Champion, win):
    old_stats = load_stats()
    champ = Champion
    os.remove('stats.txt')
    with open(filename, 'a') as f:
        for stat in old_stats:
            if (stat[champ.name] == champ.name):
                if (win):
                    stat[champ.win] = stat[champ.wins + 1]
                else:
                    stat[champ.win] = stat[champ.losses + 1]
            f.append(stat[champ.name] + "," + stat[champ.wins] + "," + stat[champ.losses])
            
    


def load_stats():
    return from_csv('stats.txt')