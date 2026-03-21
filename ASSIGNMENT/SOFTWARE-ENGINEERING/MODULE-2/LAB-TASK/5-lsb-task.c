/* Write a C program to check if a number is even or odd using an if-else
statement. Extend the program using a switch statement to display the month
name based on the user’s input (1 for January, 2 for February, etc.).*/


#include<stdio.h>
int main(){
    int number;

    // Even Odd checker
    printf("---------EVEN OR ODD------");
    printf("\n\nenter a number :");
    scanf("%d",&number);
    if(number%2==0){
        printf("\nnumber is even");
    }
    else{
        printf("\nnumber is odd");
    }

    printf("\n\n---------NUMBER BASED MONTH------");
    int choose ;
    // month name

    printf("\n\n1,2,3,4,5,6,7,8,9,10,11,12");
    printf("\nSelect your Month Number:");
    scanf("%d",&choose);
    switch (choose)
    {
    case 1:
        printf("January");
        break;
    case 2:
        printf("February");
        break;
    case 3:
        printf("March");
        break;
    case 4:
        printf("April");
        break;
    case 5:
        printf("May");
        break;
    case 6:
        printf("June");
        break;
    case 7:
        printf("July");
        break;
    case 8:
        printf("August");
        break;
    case 9:
        printf("September");
        break;
    case 10:
        printf("Octomber");
        break;
    case 11:
        printf("November");    
        break;
    case 12:
        printf("December");    
        break;
    default:
        printf("Invalid Month Number");
    }
}

