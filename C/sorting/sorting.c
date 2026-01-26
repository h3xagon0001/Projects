#include "raylib.h"
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const int WINDOW_WIDTH = 1600;
const int WINDOW_HEIGHT = 900;

const int TOP_MARGIN = 10;
const int BOTTOM_MARGIN = 10;
const int LEFT_MARGIN = 10;
const int RIGHT_MARGIN = 10;

const int GAP_SIZE = 2;

const int ARRAY_LENGTH = 50;
int numArray[64];

// inclusive
const int maxValue = 200;
const int minValue = 0;

int printArray(int length, int* numArray) {
	for (int i = 0; i < length; i++) {
		printf("%d", numArray[i]);

		if (i < length - 1) printf(", ");
	}
	printf("\n");

	return 0;
}

int isSorted(int length, int* numArray) {
	for (int i = 0; i < length - 1; i++) {
		if (numArray[i] > numArray[i+1]) return false;
	}
	return true;
}

int bubbleSort(int length, int* numArray) {
	int temp;
	for (int i = 0; i < length - 1; i++) {
		if (numArray[i] > numArray[i+1]) {
			temp = numArray[i];
			numArray[i] = numArray[i+1];
			numArray[i+1] = temp;
		}
	}

	return 0;
}

int drawBars(int top, int bottom, int left, int right, int length, int* numArray, int gapSize, int windowWidth, int windowHeight) {
	// find max of array
	float greatestValue = numArray[0];	
	for (int i = 0; i < length; i++) {
		if (numArray[i] > greatestValue) greatestValue = numArray[i];
	}

	int barWidth = ((windowWidth - left - right) / length) - gapSize;
	int maxBarHeight = windowHeight - top - bottom;

	for (int i = 0; i < length; i++) {
		DrawRectangle(
				left + i * (barWidth + gapSize) + gapSize,
				top + maxBarHeight - maxBarHeight * (numArray[i] / greatestValue),
				barWidth,
				maxBarHeight * (numArray[i] / greatestValue),
				RAYWHITE
				);
	}
	
	return 0;
}

int main() {
	srand(time(NULL));

	// add random values to array	
	for (int i = 0; i < ARRAY_LENGTH; i++) {
		numArray[i] = rand() % (maxValue + 1 - minValue) + minValue;
		// printf("%d", numArray[i]);
	}

	printArray(ARRAY_LENGTH, numArray);

	// setup for raylib
	SetTargetFPS(5);
	InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, "Sorting");

	while (!WindowShouldClose()) {
		BeginDrawing();
		ClearBackground(BLACK);
		drawBars(TOP_MARGIN, BOTTOM_MARGIN, LEFT_MARGIN, RIGHT_MARGIN, ARRAY_LENGTH, numArray, GAP_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT);

		while (!isSorted(ARRAY_LENGTH, numArray)) {
			bubbleSort(ARRAY_LENGTH, numArray);
			printArray(ARRAY_LENGTH, numArray);

			ClearBackground(BLACK);
			drawBars(TOP_MARGIN, BOTTOM_MARGIN, LEFT_MARGIN, RIGHT_MARGIN, ARRAY_LENGTH, numArray, GAP_SIZE, WINDOW_WIDTH, WINDOW_HEIGHT);
			
		EndDrawing();
		}
	}

	return 0;
}
