#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "raymath.h"

const int WINDOW_WIDTH = 500;
const int WINDOW_HEIGHT = 500;

const int ARRAY_LENGTH = 20;
int numArray[64];

// inclusive
const int maxValue = 20;
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

int main() {
	srand(time(NULL));

	for (int i = 0; i < ARRAY_LENGTH; i++) {
		numArray[i] = rand() % (maxValue + 1 - minValue) + minValue;
		// printf("%d", numArray[i]);
	}

	printArray(ARRAY_LENGTH, numArray);

	while (!isSorted(ARRAY_LENGTH, numArray)) {
		bubbleSort(ARRAY_LENGTH, numArray);
		printArray(ARRAY_LENGTH, numArray);
	}

	return 0;
}
