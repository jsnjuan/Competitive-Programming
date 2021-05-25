#include <stdio.h>

int minimo(int  a,int b)
{
	if(a<b)	return a;
	return b;
}

int main()
{
	int  m[80][80];
	char aux;
	int i,j;fflush(stdin);
	for(i=0;i<80;i++)
		for(j=0;j<80;j++)
		{
			scanf("%d",&m[i][j]);
			scanf("%c",&aux);
		}
	for(i=1;i<80;i++)
	{
		m[0][i]+=m[0][i-1];
		m[i][0]+=m[i-1][0];
	}
	for(i=1;i<80;i++)
		for(j=1;j<80;j++)
			m[i][j]+=minimo(m[i-1][j],m[i][j-1]);
	for(i=0;i<80;i++)
	{
		for(j=0;j<80;j++)
			printf("%7d",m[i][j]);
		printf("\n");			
	}
	printf("EL NUMERO MINIMO ES %d.\n",m[79][79]);
	return 0;
}
