// Write a C program that implements a simple number guessing game. The program should
// generate a random number between 1 and 100, and the user should guess the number
// within a limited number of attempts.
// • Challenge: Provide hints to the user if the guessed number is too high or too low.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int number, guess;
    int attempts = 0, maxAttempts = 7;

    // random number generate કરવા માટે
    srand(time(0));
    number = rand() % 100 + 1; // 1 to 100

    printf(" Number Guessing Game (1 to 100)\n");
    printf("You have %d attempts!\n", maxAttempts);

    while (attempts < maxAttempts) {
        printf("\nEnter your guess: ");
        scanf("%d", &guess);

        attempts++;

        if (guess == number) {
            printf("🎉 Correct! You guessed in %d attempts.\n", attempts);
            break;
        }
        else if (guess > number) {
            printf("Too High! Try again.\n");
        }
        else {
            printf("Too Low! Try again.\n");
        }
    }

    if (guess != number) {
        printf("\n You lost! The correct number was: %d\n", number);
    }

    return 0;
}