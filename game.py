from player import Enemy
from screen import Screen
import random
from player import Enemy
from player import Player



class Game:
    def __init__(self, score=0, speed=10):
        self.score=score
        self.speed=speed
        self.enemy_list=[]
    def update_enemies(self, screen_width):
        if len(self.enemy_list)<10:
            y=random.random()
            if y>0.5:
                enem_x=random.randint(0, screen_width)
                enem_y=0
                enemy=Enemy(enem_x, enem_y)
                self.enemy_list.append(enemy)

    def drop_enemies(self, screen_height):
        new_enemy=[]
        for enemy in self.enemy_list:
            if enemy.y > 0 and enemy.y <= screen_height:
                enemy.y+=self.speed+random.randint(0, 5)
                new_enemy.append(enemy)
            else:
                self.score+=1
                x=random.random()
                if x > 0.5:
                    enemy.y=0
                    enemy.x=random.randint(0, Screen.width)
                    new_enemy.append(enemy)
        self.enemy_list=new_enemy
    def set_level(self):
        self.speed= self.score/5  + 5
    def check_collision(self, player):
        for enemy in self.enemy_list:
            if enemy.detect_collision(player):
                return True
            return False