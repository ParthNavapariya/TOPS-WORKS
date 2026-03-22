/*• Write a C program that acts as a simple calculator. The program should take two numbers
and an operator as input from the user and perform the respective operation (addition,
subtraction, multiplication, division, or modulus) using operators.
• Challenge: Extend the program to handle invalid operator inputs.*/


#include<stdio.h>
int main(){
    int number1,number2,choose;
    printf("\nenter number 1");
    scanf("%d",&number1);
    printf("\nenter number 2");
    scanf("%d",&number2);

    printf("\n1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION4\n\4.DIVISION\n5.MODULUS");
    printf("\n\nselect operation");
    scanf("%d",&choose);

    if(choose == 1){
        int add;
        add = number1+number2;
        printf("%d + %d = %d",number1,number2,add);
    }
     if(choose == 2){
        int sub;
        sub = number1-number2;
        printf("%d - %d = %d",number1,number2,sub);
    }
     if(choose == 3){
        int mul;
        mul = number1*number2;
        printf("%d * %d = %d",number1,number2,mul);
    }
     if(choose == 4){
        int div;
        div = number1%number2;
        printf("%d / %d = %d",number1,number2,div);
    }
     if(choose == 5){
        int mod;
        mod = number1%number2;
        printf("%d %% %d = %d",number1,number2,mod);
    }
}