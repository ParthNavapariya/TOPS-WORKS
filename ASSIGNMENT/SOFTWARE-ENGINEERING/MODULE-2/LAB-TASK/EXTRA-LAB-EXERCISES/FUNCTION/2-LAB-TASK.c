// LAB EXERCISE 2: Factorial Calculation
// • Write a C program that calculates the factorial of a given number using a function.
// • Challenge: Implement both an iterative and a recursive version of the factorial function and
// compare their performance for large numbers.
#include <stdio.h>

// Iterative
int fact_iter(int n) {
    int f = 1;
    for(int i=1; i<=n; i++) {
        f = f * i;
    }
    return f;
}

// Recursive
int fact_rec(int n) {
    if(n==0 || n==1)
        return 1;
    return n * fact_rec(n-1);
}

int main() {
    int n;
    printf("Enter number: ");
    scanf("%d", &n);

    printf("Iterative = %d\n", fact_iter(n));
    printf("Recursive = %d\n", fact_rec(n));

    return 0;
}