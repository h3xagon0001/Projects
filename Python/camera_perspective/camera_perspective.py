import pygame
import cv2
import face_recognition
import numpy

def drawCuboid(screen: pygame.Surface, rgb: list[int], center: tuple[float, float], dimensions: tuple[float, float], layers: int, parallax: float, headPos: tuple[int, int], scalingFactor: float = 1) -> None:
    """Draws several quads stacked on each other, cycling through the colours given."""
    for layer in range(layers):
        pygame.draw.rect(
            screen,
            pygame.Color(round(rgb[0] / layers * layer), round(rgb[1] / layers * layer), round(rgb[2] / layers * layer)),
            pygame.Rect(
                center[0] - (dimensions[0] * (1 + scalingFactor * layer) / 2) + ((headPos[0] - center[0]) * (1 + parallax * layer)),
                center[1] - (dimensions[1] * (1 + scalingFactor * layer) / 2) + ((center[1] - headPos[1]) * (1 + parallax * layer)),
                dimensions[0] * (1 + scalingFactor * layer),
                dimensions[1] * (1 + scalingFactor * layer)
            )
        )


video_capture = cv2.VideoCapture(1)
face_image = face_recognition.load_image_file("image.png")
face_encoding = face_recognition.face_encodings(face_image)[0]

known_face_encodings = [face_encoding]
known_face_names = ["Ji Kin"]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

screenWidth: int = 1920
screenHeight: int = 1080

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

    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = numpy.ascontiguousarray(small_frame[:, :, ::-1])
        
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = numpy.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)


    
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 5
        right *= 5
        bottom *= 5
        left *= 5

        headPos["x"] = ((left + right) / 2) / 640 * screenWidth * 0.5 + screenWidth * 0.25
        headPos["y"] = ((top + bottom) / 2) / 480 * screenHeight * 0.5 + screenHeight * 0.25

        """
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        """

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


    #pygame.draw.circle(screen, "red", (headPos["x"], headPos["y"]), 2)

    pygame.display.flip()

    #cv2.imshow('Video', frame)

    #deltaTime = clock.tick(60) / 1000


pygame.quit()
cv2.destroyAllWindows()