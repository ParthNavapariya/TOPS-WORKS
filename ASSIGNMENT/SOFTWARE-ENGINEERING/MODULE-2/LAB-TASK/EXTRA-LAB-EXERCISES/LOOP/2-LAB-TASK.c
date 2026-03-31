// Write a C program that takes an integer input from the user and prints its multiplication
// table using a for loop.
// • Challenge: Allow the user to input the range of the multiplication table (e.g., from 1 to N)


#include<stdio.h>
int main(){
    printf("\n---------NORMAL_MULTIPLICATION TABEL---------------------");
    int i,number1;
    printf("\nenter nuber1");
    scanf("%d",&number1);
    for(i=1;i<=10;i++){
        int mul;
        mul = number1 * i;
        printf("\n%d * %d = %d",number1,i,mul);
    }


    printf("\n---------CHALLANGE MULTIPLICATION TABEL---------------------");

       int j,number,number2;
    printf("\nenter nuber1");
    scanf("%d",&number);
    printf("\nenter nuber2");
    scanf("%d",&number2);
    for(j=1;j<=number2;j++){
        int mul;
        mul = number * j;
        printf("\n%d * %d = %d",number1,j,mul);
    }


}