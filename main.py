import pygame
import random
import time
pygame.font.init()

PLAYER_HEIGHT = 60
PLAYER_WIDTH = 50
PLAYER_VEL = 1

WIDTH = 800
HEIGHT = 500

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
BG = (0,0,0)
COLOR = "white"

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

    def draw(self, screen):
        screen.blit(self.background, (0, 0))
        # ... draw tiles based on level_data
        level_map = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]

        # ... draw enemies, items

    def update(self):
        # ... update enemy positions, handle item interactions
        pass


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


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + PLAYER_WIDTH <= WIDTH:
            player.x += PLAYER_VEL
        if keys[pygame.K_UP]:
            playeri.elements()

        draw(player)
    pygame.quit()




if __name__ == "__main__":
    main()
