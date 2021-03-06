# -*- coding: utf-8 -*-
import GameClient, pygame, sys, socket, WinScreen, json
"""
Created on Sun Mar 30 16:05:48 2014

The Initializing script for the game

@author: Will Stiles
@author: Diego Gonzalez
"""

"""
    Play the game
"""

def main():
    #Create a game client
    client = GameClient.GameClient()

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
            keysP = pygame.key.get_pressed()
        # Check for movement
        client.move()
        # Check for jumping
        client.jump()
        # Render the screen
        client.render()
        # Do attacks if necessary
        client.attack()
    if client.ifWin() == 1:
        WinScreen.winner("Player 1")
    elif client.ifWin() == 2:
        WinScreen.winner("Player 2")


"""
    Call main method when script is run
"""
if __name__ == "__main__":
    main()
