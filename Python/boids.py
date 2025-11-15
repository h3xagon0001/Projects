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

def positionRollback(bird: Bird, horizontalSize: int, verticalSize: int):
    mode = "bounce" # "rollback" or "bounce"
    if mode == "rollback":
        if bird.x < 0:
            bird.x += horizontalSize
        elif bird.x > horizontalSize:
            bird.x -= horizontalSize

        if bird.y < 0:
            bird.y += verticalSize
        elif bird.y > verticalSize:
            bird.y -= verticalSize

    elif mode == "bounce":
        if bird.x < 0:
            if bird.heading > 180:
                bird.heading += 2 * (270 - bird.heading)
            else:
                bird.heading -= 2 * (bird.heading - 90)

            bird.x = 0

        elif bird.x > horizontalSize:
            if bird.heading > 180:
                bird.heading += 2 * (270 - bird.heading)
            else:
                bird.heading -= 2 * (bird.heading - 90)

            bird.x = horizontalSize

        if bird.y < 0:
            if bird.heading > 270:
                bird.heading += 2 * (bird.heading - 270)
            else:
                bird.heading -= 2 * (bird.heading - 180)

            bird.y = 0
        elif bird.y > verticalSize:
            if bird.heading > 270:
                bird.heading += 2 * (360 - bird.heading)
            else:
                bird.heading -= 2 * (bird.heading - 180)

            bird.y = verticalSize

def getClosestBird(origin: Bird, birdList: list[Bird], maxDistance: int):
    distanceList: list[tuple[float, Bird]] = []
    for bird in birdList:
        if bird != origin:
            distance = math.sqrt(
                (bird.x - origin.x) ** 2 +
                (bird.y - origin.y) ** 2
            )
            distanceList.append((distance, bird))
    
    distanceList.sort(key=lambda x: x[0])

    if distanceList[0][0] < maxDistance:
        return distanceList[0][1]
    else:
        return None

horizontalSize = 800
verticalSize = 600
framerate = 60

birdList: list[Bird] = []

for i in range(100):
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

    for bird in birdList:
        closestBird = getClosestBird(bird, birdList, 1000)
        if closestBird != None:
            angleDifference = bird.heading - closestBird.heading
            if angleDifference > 180:
                angleDifference -= 360

            if angleDifference > 1:
                bird.heading -= 1
            elif angleDifference < -1:
                bird.heading += 1

        bird.move()
        positionRollback(bird, horizontalSize, verticalSize)
        pygame.draw.circle(screen, "white", (bird.x, bird.y), 5)

    pygame.display.flip()
    deltaTime = clock.tick(framerate) / 1000

pygame.quit()