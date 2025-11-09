import pygame, random

screenWidth = 600
screenHeight = 400
cellSize = 25

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True
deltaTime = 0

snakePos: list[dict[str, int]] = [
    {
    "x": round((screenWidth / cellSize) / 2),
    "y": round((screenHeight / cellSize) / 2)
    },
    {
    "x": round((screenWidth / cellSize) / 2) - 1,
    "y": round((screenHeight / cellSize) / 2)
    },
    {
    "x": round((screenWidth / cellSize) / 2) - 2,
    "y": round((screenHeight / cellSize) / 2)
    }
]
heading = "up"

fruitPos: dict[str, int] = {}
while fruitPos == {}:
        fruitPos["x"] = random.randint(0, round(screenWidth / cellSize) - 1)
        fruitPos["y"] = random.randint(0, round(screenHeight / cellSize) - 1)

        if {"x": fruitPos["x"], "y": fruitPos["y"]} in snakePos:
            fruitPos = {}
        
        else:
            break

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False        

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and heading != "down":
        heading = "up"
    elif keys[pygame.K_s] and heading != "up":
        heading = "down"
    elif keys[pygame.K_a] and heading != "right":
        heading = "left"
    elif keys[pygame.K_d] and heading != "left":
        heading = "right"

    if heading == "up":
        snakePos.insert(
            0,
            {
                "x": snakePos[0]["x"],
                "y": snakePos[0]["y"] - 1
            }
        )
    elif heading == "down":
        snakePos.insert(
            0,
            {
                "x": snakePos[0]["x"],
                "y": snakePos[0]["y"] + 1
            }
        )
    elif heading == "left":
        snakePos.insert(
            0,
            {
                "x": snakePos[0]["x"] - 1,
                "y": snakePos[0]["y"]
            }
        )
    elif heading == "right":
        snakePos.insert(
            0,
            {
                "x": snakePos[0]["x"] + 1,
                "y": snakePos[0]["y"]
            }
        )

    if snakePos[0]["x"] < 0:
        snakePos[0]["x"] = round(screenWidth / cellSize) - 1
    elif snakePos[0]["x"] > round(screenWidth / cellSize) - 1:
        snakePos[0]["x"] = 0

    if snakePos[0]["y"] < 0:
        snakePos[0]["y"] = round(screenHeight / cellSize) - 1
    elif snakePos[0]["y"] > round(screenHeight / cellSize) - 1:
        snakePos[0]["y"] = 0

    if snakePos[0] == fruitPos:
        fruitPos = {}
        while fruitPos == {}:
            fruitPos["x"] = random.randint(0, round(screenWidth / cellSize) - 1)
            fruitPos["y"] = random.randint(0, round(screenHeight / cellSize) - 1)

            if {"x": fruitPos["x"], "y": fruitPos["y"]} in snakePos:
                fruitPos = {}
            
            else:
                break

    else:
        snakePos.pop()
        if snakePos[0] in snakePos[1:]:
            input()
            running = False

    screen.fill("black")

    for x in range(round(screenWidth / cellSize)):
        for y in range(round(screenHeight / cellSize)):
            if {"x": x, "y": y} in snakePos:
                scaling = 2 ** (-0.1 * (snakePos.index({"x": x, "y": y}) + 1))

                pygame.draw.rect(
                    screen,
                    "white",
                    (
                        cellSize * x + 0.5 * ((1 - scaling) * cellSize),
                        cellSize * y + 0.5 * ((1 - scaling) * cellSize),
                        cellSize * scaling,
                        cellSize * scaling
                    )
                )
            
            elif {"x": x, "y": y} == fruitPos:
                pygame.draw.rect(
                    screen,
                    "red",
                    (cellSize * x, cellSize * y, cellSize, cellSize)
                )

            else:
                pygame.draw.rect(
                    screen,
                    "black",
                    (cellSize * x, cellSize * y, cellSize, cellSize)
                )

    pygame.display.flip()

    deltaTime = clock.tick(10) / 1000

pygame.quit()