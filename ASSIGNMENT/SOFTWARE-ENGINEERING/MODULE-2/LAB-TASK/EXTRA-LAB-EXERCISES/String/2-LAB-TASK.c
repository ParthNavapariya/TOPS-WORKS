// Write a C program that takes a string from the user and counts the number of vowels and
// consonants in the string.
// • Challenge: Extend the program to also count digits and special characters.

#include <stdio.h>

void countCharacters(char str[]) {
    int i = 0;
    int vowels = 0, consonants = 0, digits = 0, special = 0;
    char ch;

    while (str[i] != '\0') {
        ch = str[i];

        // Check vowels
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
            ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
            vowels++;
        }
        // Check consonants (alphabets only)
        else if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            consonants++;
        }
        // Check digits
        else if (ch >= '0' && ch <= '9') {
            digits++;
        }
        // बाकी બધું special characters
        else if (ch != ' ' && ch != '\n') {
            special++;
        }

        i++;
    }

    printf("Vowels: %d\n", vowels);
    printf("Consonants: %d\n", consonants);
    printf("Digits: %d\n", digits);
    printf("Special Characters: %d\n", special);
}

int main() {
    char str[200];

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);  // space handle કરે છે

    countCharacters(str);

    return 0;
}