#include <stdio.h>

int main() {

	struct organism {
		const char* name;
		unsigned int population;
		const int consumptionPerIndividual;
		const char* consumes[2];
	};

	#define ORGANISM_COUNT 5

	struct organism ecosystem[ORGANISM_COUNT] = {
		{"Algae", 500000, 0, {"", ""}},
		{"Crab", 30000, 1, {"Algae", ""}},
		{"Shrimp", 25000, 2, {"Algae", ""}},
		{"Snapper", 4000, 3, {"Shrimp", "Crab"}},
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

	int step(struct organism* ecosystem) {
		// for each organism
		for (int i = 0; i < ORGANISM_COUNT; i++) {
			// for each organism it consumes
			for (int j = 0; j < 2; j++) {
				// search thru each organism
				for (int k = 0; k < ORGANISM_COUNT; k++) {
					if (ecosystem[i].consumes[j] == ecosystem[k].name) {
						ecosystem[k].population -= ecosystem[i].population * ecosystem[i].consumptionPerIndividual;
					}
				}
			}
		
			ecosystem[i].population *= 2;

		}
	}

	printEcosystem(ecosystem);

	while (1) {
		printf("Press ENTER to continue.");
		getchar();

		step(ecosystem);
		printEcosystem(ecosystem);
	}

	return 0;

}

