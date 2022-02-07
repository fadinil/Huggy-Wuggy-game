import pygame


class Haggy(pygame.sprite.Sprite):
    def __init__(self, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = [
            pygame.image.load('sprites/huggy1.png'),
            pygame.image.load('sprites/huggy2.png')
        ]
        self.y = y
        self.index = 0
        self.counter = 0
        self.isJump = False
        self.jumpCount = 10
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(70, self.y))

    def update(self, *args):
        self.rect = self.image.get_rect(center=(70, self.y))
        self.jump()
        self.counter += 1
        if self.counter == 10:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.counter = 0
            self.image = self.images[self.index]

    def jump(self):
        if self.isJump:
            if self.jumpCount >= -10:
                neg = 1
                if self.jumpCount < 0:
                    neg = -1
                self.y -= self.jumpCount ** 2 * 0.3 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10
