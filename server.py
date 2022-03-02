from rich import print
from rich.prompt import Prompt
from rich.table import Table

from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team
from socket import AF_INET, SOCK_STREAM, socket


#import TCP stuff




#class for player with data on each player that updates with both clients:

#class player 


#følgende metode kommuniserer med serveren og sjekker med den om champion er tilgjengelig,
#serveren sjekker det opp mot hva som er registrert fra før (i cvs fil/database)


def input_champion(prompt: str,
                color: str,
                champions: dict[Champion],
                player1: list[str],
                player2: list[str]) -> None:

    # Prompt the player to choose a champion and provide the reason why
    # certain champion cannot be selected
    while True:
        match Prompt.ask(f'[{color}]{prompt}'):
            case name if name not in champions:
                #need to check with the server here to see if champion is available
                print(f'The champion {name} is not available. Try again.')
            case name if name in player1:
                print(f'{name} is already in your team. Try again.')
            case name if name in player2:
                print(f'{name} is in the enemy team. Try again.')
            case _:
                player1.append(name)
                break




def main() -> None:

    print('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')

    champions = load_some_champs()

    #send this to client for printing
    print_available_champs(champions)
    print('\n')

    player1 = []
    player2 = []

    #ha på serversiden
    # Champion selection
    for _ in range(2):
        input_champion('Player 1', 'red', champions, player1, player2)
        input_champion('Player 2', 'blue', champions, player2, player1)

    print('\n')

    #ha på serversiden
    # Match
    match = Match(
        Team([champions[name] for name in player1]),
        Team([champions[name] for name in player2])
    )
    match.play()

    # Print a summary
    #do this client side by sending match object to client

    #code for sending match object to client goes here (to finalize the game)

    print_match_summary(match)


if __name__ == '__main__':
    main()
