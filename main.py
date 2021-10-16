import pygame
import sys
from player import Player
from player import Human_Player
from screen import Screen
from game import Game

pygame.init()
screen=Screen()
player=Human_Player(screen.width/2, screen.height-100)
game=Game()

game_over =False

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player.x-=player.size/2
            elif event.key==pygame.K_RIGHT:
                player.x+=player.size/2
    game.update_enemies(screen.width)
    game.drop_enemies(screen.height)
    game.set_level()
    screen.update_screen(player, game.enemy_list, game.score)
    if game.check_collision(player):
        game_over = True
        break
