#include <stdio.h>

int main() {

	struct organism {
		const char* name;
		const int population;
		const int consumptionPerIndividual;
		const char* consumes[2];
	};

	#define ORGANISM_COUNT 5

	struct organism ecosystem[ORGANISM_COUNT] = {
		{"Algae", 100000, 0, {"", ""}},
		{"Crab", 30000, 10, {"Algae", ""}},
		{"Shrimp", 25000, 8, {"Algae", ""}},
		{"Snapper", 4000, 5, {"Shrimp", "Crab"}},
		{"Heron", 350, 4, {"Snapper", "Crab"}}
	};

	int printEcosystem(struct organism* ecosystem) {
		for (int i = 0; i < ORGANISM_COUNT; i++) {
			printf("Name: %8s    ", ecosystem[i].name);
			printf("Population: %8i    ", ecosystem[i].population);
			printf("CPI: %4i    ", ecosystem[i].consumptionPerIndividual);
		
			printf("Consumes: ");
			for (int j = 0; j < 2; j++) {
				if (ecosystem[i].consumes[j] != "" && j != 0) {
					printf(", ");
				}
				printf("%s", ecosystem[i].consumes[j]);
			}
		
			printf("\n");
		}
	}

	printEcosystem(ecosystem);

	return 0;

}

