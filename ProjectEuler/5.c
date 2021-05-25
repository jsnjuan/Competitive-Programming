#include <stdio.h>

int main()
{
	long long i,band=0,n;
 	n=60;
 	while(band==0)
 	{
 		for(i=1;i<=20;i++)
 		{
 			if(n%i!=0)
 				break;
 		}
 		if(i=21) band=1;
 		n++;
 	}
 	printf("%lld",n);
	return 0;
}
