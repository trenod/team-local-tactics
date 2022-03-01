from rich import print
from rich.prompt import Prompt
from rich.table import Table

from champlistloader import load_some_champs
from core import Champion, Match, Shape, Team


#import TCP stuff




#class for player with data on each player that updates with both clients:

#class player 



def main() -> None:

    print('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')

    champions = load_some_champs()
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
    print_match_summary(match)


if __name__ == '__main__':
    main()
