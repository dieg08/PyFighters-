import pygame
import Stage
"""
    The base for the game

    @author     Diego Gonzalez
    @author     Will Stiles
    @version    October 20, 2014
"""


class Base(object):

    """
        Create a the base for the game
    """
    def __init__(self, music):
        # Initialize Pygame
        pygame.init()
        # Create the screen display
        self.screen = pygame.display.get_surface()
        # Set the screen size
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    """
        Get the screen of the current base
    """
    def getScreen(self):
        return self.screen
