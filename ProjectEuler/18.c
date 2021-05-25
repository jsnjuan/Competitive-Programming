# include <stdio.h>

int m[15][15];

int mayor(int i,int j,int x,int y)
{
	int a,b;
	if(i==x)
		return m[i][j];
	else
	{
		a=mayor(i+1,j,x,y);
		b=mayor(i+1,j+1,x,y);
		return ((a>b)?a+m[i][j]:b+m[i][j]);
	}
}

int main()
{
	int i,j,peso,c,n;
	for(i=0;i<15;i++)
		for(j=0;j<15;j++)
			m[i][j]=0;		
	for(i=1;i<=15;i++)
		for(j=0;j<i;j++)
		{
			scanf("%d",&peso);
			m[i-1][j]=peso;
		}
	c=mayor(0,0,14,0);
	for(i=1;i<15;i++)
	{
		n=mayor(0,0,14,i);
		if(c<n)
			c=n;
	}
	printf("%d\n",c);
	return 0;
}
