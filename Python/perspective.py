import pygame
import cv2
import numpy

def drawCuboid(screen: pygame.Surface, rgb: list[int], center: tuple[float, float], dimensions: tuple[float, float], layers: int, parallax: float, headPos: tuple[int, int], scalingFactor: float = 1) -> None:
    """Draws several quads stacked on each other, cycling through the colours given."""
    for layer in range(layers):
        pygame.draw.rect(
            screen,
            pygame.Color(round(rgb[0] / layers * layer), round(rgb[1] / layers * layer), round(rgb[2] / layers * layer)),
            pygame.Rect(
                center[0] - (dimensions[0] * (1 + scalingFactor * layer) / 2) + ((center[0] - headPos[0]) * (1 + parallax * layer)),
                center[1] - (dimensions[1] * (1 + scalingFactor * layer) / 2) + ((center[1] - headPos[1]) * (1 + parallax * layer)),
                dimensions[0] * (1 + scalingFactor * layer),
                dimensions[1] * (1 + scalingFactor * layer)
            )
        )


video_capture = cv2.VideoCapture(0)

process_this_frame = True

screenWidth: int = 1920
screenHeight: int = 1080 - 50

headPos: dict[str, int] = {
    "x": round(screenWidth / 2),
    "y": round(screenHeight / 2)
}

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()
running = True
deltaTime = 0
fps = 60

while running:
    ret, frame = video_capture.read()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        running = False

    if keys[pygame.K_w]:
        headPos["y"] -= 1
    if keys[pygame.K_s]:
        headPos["y"] += 1
    if keys[pygame.K_a]:
        headPos["x"] += -1
    if keys[pygame.K_d]:
        headPos["x"] -= -1


    screen.fill("black")

    drawCuboid(
        screen,
        [0, 0, 255],
        (round(screenWidth / 2) + 80, round(screenHeight / 2) - 100),
        (40, 120),
        100,
        0.025 / 2,
        (headPos["x"], headPos["y"]),
        0.01
    )

    drawCuboid(
        screen,
        [255, 0, 0],
        (round(screenWidth / 2) - 50, round(screenHeight / 2) - 100),
        (100, 40),
        100,
        0.025 / 2,
        (headPos["x"], headPos["y"]),
        0.01
    )

    drawCuboid(
        screen,
        [0, 255, 255],
        (round(screenWidth / 2) - 20, round(screenHeight / 2) + 100),
        (500, 20),
        100,
        0.025 / 2,
        (headPos["x"], headPos["y"]),
        0.01
    )

    drawCuboid(
        screen,
        [255, 255, 255],
        (round(screenWidth / 2), round(screenHeight / 2)),
        (50, 50),
        100,
        0.025,
        (headPos["x"], headPos["y"]),
        0.01
    )


    pygame.draw.circle(screen, "red", (headPos["x"], headPos["y"]), 2)

    pygame.display.flip()
    #deltaTime = clock.tick(60) / 1000


pygame.quit()
cv2.destroyAllWindows()