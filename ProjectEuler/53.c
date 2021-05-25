#include <stdio.h>

#define MAX 100

int main(){
	int i, j, band=1, cont;
	int C[MAX +1 ][MAX + 1];
	C[1][1]=1;
	for( i=0;i<=MAX;i++ )
		C[i][0]=0;
	for( i=0;i<MAX;i++ )
		C[i][i+1]=0;
	for( i=2;i<=MAX;i++ )
		for( j=1;j<=i;j++ )
			C[i][j]=-1;
	
	for( i=2;i<=MAX && band;i++ ){
		for( j=1;j<=i;j++ )
			C[i][j]=C[i-1][j-1]+C[i-1][j];
		cont=0;	
		for(j=1;j<=i;j++)
			if( C[i][j]>1000000 ) cont++;
		if( cont==i ) band
	}
	
	for( i=1;i<=MAX;i++,putchar('\n') )
		for( j=1;j<=i;j++ )
			printf("%5d",C[i][j]);
			
	getchar();
	return 0;
	
}
