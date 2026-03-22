//  Write a C program that takes three numbers from the user and determines:
// o The largest number.
// o The smallest number.
// • Challenge: Solve the problem using both if-else and switch-case statements


#include<stdio.h>
int main(){
    int number1,number2,number3;
    printf("Enter Number 1");
    scanf("%d",&number1);
    printf("Enter Number 2");
    scanf("%d",&number2);
    printf("Enter Number 3");
    scanf("%d",&number3);

    printf("---------------SWITCH-STATMENT-------------------");
    switch ((number1<number2 && number1 < number3) * 1 +
            (number2<number1 && number2 < number3) * 2 +
            (number3<number2 && number3 < number1) * 3)
    {
    case 1:
        printf("\n%d is smaller than %d and %d ",number1,number2,number3);
        break;
    case 2:
        printf("\n%d is smaller than %d and %d ",number2,number1,number3);
        break;
    case 3:
        printf("\n%d is smaller than %d and %d ",number3,number2,number1);
        break;    
    default:
        break;
    }


    printf("\n---------------IF-ELSE-STATMENT-------------------");

    if(number1<number2 && number1<number3){
        printf("\n%d is smaller than %d and %d",number1,number2,number3);
    }
    else if(number2<number1 && number2<number3){
         printf("\n%d is smaller than %d and %d",number2,number1,number3);
    }
    else{
         printf("\n%d is smaller than %d and %d",number3,number2,number1);   
    }
}