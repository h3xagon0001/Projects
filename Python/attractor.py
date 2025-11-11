import pygame
import math
import random

class Bird:
    def __init__(self, x: float, y: float, speed: float, heading: float):
        self.x = x
        self.y = y
        self.speed = speed
        self.heading = heading

    def clampHeading(self):
        if self.heading >= 360:
            self.heading -= 360
        elif self.heading < 0:
            self.heading += 360        

    def getComponentVectors(self) -> tuple[float, float]:
        self.clampHeading()

        xVelocity = self.speed * math.cos(math.radians(self.heading))
        yVelocity = self.speed * math.sin(math.radians(self.heading))

        return xVelocity, yVelocity
    
    def move(self):
        xVelocity, yVelocity = self.getComponentVectors()
        self.x += xVelocity
        self.y -= yVelocity

def getHeadingToPoint(origin: tuple[float, float], target: tuple[float, float]):
    horizontalDistance = target[0] - origin[0]
    verticalDistance = target[1] - origin[1]

    alpha = math.degrees(math.atan(abs(verticalDistance) / abs(horizontalDistance)))

    # target is right of origin
    if horizontalDistance > 0:
        # target is up of origin
        if verticalDistance < -1:
            return alpha
        
        # target is down of origin
        else:
            return 360 - alpha

    # target is left of origin
    else:
        # target is up of origin
        if verticalDistance < -1:
            return 180 - alpha
        
        # target is down of origin
        else:
            return 180 + alpha


horizontalSize = 800
verticalSize = 600
framerate = 60

birdList: list[Bird] = []

for i in range(10):
    birdList.append(Bird(
        random.uniform(0, horizontalSize),
        random.uniform(0, verticalSize),
        5,
        random.uniform(0, 360)
    ))

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

    mousePos = pygame.mouse.get_pos()

    for bird in birdList:
        targetHeading = getHeadingToPoint((bird.x, bird.y), mousePos)
        angleDifference = bird.heading - targetHeading
        if angleDifference > 180:
            angleDifference -= 360

        if angleDifference > 0:
            bird.heading -= 10
        elif angleDifference < 0:
            bird.heading += 10

        bird.move()
        
        pygame.draw.circle(screen, "white", (bird.x, bird.y), 5)

    pygame.display.flip()
    deltaTime = clock.tick(framerate) / 1000

pygame.quit()