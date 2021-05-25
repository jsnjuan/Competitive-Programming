#include <stdio.h>

char A[6];

int destaza(long long n,long long a)
{
	long long c,i=0,cont=0;
	while(a>=10)
	{
		c=a%10;
		cont+=c*c*c*c*c;
		a=(a-(c))/10;
	}
	cont+=a*a*a*a*a;
	if(cont==n)
		return 1;
	else return 0;
}

int main()
{
	long long i,j,cont=0;
	for(i=2;i<999999;i++)
		if(destaza(i,i)) cont+=i;
	printf("LA SUMA DE LOS NUMEROS QUE SE PUEDEN ESCRIBIR COMO POTENCIAS 5 DE SUS DIGITOS ES %d",cont);
	return 0;	
}
