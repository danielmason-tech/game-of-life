import random
import pygame
from grid import Grid

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (99, 99, 99)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
TILE_SIZE = 10

HEIGHT = WINDOW_HEIGHT // TILE_SIZE
WIDTH = WINDOW_WIDTH // TILE_SIZE

FPS = 10

def draw_grid(screen, positions, dead_positions):
    for position in dead_positions:
        x, y = position
        top_left = (x * TILE_SIZE, y * TILE_SIZE)
        pygame.draw.rect(screen, BLACK, (*top_left, TILE_SIZE, TILE_SIZE))


    for position in positions:
        x, y = position    
        top_left = (x * TILE_SIZE, y * TILE_SIZE)
        pygame.draw.rect(screen, WHITE, (*top_left, TILE_SIZE, TILE_SIZE))

    # Draw grid lines
    for row in range(HEIGHT):
        pygame.draw.line(screen, GREY, (0, row * TILE_SIZE), (WINDOW_WIDTH, row * TILE_SIZE))

    for col in range(WIDTH):
        pygame.draw.line(screen, GREY, (col * TILE_SIZE, 0), (col * TILE_SIZE, WINDOW_HEIGHT))

def gen_starting_positions():
    starting_positions = [(x, y) for x in range(HEIGHT) for y in range(WIDTH)]
    for i in starting_positions[:]:
        if random.choice([True, False]):
            starting_positions.remove(i)

    board = Grid(HEIGHT, WIDTH, starting_positions)
    return board

def main():

    # Glider
    #starting_positions = [(1, 1), (2, 2), (3, 0), (3, 1), (3, 2)]

    board = gen_starting_positions()

    pygame.init()
    pygame.display.set_caption("Game of Life")
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)

    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    running = True
    while running:
        clock.tick(FPS)
        board.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        running = False
                    case pygame.K_r:
                        board = gen_starting_positions()
                        screen.fill(BLACK)

        draw_grid(screen, board.alive_cells, board.dead_cells)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
