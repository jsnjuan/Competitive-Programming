#include <stdio.h>

int main()
{
  long long n,m,a, b, aux, max;
  int i,j, maxlength;
  while(scanf("%lld%lld",&a,&b)==2)
  {
        n=a;m=b;
	if(a>b) {aux=b; b=a; a=aux;}
        max=0;j=1;
	for(i=a;i<=b;i++)
        {
		aux=i; j=1;
                while(aux!=1)
		{	  
			if(aux%2==0) aux/=2;
	  		else aux=(aux*3+1);
        	        j++;
        	}  
        if(j>max) {max=j;maxlength=i;}
        }
 	printf("%lld %lld %lld the number is %d\n",n,m,max, maxlength); 
  } 
  return 0;
} 
