#include <stdio.h>

int main()
{ 
 int s=0,i;
 //scanf("%d",&i);
 for(i=3;i<100;i++)
   {
        if(i%3==0) s+=i;
        else if(i%5==0)s+=i; 
        printf("s = %d\n",s);   
   }
 printf("THE SUM IS : %d\n.",s); 
}

