#include <stdio.h>

long long int m[100][100];  //donde hay 100 es 15 . .

long long max(long long a,long long b)
{
	if(a>b) return a;
	return b;
}

int main()
{
	int i,j,peso,c,n;
	for(i=0;i<100;i++)
		for(j=0;j<100;j++)
			m[i][j]=0;		
	for(i=1;i<=100;i++)
		for(j=0;j<i;j++)
		{
			scanf("%d",&peso);
			m[i-1][j]=peso;
		}
	for(i=1;i<=100;i++)
	{
		m[i][i]=m[i][i]+m[i-1][i-1];
		m[i][0]=m[i][0]+m[i-1][0];
	}
	for(i=1;i<100;i++)
		for(j=1;j<i;j++)
			m[i][j]+=max(m[i-1][j],m[i-1][j-1]);
	c=m[99][0];
	for(i=1;i<100;i++)
	{
		if(m[99][i]>c) c=m[99][i];
	}
	printf("%lld\n",c);
	return 0;
}
