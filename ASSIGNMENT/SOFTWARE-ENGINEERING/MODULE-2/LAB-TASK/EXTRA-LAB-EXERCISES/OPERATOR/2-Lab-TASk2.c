/*Write a C program that takes an integer from the user and checks the following using
different operators:
o Whether the number is even or odd.
o Whether the number is positive, negative, or zero.
o Whether the number is a multiple of both 3 and 5.*/

// Whether the number is positive, negative, or zero.

#include<stdio.h>
int main(){
    int number;
    printf("enter number");
    scanf("%d",&number);
    if(number>0){
        printf("\nenter number is positive");
    }
    else if(number == 0){
        printf("\nenter number is zero");
    }
    else{
        printf("\nenter numer is negative");
    }
}