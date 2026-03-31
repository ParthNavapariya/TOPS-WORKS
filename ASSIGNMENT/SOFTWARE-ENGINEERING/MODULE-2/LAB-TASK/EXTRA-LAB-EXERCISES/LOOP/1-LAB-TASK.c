// Write a C program that checks whether a given number is a prime number or not using a for
// loop.
// • Challenge: Modify the program to print all prime numbers between 1 and a given number.
#include <stdio.h>

int main() {
    int num, i, isPrime;

    // Ask user for input
    printf("Enter an integer: ");
    scanf("%d", &num);

    // Check if the number is prime
    if (num <= 1) {
        printf("%d is not a prime number.\n", num);
    } else {
        isPrime = 1; // Assume number is prime
        for (i = 2; i * i <= num; i++) { // Check divisibility up to sqrt(num)
            if (num % i == 0) {
                isPrime = 0; // Not prime
                break;
            }
        }

        if (isPrime) {
            printf("%d is a prime number.\n", num);
        } else {
            printf("%d is not a prime number.\n", num);
        }
    }

    // Challenge: Print all prime numbers from 1 to num
    printf("Prime numbers between 1 and %d: ", num);
    for (i = 2; i <= num; i++) {
        int j, primeFlag = 1;
        for (j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                primeFlag = 0;
                break;
            }
        }
        if (primeFlag) {
            printf("%d ", i);
        }
    }
    printf("\n");

    return 0;
}