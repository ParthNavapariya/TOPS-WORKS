// • Write a C program that accepts 10 integers from the user and stores them in an array. The
// program should then find and print the maximum and minimum values in the array.
// • Challenge: Extend the program to sort the array in ascending order.


#include<stdio.h>
int main()
{
    int number[10],i,temp,j;
    for(i=0;i<10;i++){
        printf("enter value %d " ,i);
        scanf("%d",&number[i]);

    }
    int max,min;
    max=number[0];
    min=number[0];
    for(i=0;i<10;i++){
        printf("\n%d",number[i]);
        if(max<number[i]){
            max = number[i];
        }
        if(min>number[i]){
            min = number[i];
        }
    }
    printf("\nmaximum number is = %d",max);
    printf("\nminimum number is %d",min);
 for(i = 0; i < 10 - 1; i++){
        for(j = 0; j < 10 - i - 1; j++){
            if(number[j] > number[j+1]){
                temp = number[j];
                number[j] = number[j+1];
                number[j+1] = temp;
            }
        }
    }

    // Output Sorted Array
    printf("\nSorted array (Ascending):\n");
    for(i = 0; i < 10; i++){
        printf("%d ", number[i]);
    }

}