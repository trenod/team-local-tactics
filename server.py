from rich import print
from rich.prompt import Prompt
from rich.table import Table

from champlistloader import load_some_champs, load_some_champs_as_string
from core import Champion, Match, Shape, Team
from socket import AF_INET, SOCK_STREAM, socket, SOL_SOCKET, SO_REUSEADDR







#class for player with data on each player that updates with both clients?

#class player 


#følgende metode kommuniserer med serveren og sjekker med den om champion er tilgjengelig,
#serveren sjekker det opp mot hva som er registrert fra før (i cvs fil/database)


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
        answer = conn.recv(1024).decode()
        match answer:
            case name if name not in champions:
                #need to check with the server here to see if champion is available
                #so the following needs to be sent to the client depending on outcome:
                #print(f'The champion {name} is not available. Try again.')
                conn.send('The champion {name} is not available. Try again.'.encode())
            case name if name in player1:
                conn.send('{name} is already in your team. Try again.')
            case name if name in player2:
                conn.send('{name} is in the enemy team. Try again.')
            case _:
                player1.append(name)

                if (player1.__sizeof__ == 2):
                    conn.send('done')
                    
                break




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
    

    #basic send/receive over network:

    #sentence = conn.recv(1024).decode()
    #new_sentence = sentence.upper()
    #conn.send(new_sentence.encode())

    print('\n'
          'Welcome to [bold yellow]Team Local Tactics[/bold yellow]!'
          '\n'
          'Each player choose a champion each time.'
          '\n')

    champions = load_some_champs_as_string()



    #send this to client for printing
    #need to parse champions object as text and send to client

    conn1.send(champions.encode())
    conn2.send(champions.encode())

    player1 = []
    player2 = []

    #champion1 = conn1.recv(1024).decode()
    #champion2 = conn2.recv(1024).decode()

    #ha på serversiden:
    # Champion selection
    for _ in range(2):
        input_champion('Player 1', 'red', champions, player1, player2, conn1)
        input_champion('Player 2', 'blue', champions, player2, player1, conn2)

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

    conn1.send(match.encode())
    conn2.send(match.encode())

    #print_match_summary(match)

    conn1.close()
    conn2.close()


if __name__ == '__main__':
    main()
