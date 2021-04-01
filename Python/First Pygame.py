#techwithtim's pygame tutorial
import pygame
pygame.init()

window = pygame.display.set_mode((640, 360))

pygame.display.set_caption("First Pygame")

x = 50
y = 295
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 640 - width - vel:
        x += vel
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 360 - height - vel:
            y += vel
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()