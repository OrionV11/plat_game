import pygame
import random
import time
pygame.font.init()

PLAYER_HEIGHT = 60
PLAYER_WIDTH = 50
PLAYER_VEL = 1

WIDTH = 800
HEIGHT = 500

TILE_SIZE = 50


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
BG = (0,0,0)
COLOR = "white"

red = (255,0,0)
blue = (0,0,255)

def draw(player):
    WIN.fill(BG)
    pygame.draw.rect(WIN, COLOR, player)
    pygame.display.update()

class GameState:

    def __init__(self, start, quit):
        self.start = start
        self.quit = quit

    def create_menu(self, screen):
        pass

    def check_hit(self):
        pass


class Level:
    def __init__(self, level_data, background_image, music_file):
        self.level_data = level_data
        self.background = pygame.image.load(background_image)
        self.music = pygame.mixer.Sound(music_file)
        # ... other level-specific data like enemies, items

    def drawl(self, screen):
        screen.blit(self.background, (0, 0))
        # ... draw tiles based on level_data

        pass

        # ... draw enemies, items








level_map = [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,1,0,1,1],
        [1,0,0,0,1]
        ]


class Player:
    x = 60
    y = 60
    player = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    def __init__(self,fire,water):
        self.fire = True
        self.water = False

    def elements(self):
        global COLOR

        if self.fire:
            COLOR = "red"
            self.fire = False
            self.water = True
        else:
            COLOR = "blue"
            self.fire = True


def main():
    running = True
    pygame.init()
    game_state = GameState(True, False)
    playeri = Player(fire=None, water=None)
    player = pygame.Rect(playeri.x, playeri.y, PLAYER_WIDTH, PLAYER_HEIGHT)

    color_surface = pygame.Surface((100,50))
    color_surface.fill(red)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        WIN.fill((0,0,0)) #clear screen

        for row_index, row in enumerate(level_map):
            for col_index, tile_type in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                if tile_type == 0:
                    color_surface.fill(red)
                    WIN.blit(color_surface, (100, 100))
                elif tile_type == 1:
                    color_surface.fill(blue)
                    WIN.blit(color_surface, (100, 100))




        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP]:
            playeri.elements()

        pygame.display.flip()
        draw(player)
    pygame.quit()




if __name__ == "__main__":
    main()
