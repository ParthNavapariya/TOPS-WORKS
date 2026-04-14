/*Write a C program that accepts two 2x2 matrices from the user and adds them. Display the
resultant matrix.
• Challenge: Extend the program to work with 3x3 matrices and matrix multiplication.*/
#include<stdio.h>
int main(){
    int number1,number2,i,j;
    printf("enter number r");
    scanf("%d",&number1);
    printf("enter number c");
    scanf("%d",&number2);
    int matrix[number1][number2];
    for(i=0;i<number1;i++){
        for(j=0;j<number2;j++){
            printf("enter element");
            scanf("%d",&matrix[i][j]);
        }
    }



    
}