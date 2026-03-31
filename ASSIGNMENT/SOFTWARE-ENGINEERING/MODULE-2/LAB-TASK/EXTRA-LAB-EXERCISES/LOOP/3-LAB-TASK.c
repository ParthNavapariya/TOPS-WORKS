// Write a C program that takes an integer from the user and calculates the sum of its digits
// using a while loop.
// • Challenge: Extend the program to reverse the digits of the number.

#include <stdio.h>

int main() {
    int num, originalNum, sum = 0, reversed = 0;

    // Ask the user for input
    printf("Enter an integer: ");
    scanf("%d", &num);

    originalNum = num; // Keep a copy of the original number

    // Calculate the sum of digits
    int temp = num; // Use a temporary variable for sum calculation
    while (temp != 0) {
        sum += temp % 10;  // Add the last digit to sum
        temp /= 10;        // Remove the last digit
    }

    // Reverse the digits
    temp = num; // Reset temp for reversal
    while (temp != 0) {
        reversed = reversed * 10 + (temp % 10); // Build the reversed number
        temp /= 10;
    }

    // Print results
    printf("Sum of digits of %d is: %d\n", originalNum, sum);
    printf("Reversed number: %d\n", reversed);

}