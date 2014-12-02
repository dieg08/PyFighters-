# -*- coding: utf-8 -*-
import GameClient, pygame, sys, socket, WinScreen, json, errno, CharSelect 
from socket import error as socket_error
"""
Created on Sun Mar 30 16:05:48 2014

The Initializing script for the game

@author: Will Stiles
@author: Diego Gonzalez
"""

"""
    Play the game
"""

#def main(socket):
def main(socket, character):
    player = 3
    #Initialize the connection with the server
    s = socket
    #Send a mesage to the server (broken)
    send(s, player, None, None)
    #Catch a reply from the server, will contain the player
    reply = s.recv(1024)
    #The player number for this client
    player = reply
    #Create a game client
    client = GameClient.GameClient(player)
    #Print the player number (test)
    print "Player: " + str(player)
    #Parameters of the message
    center = None 
    keysp = None
    #Message that will be sent
    message = None
    #Start the game
    while client.ifWin() < 1:
        """
            Event Handling
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the game
                sys.exit()
            if event.type == pygame.KEYDOWN and client.jump1Double < 2:
                client.jump1Double = client.jump1Double + 1
                keypressed = pygame.key.name(event.key)
                if keypressed == pygame.key.name(pygame.K_SPACE):
                    client.jump1Peak = client.player.getHitBox().top - 100
                    print client.jump1Peak
            client.keys = pygame.key.get_pressed()
        opponent = client.getPlayer()
        hitbox = opponent.getHitBox()
        center = hitbox.center
        keysp = client.getKeys()
        message = center
        # sends packet for movement
        send(s, player, message, keysp)
        # receive packet
        data = s.recv(1024)
        reply = json.loads(data)
        print str(reply)
        # Check for movement
        if reply != None:
            client.move(reply[1])
        #client.keys = reply[2]
        # Check for jumping
        client.jump()
        # Render the screen
        client.render()
        # Do attacks if necessary
        client.attack()
    if client.ifWin() == 1:
        WinScreen.winner("Player 1")
        end(s)
    elif client.ifWin() == 2:
        WinScreen.winner("Player 2")
        end(s)

"""
    Send information to the server
"""
def send(s, player, msg, keys):
    #Package to hold information to send to the server
    message = [player, msg, keys]
    packet = json.dumps(message)
    #Try sending the message and catch any errors
    try:
        s.send(packet)
    except socket.error:
        print 'Send failed'
        sys.exit

def end(s):
    message = "Done"
    try:
        s.send(message)
    except socket.error:
        print 'Send Failed'
        sys.exit
"""
    Call main method when script is run
"""
if __name__ == "__main__":
    main()
