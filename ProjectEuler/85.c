#include <stdio.h>

#define lli long long int

int main(){
     lli i, j, s, aux, sol=0,minim=999999;
     for( i=1;i<=4000;i++ )
		for( j=1;j<=4000;j++ ){
			s=i*j*(i+1)*(j+1);
			aux=8000000-s;
			if( aux>0  && aux<minim ){
				minim=aux;
				sol=i*j;
			}	
		}		
     printf(" LA SOLUCION ES %d\n ", sol);
     getchar();
     return 0;
}
