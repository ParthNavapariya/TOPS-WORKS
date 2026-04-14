// Write a C program that takes a number as input and checks whether it is a palindrome using
// a function.
// • Challenge: Modify the program to check if a given string is a palindrome.
#include <stdio.h>
#include <string.h>

// Function to check number palindrome
int isPalindromeNumber(int n) {
    int original = n, reverse = 0, rem;

    while(n > 0) {
        rem = n % 10;
        reverse = reverse * 10 + rem;
        n = n / 10;
    }

    if(original == reverse)
        return 1;
    else
        return 0;
}

// Function to check string palindrome
int isPalindromeString(char str[]) {
    int start = 0;
    int end = strlen(str) - 1;

    while(start < end) {
        if(str[start] != str[end])
            return 0;
        start++;
        end--;
    }
    return 1;
}

int main() {
    int num;
    char str[100];

    // Number check
    printf("Enter a number: ");
    scanf("%d", &num);

    if(isPalindromeNumber(num))
        printf("Number is Palindrome\n");
    else
        printf("Number is NOT Palindrome\n");

    // String check
    printf("\nEnter a string: ");
    scanf("%s", str);

    if(isPalindromeString(str))
        printf("String is Palindrome\n");
    else
        printf("String is NOT Palindrome\n");

    return 0;
}