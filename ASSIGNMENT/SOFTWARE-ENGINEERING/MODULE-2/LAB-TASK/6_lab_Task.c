/*Write a C program to print numbers from 1 to 10 using all three types of loops
(while, for, do-while)*/

#include<stdio.h>
int main(){
    // for loop
    printf("\n-------FOR LOOP---------");
    int i ;
    for(i=0;i<=10;i++){
        printf("\n\t%d",i);
    }

    // while loop
    printf("\n-------WHILe LOOP---------");
    int j=1;
    while(j <= 10){
        printf("\n\t%d",j);
        j++;
    }
    //do while
    printf("\n-------DO WHILE LOOP---------");
    int k=1;
    do{
        printf("\n\t%d",k);
        k++;
    }while(k<=10);

}