#include <stdio.h>

int main()
{
    int a, b, c;
    for(c=2;c<1000;c++)
    {  
  	for(a=1;a<c-1;a++)
        { 	
     		for(b=a+1;b<c;b++)
                {
			 if( (a*a + b*b )== c*c  && (a+b+c==1000)) 
			 printf(" CASO ESPECIAL : %d^2 + %d^2 = %d^2\nYA QUE  %d + %d + %d = 1000. . .o no??",a,b,c,a,b,c); 
                }
        }
    }
    return 0;
}

