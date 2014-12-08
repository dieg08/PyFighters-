# -*- coding: utf-8 -*-
import GameClient, pygame, sys, socket, WinScreen, json, errno, CharSelect, time 
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
    init_send(s, player)
    #Catch a reply from the server, will contain the player
    reply = s.recv(1024)
    #The player number for this client
    player = reply
    #send the character
    char_send(s, character)
    #THe parameter to be passed to game client
    reply = s.recv(1024)
    parameter = [character, reply]
    #Create a game client
    if player == '1':
        parameter = [character, reply]
    else:
        parameter = [reply, character]
    client = GameClient.GameClient(int(player), parameter)

    #Print the player number (test)
    print "Player: " + str(player)
    #print the opponents character (test)
    print "Opponent: " + reply
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
        health = (opponent.getHP(), client.getOpponent().getHP())
        # sends packet for movement
        send(s, player, message, keysp, health)
        # receive packet
        data = s.recv(1024)
        reply = json.loads(data)
        # Check for movement
        if client.getKeys() != None:
            client.move(reply[1])
            #client.move(reply[1], reply[2])
        #client.keys = reply[2]
        # Check for jumping
        client.jump()
        # Render the screen
        if client.getKeys() != None:
            client.render()
        # Do attacks if necessary
        if client.getKeys() != None:
            client.attack()
            client.getPlayer().setHP(reply[3][0])
            client.getOpponent().setHP(reply[3][1])
            
    if client.ifWin() == 1:
        WinScreen.winner("Player 1")
        end(s)
    elif client.ifWin() == 2:
        WinScreen.winner("Player 2")
        end(s)

"""
    Send information to the server
"""
def send(s, player, msg, keys, health):
    #Package to hold information to send to the server
    message = [player, msg, keys, health]
    packet = json.dumps(message)
    #Try sending the message and catch any errors
    try:
        s.send(packet)
    except socket.error:
        print 'Send failed'
        sys.exit

def init_send(s, player):
    #Package to hold information to send to the server
    message = str(player)
    #Try sending the message and catch any errors
    try:
        s.send(message)
    except socket.error:
        print 'Send failed'
        sys.exit

def char_send(s, char):
    #Package to hold information to send to the server
    message = char
    #Try sending the message and catch any errors
    try:
        s.send(message)
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
