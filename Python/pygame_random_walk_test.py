import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
running = True
deltaTime = 0

particleList: list[pygame.Vector2] = []

for i in range(1000):
    particleList.append(pygame.Vector2(
        x = random.randint(0, 500),
        y = random.randint(0, 500)
    ))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for particle in particleList:
        particle.x += random.choice([-1, 1])
        particle.y += random.choice([-1, 1])

        if particle.x < 0:
            particle.x = screen.get_width()
        elif particle.x > screen.get_width():
            particle.x = 0
        
        if particle.y < 0:
            particle.y = screen.get_height()
        elif particle.y > screen.get_width():
            particle.y = 0

        pygame.draw.circle(screen, "white", particle, 5)

    pygame.display.flip()

    deltaTime = clock.tick(30) / 1000

pygame.quit()