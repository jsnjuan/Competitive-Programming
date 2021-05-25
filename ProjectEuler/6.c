#include <stdio.h>

int main()
{
	int s=0,i,j;
        for(i=1;i<100;i++)
            for(j=i+1;j<=100;j++){   
		s+=i*j;printf("( %d , %d ) s : %d.\n",i,j,s);}
        printf(" %d\n",2*s);
} 
