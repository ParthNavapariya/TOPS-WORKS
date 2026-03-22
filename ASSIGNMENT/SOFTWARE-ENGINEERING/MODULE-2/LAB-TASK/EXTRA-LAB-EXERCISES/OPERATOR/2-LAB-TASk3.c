/*Write a C program that takes an integer from the user and checks the following using
different operators:
o Whether the number is even or odd.
o Whether the number is positive, negative, or zero.
o Whether the number is a multiple of both 3 and 5.*/

// o Whether the number is a multiple of both 3 and 5.

#include<stdio.h>
int main(){
    int number1;
    printf("enter number");
    scanf("%d",&number1);
    if(number1%3==0 && number1%5==0){
        printf("Number is multiple of both 3 and 5\n");
    }
    else{
        printf("Number is NOT multiple of both 3 and 5\n");
    }

}