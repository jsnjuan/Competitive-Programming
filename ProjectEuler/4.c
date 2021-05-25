#include <stdio.h>
#include <stdlib.h>

char A[10],B[10];

int maximo(int a,int b)
{
	if(a>b)	return a;
	return b;
}

void pone_en_cadena(int a)
{
	int i=0,j=0;
	while(a>=10)
	{
		A[i]=a%10+'0';
		a=(a-(a%10))/10;
		i++;
	}
	A[i]=a+'0';
	A[i+1]='\0';
}

int main()
{
	int i,j,c,n,ad=-1;
	char buffer[6];
	for(i=100;i<999;i++)
		for(j=100;j<999;j++)
		{
			n=i*j;
			pone_en_cadena(n);
			c=atoi(A);
			if(c==n)
			{
			ad=maximo(ad,n);
			//printf(" %5d EN NUMERO   :%10s (EN CADENA)---INDICES i =%d ; j=%d.\n",n,A,i,j);
			}
		}
	printf(" EL PALINDROMO MAS GRANDE ES : %d.\n",ad);
	return 0;
}
