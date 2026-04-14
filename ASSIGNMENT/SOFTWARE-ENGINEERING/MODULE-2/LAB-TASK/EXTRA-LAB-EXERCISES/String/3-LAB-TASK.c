// Write a C program that counts the number of words in a sentence entered by the user.
// • Challenge: Modify the program to find the longest word in the sentence.

#include <stdio.h>

void countWordsAndLongest(char str[]) {
    int i = 0, words = 0;
    int maxLen = 0, currLen = 0;
    int start = 0, maxStart = 0;

    while (str[i] != '\0') {

        // જો character space કે newline ના હોય → word નો ભાગ
        if (str[i] != ' ' && str[i] != '\n') {
            currLen++;
        } else {
            // word complete થયો
            if (currLen > 0) {
                words++;

                // longest word check
                if (currLen > maxLen) {
                    maxLen = currLen;
                    maxStart = i - currLen;
                }
                currLen = 0;
            }
        }
        i++;
    }

    // last word માટે check (important)
    if (currLen > 0) {
        words++;
        if (currLen > maxLen) {
            maxLen = currLen;
            maxStart = i - currLen;
        }
    }

    // longest word print
    printf("Total Words: %d\n", words);

    printf("Longest Word: ");
    for (int j = 0; j < maxLen; j++) {
        printf("%c", str[maxStart + j]);
    }
    printf("\nLength: %d\n", maxLen);
}

int main() {
    char str[200];

    printf("Enter a sentence: ");
    fgets(str, sizeof(str), stdin);

    countWordsAndLongest(str);

    return 0;
}