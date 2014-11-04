__author__ = 'Will Stiles'
import pygame
import Platform
"""
    The Stage the game will be played on

    @author     Will Stiles
    @version    October 29, 2014
"""


class Stage:


    """
        Create a stage with optional Platforms

        @param  music       The music for the stage
        @param  picture     The picture for the stage
        @param  width       The width of the stage
        @param  height      The height of the stage
        @param  center      (Optional) The center platform
        @param  left        (Optional) The left platform
        @param  right       (Optional) The right platform
    """
    def __init__(self, music, picture, width, height, center=None,
                 left=None, right=None):
        # The music for the stage
        self.music = music
        # Load the game music
        pygame.mixer.music.load(self.music)
        # Play the game music
        pygame.mixer.music.play(-1)
        # The level image
        self.level = pygame.image.load(picture).convert()
        # The edge of the level screen
        self.levelRect = self.level.get_rect(center=((width / 2), (height / 2)))
        # Set center platform
        self.center = center
        # Set left platform
        self.left = left
        # Set right platform
        self.right = right

    """
        Get the right platform for the stage
    """
    def getRightPlatform(self):
        return self.right

    """
        Get the left platform for the stage
    """
    def getLeftPlatform(self):
        return self.left

    """
        Get the center platform for the stage
    """
    def getCenterPlatform(self):
        return self.center

    """
        Get the level
    """
    def getLevel(self):
        return self.level

    """
        Get the rectangle for the level
    """
    def getLevelRect(self):
        return self.levelRect
