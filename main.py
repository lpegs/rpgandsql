import pygame, sys, random
from pygame.math import Vector2

class MAIN:
    
    def __init__(self):
        self.player = PLAYER()

    def draw_elements(self):
        self.draw_grass()
        self.player.draw_player()

    def update(self):
        self.player.movement()

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

        
class PLAYER:
    def __init__(self):
        self.body = [Vector2(5,5)]
        self.direction = Vector2(0,0)

    def draw_player(self):
        for player_block in self.body:
            x_pos = int(player_block.x)
            y_pos = int(player_block.y)
            player_rect = pygame.Rect(x_pos * cell_size, y_pos * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (255,255,255), player_rect)

    def movement(self):
        body_copy = self.body[:]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]
        self.body = self.body[:-1]
        self.direction = Vector2(0,0)
        

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
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.player.direction.y != 1:
                    main_game.player.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN:
                if main_game.player.direction.y != -1:
                    main_game.player.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if main_game.player.direction.x != -1:
                    main_game.player.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if main_game.player.direction.x != 1:
                    main_game.player.direction = Vector2(-1,0)
    

    screen.fill((89, 171, 92))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
