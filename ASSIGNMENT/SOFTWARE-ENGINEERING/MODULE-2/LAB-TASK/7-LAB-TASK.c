//  Write a C program that uses the break statement to stop printing numbers
// when it reaches 5. Modify the program to skip printing the number 3 using the
// continue statement.

#include<stdio.h>
int main(){
    int i;
    printf("\n----------BREAK STATMENT------------");
    for(i=0;i<=10;i++){
        if(i==5){
            break;
        }
        printf("\n\t%d",i);
    }
    printf("\n----------CONTINUE STATMENT------------");
    for(i=0;i<=10;i++){
        if(i==5){
            continue;
        }
        printf("\n\t%d",i);
    }
}