import pygame, sys, random
from pygame.math import Vector2

class PLAYER:
    def __init__(self):
        self.pos = Vector2(10,10)
        self.direction = Vector2(0,0)

    def draw_player(self):
        player_rect = pygame.Rect(cell_size, cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, (255,255,255), player_rect)

class MAIN:
    def __init__(self):
        self.player = PLAYER()

#    def update(self):


    def draw_elements(self):
        self.draw_grass()
        self.player.draw_player()

    def draw_grass(self):
        grass_color = (89, 210, 92)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)
 

pygame.init()
pygame.display.init()

cell_number = 30
cell_size = 40
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size - 600))

clock = pygame.time.Clock()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       # if event.type == SCREEN_UPDATE:
            # update what?
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_UP:
#                pygame.Rect.move(1,0)
#            if event.key == pygame.K_DOWN:
#                main_game.player.direction = Vector2(0, 1)
#            if event.key == pygame.K_LEFT:
#                main_game.player.direction = Vector2(-1, 0)
#            if event.key == pygame.K_RIGHT:
#                main_game.player.direction = Vector2(1, 0)

    screen.fill((89, 171, 92))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
