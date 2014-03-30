# -*- coding: utf-8 -*-
import GameClient, pygame, sys
"""
Created on Sun Mar 30 16:05:48 2014

@author: Will Stiles
@author: Diego Gonzalez
"""

"""
    Play the game
"""
def complicated():
    client = GameClient.GameClient()
    while 1:
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
                    client.jump1Peak = client.player1Rect.top - 100
                    print client.jump1Peak
            client.keys = pygame.key.get_pressed()
        # Check for movement
        client.move()
        # Check for jumping
        client.jump()
        # Render the screen
        client.render()
        
"""
    Call main method when script is run
"""
if __name__ == "__main__":
    main()
