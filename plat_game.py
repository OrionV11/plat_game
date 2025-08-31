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

def draw(win, player, level):
    level.drawl(win)
    pygame.draw.rect(win, COLOR, player)
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
    def __init__(self, level_data, background_image=None, music_file=None):
        self.level_data = level_data
        self.background = pygame.image.load(background_image) if background_image else None
        self.music = pygame.mixer.Sound(music_file) if music_file else None
        
        # ... other level-specific data like enemies, items

    def drawl(self, screen):
        if self.background:
            screen.blit(self.background, (0, 0))
        
        for row_index, row in enumerate(self.level_data):
            for col_index, tile_type in enumerate(row):
                x = col_index * TILE_SIZE
                y = row_index * TILE_SIZE

                tile_surface = pygame.Surface((TILE_SIZE, TILE_SIZE))
                if tile_type == 0:
                    tile_surface.fill(red)
                elif tile_type == 1:
                    tile_surface.fill(blue)
                screen.blit(tile_surface, (x, y))

    def check_player_tile_match(self, player):
        #Get tile coordinates
        tile_x = int(player.x / TILE_SIZE)
        tile_y = int(player.y / TILE_SIZE)

        #Ensure tile coordinates the player is on
        if 0 <= tile_y < len(self.level_data) and 0 <= tile_x < len(self.level_data[0]):
            tile_type = self.level_data[tile_y][tile_x]

            # Determine the tile color
            tile_color = None
            if tile_type == 0:
                tile_color = red
            elif tile_type == 1:
                tile_color = blue
    
            # Check if player color matches tile color
            # Assuming player.COLOR holds the current color (red or blue)
            if tile_color and COLOR == tile_color:
                return True
        return False

        # ... draw tiles based on level_data

        pass

        # ... draw enemies, items

level_map = [
        [1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,1,1,0,0,0,0,0,1],
        [1,1,0,1,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1]
        ]


class Player:
    x = 60
    y = 60
    player = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

    def __init__(self,fire,water):
        self.fire = True
        self.water = False
        self.y_vel = 0
        self.gravity = 0.1


    def elements(self):
        global COLOR

        if self.fire:
            COLOR = "red"
            self.fire = False
            self.water = True
        else:
            COLOR = "blue"
            self.fire = True

    def apply_gravity(self):
        self.y_vel += self.gravity
        self.player.y += self.y_vel

    def jump(self):
        pass


def main():
    running = True
    pygame.init()
    game_state = GameState(True, False)
    playeri = Player(fire=None, water=None)
    player = pygame.Rect(playeri.x, playeri.y, PLAYER_WIDTH, PLAYER_HEIGHT)

    level = Level(level_map)

    ground_level = HEIGHT - PLAYER_HEIGHT
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
            if level.check_player_tile_match(player):
                print("Player color matches tile color")
        
        playeri.apply_gravity()
        player.y = playeri.player.y

        if player.y >= ground_level:
            player.y = ground_level
            playeri.y_vel = 0


        draw(WIN, player, level)
    pygame.quit()

if __name__ == "__main__":
    main()
