#include <stdio.h>
#include <math.h> 
 
int main()
{
    int a[100][100],n[10001], i, j;
    for(i=0;i<100;i++)
	for(j=0;j<100;j++)
               a[i][j]=pow(i+2,j+2); 

    for(i=0;i<100;i++)
    {	
	printf("\n");
	for(j=0;j<100;j++)
               printf("%d^%d = %d  ",i+2,j+2,a[i][j]); 
                
    }
    return 0;
}
