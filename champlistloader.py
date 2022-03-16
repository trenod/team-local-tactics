from core import Champion, Match


def _parse_champ(champ_text: str) -> Champion:
    name, rock, paper, scissors = champ_text.split(sep=',')
    #champ_text_list = champ_text.split(",")
    #name = champ_text_list[0]
    #rock = champ_text_list[1]
    #paper = champ_text_list[2]
    #scissors = champ_text_list[3]
    #name, rock, paper, scissors = champ_text.split(",")
    #right here there is a strange bug that prevents the program from
    #finishing running. i have tried many things and asked TA's, but 
    #no solution has been found.
    print(champ_text)
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

def from_match_to_string(match: Match) -> str:
    match_as_string = ''
    return match_as_string

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
