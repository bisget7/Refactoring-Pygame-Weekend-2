from colours import Colours
import pygame

class Screen:
    def __init__(self, width=800, height=600, Backgroud_colour=Colours.Backgroud_colour, font_type="monospace", font_size=35, clock_tick=20):
        self.width=width
        self.height=height
        self.Backgroud_colour=Backgroud_colour
        self.screen=pygame.display.set_mode((width, height))
        self.font_size=font_size
        self.font_type=font_type
        self.font=pygame.font.SysFont(font_type, font_size)
        self.clock=pygame.time.Clock()
        self.clock_tick=clock_tick
    

    def refresh_background(self):
        self.screen.fill(self.Backgroud_colour)
    def draw_enemies(self, enemy_list):
        for enemy in enemy_list:
            enemy.draw(self.screen)
    def draw_player(self, player):
        player.draw(self.screen)
    def draw_score_label(self, score, colour=Colours.Yellow):
        text=f"SCORE:  {score}"
        label=self.font.render(text, 2, colour)
        self.screen.blit(label, (self.width-200, self.height-40))
    def update_screen(self, player, enemy_list, score):
        self.refresh_background()
        self.draw_enemies(enemy_list)
        self.draw_player(player)
        self.draw_score_label(score)

        self.clock.tick(self.clock_tick)
        pygame.display.update()




