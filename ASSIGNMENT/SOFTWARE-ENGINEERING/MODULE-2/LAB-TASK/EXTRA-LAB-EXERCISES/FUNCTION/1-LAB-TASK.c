// Write a C program that generates the Fibonacci sequence up to N terms using a recursive
// function.
// • Challenge: Modify the program to calculate the Nth Fibonacci number using both iterative
// and recursive methods. Compare their efficiency.
#include <stdio.h>

// Recursive method
int fibRecursive(int n) {
    if (n <= 1)
        return n;
    return fibRecursive(n - 1) + fibRecursive(n - 2);
}

// Iterative method
int fibIterative(int n) {
    int a = 0, b = 1, c, i;

    if (n <= 1)
        return n;

    for (i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int main() {
    int n;

    printf("Enter N: ");
    scanf("%d", &n);

    printf("Recursive Result: %d\n", fibRecursive(n));
    printf("Iterative Result: %d\n", fibIterative(n));

    return 0;
}