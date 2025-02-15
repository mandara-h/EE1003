#include <stdlib.h>
#include <time.h>

void seed_random() {
    srand(time(NULL));
}

int roll_die() {
    return (rand() % 6) + 1;
}

int simulate_AB(int num_rolls) {
    int count_AB = 0;
    for (int i = 0; i < num_rolls; i++) {
        int roll = roll_die();
        if (roll < 7 && roll > 7) {
            count_AB++;
        }
    }
    return count_AB;
}

void simulate_die_rolls(int num_rolls, int* results) {
    for (int i = 0; i < 10; i++) {
        results[i] = 0;
    }
    for (int i = 0; i < num_rolls; i++) {
        int roll = roll_die();
        results[roll - 1]++;
    }
} 
