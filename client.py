#from team-local-tactics import print_available_champs, input_champion, print_match_summary
#import TCP stuff
from socket import AF_INET, SOCK_STREAM, socket

sock = socket(AF_INET, SOCK_STREAM)
server_address = ("localhost", 5555)
sock.connect(server_address)

#client mottar et objekt fra server som kan brukes til å printe ting til spilleren

sentence = input("Input lowercase sentence: ")
sock.send(sentence.encode())
new_sentence = sock.recv(1024).decode()
print(f"From Server: {new_sentence}")
sock.close()


#konvertere til match objekt på clientside og sende det til serverside