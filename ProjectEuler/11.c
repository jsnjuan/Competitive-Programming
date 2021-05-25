#include <stdio.h>
#include <string.h>


int derecha( int i, int j ){
	return j<=16;
}

int abajo( int i, int j ){
	return i<=16;
}

int diagonal( int i, int j ){
	return i<=16 && j<=16;
}

int ddiagonal( int i, int j ){
	return i<=16 && j>=3;
}

int cderecha(int i, int j, int M[][20]){
	int ii, p=1;
	for( ii=0;ii<4;ii++ ){
		p*=M[i][j+ii];
	}
	return p;
}

int cabajo(int i, int j, int M[][20]){
	int ii, p=1;
	for( ii=0;ii<4;ii++ ){
		p*=M[i+ii][j];
	}
	return p;
}

int cdiagonal(int i, int j, int M[][20]){
	int ii, p=1;
	for( ii=0;ii<4;ii++ ){
		p*=M[i+ii][j+ii];
	}
	return p;
}

int ddiagonal2(int i, int j, int M[][20]){
	int ii, p=1;
	for( ii=0;ii<4;ii++ ){
		p*=M[i+ii][j-ii];
	}
	return p;
}



int main(){
	int M[20][20];
	int i, j, max=0,s;
	FILE *fin=fopen("peuler11.txt","r");
	for(i=0;i<20;i++)
		for(j=0;j<20;j++)
			fscanf(fin,"%d", &M[i][j]);
	fclose(fin);
	
	for(i=0;i<20;i++, putchar('\n'))
		for(j=0;j<20;j++)
			printf("%3d",M[i][j]);
	
	for(i=0;i<20;i++)
		for(j=0;j<20;j++){
			if(derecha(i,j)){
				s=cderecha(i,j,M);
				if( s>max ) max=s;
			}
			if(abajo(i,j)){
				s=cabajo(i,j,M);
				if( s>max ) max=s;	
			}
			if(diagonal(i,j)){
				s=cdiagonal(i,j,M);
				if( s>max ) max=s;
			}
			if(ddiagonal(i,j)){
				s=ddiagonal2(i,j,M);
				if( s>max ) max=s;
			}
		}
	
	printf("LA SOLUCION ES %d\n", max);
	getchar();
	return 0;
	
}
