import pygame, sys

class base(object):

    def _init_(self, music, picture):
        pygame.init()
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)
        self.screen = pygame.display.get_surface()
        self.screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
        self.level = pygame.image.load(picture).convert()
        self.levelRect = self.level.get_rect(center=(400, 300))
        self.screen.blit(self.level, (0, 0))

    def getLevel(self):
        return self.level

    def getScreen(self):
        return self.screen
