# Mike Wilson 30 June 2021
# This program manages the bullets for Alien_Invasion

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
  """A class to manage bullets fired from the ship"""

  def __init__(self, ai_game):
    """Create a bullet object at the ship's current position."""
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings
    self.color = self.settings.bullet_color

    # Create a bullet rect at (0,0) then set the correct position
    self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        self.settings.bullet_height)
    self.rect.midtop = ai_game.ship.rect.midtop

    # Store the bullet's posiiton as a decimal value.
    self.y = float(self.rect.y)

  def update(self):
    """Move the bullet up the screen."""
    # Update the decimal position of the bullet.
    self.y -= self.settings.bullet_speed
    # Update teh rect position.
    self.rect.y = self.y

  def draw_bullet(self):
    """Draw the bullet to the screen."""
    pygame.draw.rect(self.screen, self.color, self.rect)