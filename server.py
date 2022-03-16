from rich import print
from rich.prompt import Prompt
from rich.table import Table

from champlistloader import load_some_champs, load_some_champs_as_string
from core import Champion, Match, Shape, Team
from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR
from database import to_csv, from_csv_to_string



def input_champion(prompt: str,
                color: str,
                champions: dict[Champion],
                player1: list[str],
                player2: list[str], conn) -> None:

    # Prompt the player to choose a champion and provide the reason why
    # certain champion cannot be selected
    while True:
        #champion1 = conn.recv(1024).decode()
        #match Prompt.ask(f'[{color}]{prompt}'):
        name = conn.recv(1024).decode()
        match name:
            case name if name not in champions:
                conn.send('The champion {name} is not available. Try again.'.encode())
            case name if name in player1:
                conn.send('{name} is already in your team. Try again.'.encode())
            case name if name in player2:
                conn.send('{name} is in the enemy team. Try again.'.encode())
            case _:
                player1.append(name)

                if (player1.__sizeof__ == 2):
                    conn.send('done'.encode())
                    
                break


def save_stats(match: Match) -> None:
    red_score, blue_score = match.score
    if (red_score > blue_score):
        winner = 'player1'
        loser = 'player2'
    else:
        winner = 'player2'
        loser = 'player1'
    to_csv('stats.txt', winner, True)
    to_csv('stats.txt', loser, False)

def get_stats_as_string(filename: str) -> str:
    playerstats = from_csv_to_string(filename)
    return playerstats


def from_match_to_string(match: Match) -> str:
    match_as_string = ''
    index = 1
    for round in enumerate(match.rounds):
        for key in round:
            red, blue = key.split(', ')
            match_as_string += round[key].red
            match_as_string += ','
            match_as_string += round[key].blue
            match_as_string += 'round'
            index += 1
    
    match_as_string += ','
    match_as_string += index
    match_as_string += ' SENTINEL1 '
    match_as_string += ' '
    red_score, blue_score = match.score
    match_as_string += red_score
    match_as_string += ','
    match_as_string += blue_score
    match_as_string += ' SENTINEL2 '

    return match_as_string


def main() -> None:

    #opretter TCP socket
    sock = socket(AF_INET, SOCK_STREAM)
    # Reuse an address
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(("localhost", 5555))
    sock.listen()

    done = False

    print('Listening for clients to connect...')

    while (done == False):
        conn1, player1_address = sock.accept()
        conn2, player2_address = sock.accept()
        if (conn1 and conn2):
            print('Both clients connected!')
            done = True
    

    print('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')

    champions = load_some_champs_as_string()

    conn1.send(champions.encode())
    conn2.send(champions.encode())

    stats = get_stats_as_string(stats.txt)

    player1 = []
    player2 = []


    # Champion selection
    for _ in range(2):
        input_champion('Player 1', 'red', champions, player1, player2, conn1)
        input_champion('Player 2', 'blue', champions, player2, player1, conn2)

    print('\n')

    # Match
    match = Match(
        Team([champions[name] for name in player1]),
        Team([champions[name] for name in player2])
    )
    match.play()

    save_stats(match)

    match_as_string = from_match_to_string(match)
    
    conn1.send(match_as_string.encode())
    conn2.send(match_as_string.encode())


    conn1.close()
    conn2.close()


if __name__ == '__main__':
    main()
