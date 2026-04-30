// 3. Functions & Pointers
// Write a program to:
// ● Swap two numbers using a user-defined function
// ● Implement swapping using pointers
// ● Explain why pass-by-reference is necessary here

#include<iostream>
using namespace std;

void swap(int *a, int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int main(){
    int x = 10, y = 20;

    swap(&x, &y);

    cout << "After swap:\n";
    cout << "x = " << x << " y = " << y;

    return 0;
}