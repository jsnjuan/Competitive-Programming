#include <stdio.h>
#include <string>
#include <sstream>
#include <iostream>
#include <queue>

using namespace std;

struct p
{
	int x,y;
};
typedef struct p punto;

struct t
{
	long long camino,costo,marca;
};
typedef struct t tipo;

tipo matriz[82][82];

long long minimo(long long a,long long b,long long c,long long d)
{
	long long m=a;
		if(m>b) m=b;
		if(m>c) m=c;
		if(m>d) m=d;
	return m;
}

long long analiza()
{
	punto top,ini,fin,a1,a2,a3,a4;
	ini.x=1;ini.y=1;
	priority_queue <punto> cola;
	cola.push(ini);
	matriz[1][1].marca=1;matriz[1][1].camino=matriz[1][1].costo;
	while(!cola.empty())
	{
		top=cola.pop();
		if(top.x==80 && top.y==80)
			break;
		
		
		
	}
	return matriz[80][80].camino;
		
 	
}

void inicia()
{
	int i,j;
	for(i=0;i<=81;i++)
		for(j=0;j<=81;j++)
		{
			matriz[i][j].marca=0;
			matriz[i][j].costo=-1;
		}
}

/*
void imprime()
{
	int i,j;
	for(i=0;i<=2;i++)
	{
		for(j=0;j<=81;j++)
			printf(" %lld ",matriz[i][j].costo);
		printf("\n");
	}
}*/

int main()
{
	long long n;
	char aux;
	int i,j;
	inicia();
	for(i=1;i<=2;i++)
	{
		for(j=1;j<=80;j++)
		{	
			scanf("%lld%c",&matriz[i][j].costo,&aux);
		}
		//if(aux!=',')scanf("%c",&aux);
	}
	imprime();	
	return 0;
}


