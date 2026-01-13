#include <stdlib.h>
#include <time.h>
#include "raylib.h"

const int windowHeight = 500;
const int windowWidth = 500;

const int particleCount = 10000;

struct particle {
	int x;
	int y;
};

int main ()
{
	struct particle particleArray[10000] = {{0, 0}}; 

	srand(time(NULL));

	for (int i = 0; i < particleCount; i++) {
		particleArray[i].x = rand() % windowWidth + 1;
		particleArray[i].y = rand()	% windowHeight + 1;
	}

	// cap 60 fps
	SetTargetFPS(60);

	// Create the window and OpenGL context
	InitWindow(windowHeight, windowWidth, "Random Walk Test");

	// game loop
	while (!WindowShouldClose()) // run the loop until the user presses ESCAPE or presses the Close button on the window
	{
		// drawing
		BeginDrawing();

		// Setup the back buffer for drawing (clear color and depth buffers)
		ClearBackground(BLACK);

		// move and draw circle
		for (int i = 0; i < particleCount; i++) {
			if (rand() % 2 == 0) particleArray[i].x += 1;
			else particleArray[i].x -= 1;

			if (rand() % 2 == 0) particleArray[i].y += 1;
			else particleArray[i].y -= 1;

			// check if outside bounds
			if (particleArray[i].x < 0) particleArray[i].x = windowWidth;
			else if (particleArray[i].x > windowWidth) particleArray[i].x = 0;

			if (particleArray[i].y < 0) particleArray[i].y = windowHeight;
			else if (particleArray[i].y > windowHeight) particleArray[i].y = 0;

			DrawCircle(particleArray[i].x, particleArray[i].y, 1, RAYWHITE);
		}
		
		// end the frame and get ready for the next one  (display frame, poll input, etc...)
		EndDrawing();
	}

	// destroy the window and cleanup the OpenGL context
	CloseWindow();
	return 0;
}
