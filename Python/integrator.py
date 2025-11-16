import pygame

def mapToTarget(fromRange: tuple[float, float], toRange: tuple[float, float], value: float):
    fromWidth = fromRange[1] - fromRange[0]
    toWidth = toRange[1] - toRange[0]
    return toRange[0] + (((value - fromRange[0])* toWidth) / fromWidth)


horizontalSize = 600
verticalSize = 600

lowerBound = -1
upperBound = 1

pygame.init()
screen = pygame.display.set_mode((horizontalSize, verticalSize))
clock = pygame.time.Clock()
running = True
deltaTime = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    pygame.draw.line(
        screen, "white",
        (
            mapToTarget(
                (lowerBound, upperBound),
                (0, horizontalSize),
                0
            ),
            0
        ),
        (
            mapToTarget(
                (lowerBound, upperBound),
                (0, horizontalSize),
                0
            ),
            verticalSize
        )



    pygame.display.flip()

    deltaTime = clock.tick(30) / 1000

pygame.quit()