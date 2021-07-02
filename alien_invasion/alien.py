# Mike Wilson 2 July 2021
# This program manages the 'aliens' used in Alien Invasion.

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """A class to represent an alien in the fleet"""

  def __init__(self, ai_game):
    """Initialize the alien and set its starting position"""
    super().__init__()
    self.screen = ai_game.screen

    # Load the alien image and set its rect attribute
    self.image = pygame.image.load('alien_invasion\images\\alien.bmp')
    self.rect = self.image.get_rect()

    # Start each new alien near the top left of the screen
    self.rect.x = relf.rect.width
    self.rect.y = self.rect.height

    # Store the alien's exact horizontal position
    self.x = float(self.rect.x)

    