//  Write a C program that checks whether a given number is an Armstrong number or not (e.g.,
// 153 = 1^3 + 5^3 + 3^3).
// • Challenge: Write a program to find all Armstrong numbers between 1 and 1000.

#include <stdio.h>

// Function to calculate power
int power(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) {
        result *= base;
    }
    return result;
}

// Function to count digits
int countDigits(int num) {
    int count = 0;
    while (num != 0) {
        count++;
        num /= 10;
    }
    return count;
}

// Function to check Armstrong
int isArmstrong(int num) {
    int original = num;
    int sum = 0, digit, digits;

    digits = countDigits(num);

    while (num != 0) {
        digit = num % 10;
        sum += power(digit, digits);
        num /= 10;
    }

    return (sum == original);
}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (isArmstrong(num))
        printf("Armstrong Number\n");
    else
        printf("Not an Armstrong Number\n");

    return 0;
}