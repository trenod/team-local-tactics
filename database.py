#initially use a cvs file updating, based on champlistloader.py,
#then implement mongoDB features using the cloud solution

from core import Champion


def _parse_champ(champ_text: str) -> ChampionStats:
    name, rock, paper, scissors, wins, losses = champ_text.split(sep=',')
    return ChampionStats(name, float(rock), float(paper), float(scissors), int(wins), int(losses))


def from_csv(filename: str) -> dict[str, Champion]:
    champions = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            champstat = _parse_champ(line)
            championsstats[champ.name] = champstat

    return championsstats

def to_csv(filename: str, ChampionStats, win):
    old_stats = load_stats()
    with open(filename, 'w') as f:
        for stat in ChampionStats:
            champions[champ.name] = champ
            f.append(_parse_champ(stat))
            
    


def load_stats():
    return from_csv('stats.txt')