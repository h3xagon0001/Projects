#include <stdio.h>
#include <stdbool.h>

int main() {

    int mora = 20;
    float watts = 9.8;
    float angle = 45.5;
    double e = 2.718281828459045235360287471352;
    char vowel = 'Y';
    char gamemode[] = "Currency Wars";
    bool isDead = true;

    printf("You have %d mora\n", mora);
    printf("I consume %.2f watts of power\n", watts);
    printf("They are %.1f° above us\n", angle);
    printf("The value of e is %.15lf\n", e);
    printf("%c is sometimes a vowel\n", vowel);
    printf("The new endgame mode is called %s\n", gamemode);
    
    printf("You are ");
    if (isDead) {
        printf("dead");
    }
    else {
        printf("alive");
    }
    printf("\n");
    
    return 0;
}