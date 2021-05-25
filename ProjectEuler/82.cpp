#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <queue>

#define inf 90000000000

using namespace std;

int matriz[7][7]={{inf, inf, inf, inf, inf, inf,inf},
		  {inf,131,673,234,103, 18,inf},
		  {inf,201, 96,342,965,150,inf},
		  {inf,630,803,746,422, 11,inf},
		  {inf,537,699,497,121,956,inf},
		  {inf,805,732,524, 37,331,inf},
		  {inf, inf, inf, inf, inf, inf,inf}};
int dist[7][7];

bool marca[7][7];

void dijkstra()
{	
	pair< int , int > elem(1,1), temp, adj;
	priority_queue< pair< int, int> > cola;
	cola.push(elem);
	dist[1][1]=matriz[1][1];
	while(!cola.empty()){
		temp=cola.top(); cola.pop();
		if( marca[temp.first][temp.second] == false ){
			marca[temp.first][temp.second]=true;
			if( dist[temp.first][temp.second] + matriz[temp.first+1][temp.second] < dist[temp.first+1][temp.second]){
				dist[temp.first+1][temp.second]=dist[temp.first][temp.second] + matriz[temp.first+1][temp.second];
				adj.first=temp.first + 1;adj.second=temp.second;
				
			}	
		}
		
	}	
}

void init()
{
	for(int i=1; i<=5; i++)
		for(int j=1; j<=5;j++){
			marca[i][j]=false;
			dist[i][j]=inf;
		}
	for(int i=0;i<7;i++)
		marca[6][6-i]=marca[6-i][6]=marca[i][0]=marca[0][i]=true;
}

int main()
{
	int i, j;
	init();
	for(i=1;i<=5;i++){
		for(j=1;j<=5;j++)
			printf("%5d",matriz[i][j]);
		printf( "\n" );
	}
	return 0;
}

