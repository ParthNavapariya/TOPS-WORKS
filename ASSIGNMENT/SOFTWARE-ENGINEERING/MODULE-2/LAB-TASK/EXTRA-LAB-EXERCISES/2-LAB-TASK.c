//  Write a C program that generates Pascal’s Triangle up to N rows using loops.
// • Challenge: Implement the same program using a recursive function.

#include <stdio.h>

// Function to calculate factorial
int fact(int n) {
    int f = 1;
    for (int i = 1; i <= n; i++) {
        f *= i;
    }
    return f;
}

int main() {
    int n;

    printf("Enter number of rows: ");
    scanf("%d", &n);

    for (int i = 0; i < n; i++) {
        
        // spacing (triangle shape માટે)
        for (int s = 0; s < n - i - 1; s++) {
            printf(" ");
        }

        for (int j = 0; j <= i; j++) {
            int value = fact(i) / (fact(j) * fact(i - j));
            printf("%d ", value);
        }

        printf("\n");
    }

    return 0;
}
