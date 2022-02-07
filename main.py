import pygame
from player import Haggy
pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Hagi-wagi")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

FPS = 60
clock = pygame.time.Clock()
road_chunks = [
    [pygame.image.load('sprites/road.png'), [0, H - 100]],
    [pygame.image.load('sprites/road.png'), [2404, H - 100]]
]

y = 270
speed = 5

p = Haggy(y)
group_Haggy = pygame.sprite.Group(p)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                p.isJump = True

    sc.fill(WHITE)
    for road_chunk in road_chunks:
        if road_chunk[1][0] <= -2400:
            road_chunk[1][0] = road_chunks[len(road_chunks) - 1][1][0] + 2400

            road_chunks[0], road_chunks[1] = road_chunks[1], road_chunks[0]
            break

        road_chunk[1][0] -= speed
        sc.blit(road_chunk[0], (road_chunk[1][0], road_chunk[1][1]))
    group_Haggy.update()
    group_Haggy.draw(sc)
    pygame.display.update()
    clock.tick(FPS)