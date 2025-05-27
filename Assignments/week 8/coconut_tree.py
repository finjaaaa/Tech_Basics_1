# importing required library
import pygame
import random
import math

#creating a class for the picture with correct size
class PalmTree:
    def __init__ (self,screen_width, screen_height):
        self.image = pygame.image.load("palmtree.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))

#random starting position

        self.x = random.randint(0, screen_width)
        self.y = random.randint(0, screen_height)
        self.speed_x = 3
        self.speed_y = 2
#rotation variables
        self.center_x = random.randint(100, screen_width-100)
        self.center_y = random.randint(100, screen_height-100)
        self.radius = random.randint(30, 120)
        self.angle = random.uniform(0,2*math.pi)
        self.angle_speed = random.uniform(0.02, 0.05)

    def move(self):
        self.angle += self.angle_speed
        self.x = self.center_x + self.radius * math.cos(self.angle)
        self.y = self.center_y + self.radius * math.sin(self.angle)

    def draw(self, screen):
        screen.blit(self.image,(self.x, self.y))

# initializing pygame and screen
pygame.init()
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (173,216,230)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('image')
clock = pygame.time.Clock()

# creating the palmtree objects (this was created with ai)
palm = [PalmTree(SCREEN_WIDTH, SCREEN_HEIGHT)for _ in range(5)]

#running loop
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((173,216,230))

    for tree in palm:
        tree.move()
        tree.draw(screen)

    pygame.display.flip()
pygame.quit()











