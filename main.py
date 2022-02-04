import pygame
pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Hagi-wagi")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

FPS = 60
clock = pygame.time.Clock()

x = W // 2
y = H // 2
speed = 5

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    elif keys[pygame.K_RIGHT]:
        x += speed
    elif keys[pygame.K_UP]:
        y -= speed
    elif keys[pygame.K_DOWN]:
        y += speed


    sc.fill(WHITE)
    pygame.draw.rect(sc, BLUE, (x, y, 10, 20))
    pygame.display.update()

    clock.tick(FPS)