#initially use a cvs file updating, based on champlistloader.py,
#then implement mongoDB features using the cloud solution

from core import Champion


def _parse_champ(champ_text: str) -> Champion:
    name, rock, paper, scissors = champ_text.split(sep=',')
    return Champion(name, float(rock), float(paper), float(scissors))


def from_csv(filename: str) -> dict[str, Champion]:
    champions = {}
    with open(filename, 'r') as f:
        for line in f.readlines():
            champ = _parse_champ(line)
            champions[champ.name] = champ

    return champions

def to_csv(filename: str, Champion, win):
    old_stats = load_stats()
    with open(filename, 'w') as f:
        for line in f.readlines():
            f.append(_parse_champ(line))
            champions[champ.name] = champ
    return champions


def load_stats():
    return from_csv('stats.txt')