#include <stdio.h>
int main()
{
    int choose, quantity, amount; 
    int totalamount = 0;
    char more;
do{
  
    
    printf("\n1. pizza\tPrice = 180rs/pcs,\n2. Burger\tPrice = 100rs/pcs,\n3. dosa\t\tPrice = 120rs/pcs,\n4. idli\t\tPrice = 50rs/pcs"); // menu item
    printf("\nPlease Enter Your Choice... : ");
    scanf("%d", &choose);
    if (choose == 1)
    {
        printf("\nyou have selected pizza.");
        printf("\nenter the quantity :");
        scanf("%d", &quantity);
        if (quantity > 0)
        {
            amount = quantity * 180; // amount calculation
            printf("\namount = %d",amount);
            totalamount += amount;
        };
         
    }
    else if (choose == 2)
    {
        printf("\nyou have selected burger.");
        printf("\nenter the quantity :");
        scanf("%d", &quantity);
        if (quantity > 0)
        {
            amount = quantity * 100; // amount calculation
            printf("\namount = %d",amount);
            totalamount += amount;
        }

    }
        else if (choose == 3)
        {
            printf("\nyou havse selected dosa.");
            printf("\nenter the quantity :");
            scanf("%d", &quantity);
            if (quantity > 0)
            {
                amount = quantity * 120; // amount calculation
                  printf("\namount = %d",amount);
                  totalamount += amount;
            }
        }
        else if (choose == 4)
        {
            printf("\nyou have selected idli.");
            printf("\nenter the quantity :");
            scanf("%d", &quantity);
            if (quantity > 0)
            {
                amount = quantity * 50; // amount calculation
                  printf("\namount = %d",amount);
                  totalamount += amount;
            }
        } 
   

        printf("\n");
       printf("do you want place more order ? y & n :");
        scanf(" %c",&more);
        
          if(more == 'n' || more == 'N'){
        printf("thank you for order :");
         printf("\nTotal Bill Amount = %d\n",totalamount);
    }

        }while (more=='y' || more == 'Y');
    }

    


        
     
     
