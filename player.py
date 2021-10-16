from colours import Colours
import pygame




class Player:
    def __init__(self, x, y, size, colour=Colours.player_colour):
        self.x=x
        self.y=y
        self.size=size
        self.colour=colour
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, (self.x, self.y, self.size, self.size))
    def detect_collision(self, other):
        if (self.x > other.x and self.x <= other.x+other.size) or (other.x > self.x and other.x <= self.x + self.size):
            if (self.y > other.y and self.y <= other.y+other.size) or (other.y > self.y and other.y <= self.y + self.size):
                return True
        return False
#Enemy class is a restricted version of Player class
class Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, colour=Colours.enemy_colour)

#Large_Enemy is likewise a restricted version of Player class only different from Enemy with size
class Large_Enemy(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=100, colour=Colours.enemy_colour)
#Human_player is likewise a restricted version of Player class
class Human_Player(Player):
    def __init__(self, x, y):
        super().__init__(x, y, size=50, colour=Colours.player_colour)

