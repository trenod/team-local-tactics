#from team-local-tactics import print_available_champs, input_champion, print_match_summary
from rich import print
from rich.prompt import Prompt
from rich.table import Table
import pickle

from champlistloader import load_some_champs, from_string_to_champions, load_some_champs_as_string
from core import Champion, Match, Shape, Team
#import TCP stuff
from socket import AF_INET, SOCK_STREAM, socket



#henter available champs fra serveren og sender til klienten i følgende metode:

def print_available_champs(champions: dict[Champion]) -> None:

    # Create a table containing available champions
    available_champs = Table(title='Available champions')

    # Add the columns Name, probability of rock, probability of paper and
    # probability of scissors
    available_champs.add_column("Name", style="cyan", no_wrap=True)
    available_champs.add_column("prob(:raised_fist-emoji:)", justify="center")
    available_champs.add_column("prob(:raised_hand-emoji:)", justify="center")
    available_champs.add_column("prob(:victory_hand-emoji:)", justify="center")

    # Populate the table
    for champion in champions.values():
        available_champs.add_row(*champion.str_tuple)

    print(available_champs)






#følgende metode printer match summary til player, etter å ha gjort matchen via serveren:


#def print_match_summary(match: Match) -> None:
def print_match_summary(match: Match) -> None:

    EMOJI = {
        Shape.ROCK: ':raised_fist-emoji:',
        Shape.PAPER: ':raised_hand-emoji:',
        Shape.SCISSORS: ':victory_hand-emoji:'
    }

    # For each round print a table with the results
    for index, round in enumerate(match.rounds):

        # Create a table containing the results of the round
        round_summary = Table(title=f'Round {index+1}')

        # Add columns for each team
        round_summary.add_column("Red",
                                 style="red",
                                 no_wrap=True)
        round_summary.add_column("Blue",
                                 style="blue",
                                 no_wrap=True)

        # Populate the table
        for key in round:
            red, blue = key.split(', ')
            round_summary.add_row(f'{red} {EMOJI[round[key].red]}',
                                  f'{blue} {EMOJI[round[key].blue]}')
        print(round_summary)
        print('\n')

    # Print the score
    red_score, blue_score = match.score
    print(f'Red: {red_score}\n'
          f'Blue: {blue_score}')

    # Print the winner
    if red_score > blue_score:
        print('\n[red]Red victory! :grin:')
    elif red_score < blue_score:
        print('\n[blue]Blue victory! :grin:')
    else:
        print('\nDraw :expressionless:')


    
def main() -> None:

    print('\n'
        'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
        '\n'
        'Each player choose a champion each time.'
        '\n')


    #opretter TCP socket
    sock = socket(AF_INET, SOCK_STREAM)
    #server_address = ("192.168.1.132", 5555)
    server_address = ("127.0.0.1", 5555)
    sock.connect(server_address)



    #champions_as_text = sock.recv(1024).decode()

    champions_as_text = load_some_champs_as_string()
    champions = from_string_to_champions(champions_as_text)

    """print_available_champs(champions)"""
    
    #make a choice and send champion to server over TCP:
    #while getting info and what to do
    
    response = 'Please write the name of a champion: ' 
    while response != 'done':
        print_available_champs(champions)
        champion = input(response)
        sock.send(champion.encode())
        #parse og sende som tekst
        response = sock.recv(2048).decode()
        print(response)


    print('\n')

    #receive match from server as string:
    
    pickled_match = sock.recv(1024)

    f = open('data.pickle', 'rb')
    match_object = pickle.load(f)
    f.close()

    #match = pickle.load(match_object)

    #parse string til match objekt

    #need to change print_match_summary so it receives
    #a string instead of a match object, and handles that instead

    print_match_summary(match_object)


if __name__ == '__main__':
    main()