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


def load_some_champs():
    return from_csv('some_champs.txt')

def from_string_to_champions(champ_string: str) -> dict[str, Champion]:
    champions = {}
    champlist = champ_string.split(sep=' ')
    for line in champlist:
        champ = _parse_champ(line)
        champions[champ.name] = champ
    return champions



def from_csv_to_string(filename: str) -> str:
    champions = ''
    with open(filename, 'r') as f:
        for line in f.readlines():
            champ = line
            champions += champ
            champions += ' '

    return champions

def load_some_champs_as_string():
    return from_csv_to_string('some_champs.txt')
