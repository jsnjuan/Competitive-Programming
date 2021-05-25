#include <stdio.h>

int mes[]={31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int leap(int n){
	return n%4==0 && (n%100!=0 || n%400==0) ;
}

int main(){
	int veces[7];
	
	int ndias, i, j;
	for(i=0;i<7;i++)
		veces[i]=0;
	ndias=365;// esto es porque el 1 de enero de 1990 fue monday, asi, como nuestro conteo comienza en 1901, pues basta con sumar los dias que han ocurrido. . . 
	for(i=1;i<=100;i++){
		for(j=0;j<12;j++){
			veces[ndias%7]++;
			ndias+=mes[j];
			if( j==1 && leap(1900 + j) )
			ndias++;
		}
	}
	printf("There were %d sundays that felt on the first of the month during the twentieth century(01/01/1901 --31/12/2000)\n", veces[6]);
	return 0;
}
