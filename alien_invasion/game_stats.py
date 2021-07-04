# Mike Wilson 2 July 2021
# Keeps track of game states for Alien Invasion.

class GameStats:
  """Track stats for Alien Invasion."""

  def __init__(self, ai_game):
    """Initialize statistics."""
    self.settings = ai_game.settings
    self.reset_stats()

    # Start Alien Invasion in an active state.
    self.game_active = False

  def reset_stats(self):
    """Initialize statistics that can change during the game."""
    self.ships_left = self.settings.ship_limit
    self.score = 0