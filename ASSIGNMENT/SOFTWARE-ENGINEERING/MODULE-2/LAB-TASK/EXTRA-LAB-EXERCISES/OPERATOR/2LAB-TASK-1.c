/*Write a C program that takes an integer from the user and checks the following using
different operators:
o Whether the number is even or odd.
o Whether the number is positive, negative, or zero.
o Whether the number is a multiple of both 3 and 5.*/


//Whether the number is even or odd.
#include<stdio.h>
int main(){
    int number;
    printf("enter number");
    scanf("%d",&number);
    if(number%2==0){
        printf("Number Is Even");
    }
    else{
        printf("Number Is Odd");
        }
}