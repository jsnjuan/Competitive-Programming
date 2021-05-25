#include <stdio.h>

int main()
{
	long long cont=0,cont2,fib[50];
	int i;
	fib[0]=1;
	fib[1]=2;
	for(i=2;i<=50;i++)
	{
		fib[i]=fib[i-1]+fib[i-2];
	}cont=0;
	for(i=0;i<=40;i++)
	{
		if(fib[i]%2==0 && fib[i]<4000000)
			cont+=fib[i];
	} 
	printf("EL VALOR BUSCADO ES: %lld.\n",cont);
	return 0;
}
