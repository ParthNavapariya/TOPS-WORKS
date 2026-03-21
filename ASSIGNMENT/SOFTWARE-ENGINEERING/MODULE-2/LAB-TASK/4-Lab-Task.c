/*Write a C program that accepts two integers from the user and performs
arithmetic, relational, and logical operations on them. Display the results.*/      


#include<stdio.h>
int main(){
    int number1,number2;
    printf("enter number 1 :");
    scanf("%d",&number1);
    printf("enter number 2 :");
    scanf("%d",&number2);

    // Airthmatic Operator;
    printf("-----------AIRTHMATIC OPERATOR----------");  

    // addition
    int add = number1+number2;
    printf("\naddition \t=\t %d + %d = %d",number1,number2,add);
    
    //substraction
    int sub = number1 - number2;
    printf("\nsubstraction \t=\t %d - %d = %d",number1,number2,sub);

    //Multiplication
    int mul = number1*number2;
    printf("\nMultiplication \t=\t %d * %d = %d",number1,number2,mul);

    //division
    int div = number1/number2;
    printf("\nDvision \t=\t %d / %d = %d",number1,number2,div);

    //modulus
    int mod = number1%number2;
    printf("\nModulus \t=\t %d %% %d = %d",number1,number2,mod);

    //Relational operaotr
    printf("\n-----------RILATIONAL OPERATOR----------");
    // Equal To
    int equal = number1 == number2;
	printf("\nEqual To \t=\t %d == %d = %d ",number1,number2,equal);

    //Not Equal To
    int Nequal = number1 != number2;
    printf("\nNot Equal To \t=\t %d != %d = %d",number1,number2,Nequal);

    //Greter Than
    int greter = number1 > number2;
    printf("\nGreter Than \t=\t %d > %d = %d",number1,number2,greter);

    //Less Than
    int less = number1 < number2;
    printf("\nLess Than \t=\t %d < %d = %d",number1,number2,less);

    // Grether Than Or Equal To
    int Gequal = number1 >= number2;
    printf("\nGreter Or Equal\t=\t %d >= %d = %d",number1,number2,Gequal);

    //Less Than Or Equal To
    int Lequal = number1 <= number2;
    printf("\nLess Or equal \t=\t %d <= %d = %d",number1,number2,Lequal);

    //Logical operator
    printf("\n-----------LOGICAL OPERATOR----------");

    int number3;
    printf("\nenter number 3");
    scanf("%d",&number3);
    //and
    if(number1>number2 && number1>number3){
        printf("and \t=\t %d is bigger than %d and %d",number1,number2,number3);
    }
    else if(number2>number1 && number2>number3){
        printf("and \t=\t %d is bigger than %d and %d",number2,number1,number3);
    }
    else{
         printf("and \t=\t %d is bigger than %d and %d",number3,number1,number2);
    }

    // or 

      if (number1 > 10 || number2 > 10) {
        printf("\nOR \t= \tAt least one number is greater than 10");
    } else {
        printf("\nOr \t=\tBoth numbers are 10 or less");
    }

    // not

    if(!(number1 > number2)){
    printf("\nNOT \t=\t %d is NOT greater than %d", number1, number2);
}
else{
    printf("\nNOT \t=\t %d is greater than %d", number1, number2);
}
}

