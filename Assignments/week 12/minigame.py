import pygame
import random
import sys

#initializing
pygame.init()
screen_width =800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("coconut evader game")

#colours
black = (0,0,0)
white = (255, 255, 255)
lightblue =(173, 216, 230)
green = (144, 238, 144)
yellow = (255, 255, 0)
brown = (139, 69,19)

#player-surface and player rectangle
player_surface = pygame.Surface((40, 30))
player_surface.fill(green)
player_rect = player_surface.get_rect(center = (screen_width//2, screen_height//2))
player_speed = 5

#obstacles (coconuts)
class Coconut:
    def __init__(self):
        self.radius = random.randint(20, 40)
        self.color = brown
        self.x = screen_width
        self.y = random.randint(self.radius, screen_height - self.radius)
        self.speed = random.randint(3, 6)

    def update(self):
        self.x -= self.speed
        return self.x < -self.radius

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    #creating bounding box for collision
    def get_rect(self):
        return pygame.Rect(self.x -self.radius, self.y - self.radius, self.radius*2, self.radius*2)

#player variables
obstacles = []
clock = pygame.time.Clock()
score = 0
font = pygame.font.SysFont(None, 35)
game_over = False

# main game loop
running = True

while running:
    screen.fill(lightblue)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                game_over = False
                score = 0
                obstacles.clear()
                player_rect.center = (screen_width//2, screen_height//2)

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_rect.left >0:
            player_rect.x -= player_speed
        if keys[pygame.K_RIGHT] and player_rect.right < screen_width:
            player_rect.x += player_speed
        if keys[pygame.K_UP] and player_rect.top >0:
            player_rect.y -= player_speed
        if keys[pygame.K_DOWN] and player_rect.bottom < screen_height:
            player_rect.y += player_speed

        if random.random() < 0.02:
            obstacles.append(Coconut())

        for obstacle in obstacles[:]:
            if obstacle.update():
                obstacles.remove(obstacle)
                score += 1

        #collision notice
        for obstacle in obstacles:
            if player_rect.colliderect(obstacle.get_rect()):
                game_over = True

        score_text = font.render(f"Score: {score}", True, yellow)
        screen.blit(score_text, (10,10))

    screen.blit(player_surface, player_rect)
    for obstacle in obstacles:
        obstacle.draw()

    if game_over:
        game_over_text = font.render("GAME OVER - Press r to restart", True, (255,0,0))
        screen.blit(game_over_text, (screen_width//2, screen_height//2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()















