/*Write a C program that takes two strings from the user and concatenates them
using strcat(). Display the concatenated string and its length using
strlen().*/

#include<stdio.h>
#include<string.h>
int main(){
    char str1[20] = "paeth ";
    char str2[20] = "navapariy";

    strcat(str1,str2);
    printf("%s", str1);
   
    int len;
    len = (strlen(str1));

    printf("\n%d", len);
}