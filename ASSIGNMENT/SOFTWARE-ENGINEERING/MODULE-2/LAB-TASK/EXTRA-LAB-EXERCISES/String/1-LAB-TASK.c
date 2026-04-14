//  Write a C program that takes a string as input and reverses it using a function.
// • Challenge: Write the program without using built-in string handling functions.

#include <stdio.h>

// Function to reverse string
void reverseString(char str[]) {
    int i = 0, j = 0;
    char temp;

    // Find length manually
    while (str[j] != '\0') {
        j++;
    }
    j = j - 1; // last index

    // Reverse logic
    while (i < j) {
        temp = str[i];
        str[i] = str[j];
        str[j] = temp;

        i++;
        j--;
    }
}

int main() {
    char str[100];

    printf("Enter a string: ");
    scanf("%s", str);  // Note: space handle nahi kare

    reverseString(str);

    printf("Reversed string: %s\n", str);

    return 0;
}

