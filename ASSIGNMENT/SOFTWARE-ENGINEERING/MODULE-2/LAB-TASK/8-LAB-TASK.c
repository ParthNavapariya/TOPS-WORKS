/*Write a C program that stores 5 integers in a one-dimensional array and prints
them. Extend this to handle a two-dimensional array (3x3 matrix) and
calculate the sum of all elements.*/

#include<stdio.h>
int main(){
    int number[5],i;
    //one dimendional array
    printf("\n-------ONE DIMENSIONAL ARRAY-----------");
    for(i=0;i<5;i++){
        printf("\nenter value for %d",i);
        scanf("%d",&number[i]);
    }
    //display
    for(i=0;i<5;i++){
        printf("\n%d",number[i]);
    }

    // Two DOMENSIONAL ARAAY;
    printf("\n-------ONE DIMENSIONAL ARRAY-----------");
    int r,c,k,j;
    printf("\nenter number of row :");
    scanf("%d",&r);
    printf("\nenter number of colom :");
    scanf("%d",&c);
    int matrix[3][3];
    int sum = 0;
    for(j=0;j<r;j++){
        for(k=0;k<c;k++){
            printf("\nenter element");
            scanf("%d",&matrix[j][k]);
           sum += matrix[j][k];
        }
    }
     for(j=0;j<r;j++){
        for(k=0;k<c;k++){
            printf("\t%d",matrix[j][k]);
        }
        printf("\n");
    }
   	printf("\n\n\nSum of all the element is %d",sum);
    
}