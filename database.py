#initially use a cvs file updating, based on champlistloader.py,
#then implement mongoDB features using the cloud solution

from core import Champion


def _parse_champ(champ_text: str) -> ChampionStats:
    name, rock, paper, scissors, wins, losses = champ_text.split(sep=',')
    return ChampionStats(name, float(rock), float(paper), float(scissors), int(wins), int(losses))


def from_csv(filename: str) -> dict[ChampionStats]:
    championsstat = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            champstat = _parse_champ(line)
            championsstats[champstat.name] = champstat

    return championsstats

def to_csv(filename: str, Champion, win):
    old_stats = load_stats()
    champ = Champion
    with open(filename, 'a') as f:
        for stat in old_stats:
            if (stat[champ.name] == champ.name):
                if (win):
                    stat[champ.win] = stat[champ.wins + 1]
                else:
                    stat[champ.win] = stat[champ.losses + 1]
            
            f.append(_parse_champ(stat))
            
    


def load_stats():
    return from_csv('stats.txt')