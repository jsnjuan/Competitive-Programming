#include <stdio.h>
#include <string>
#include <iostream>

using namespace std;

string suma(string a, string b)
{
	int l = 1 + (a.length() > b.length() ? a.length() : b.length() );
	string c( l , '0' );
	a = string( l - a.length() , '0' ) + a;
	b = string( l - b.length() , '0' ) + b; 
	int ac=0, sum=0;
	for(int i=l-1; i>=0; i--){
		sum= a[i] + b[i] -'0' -'0' + ac;
		c[i]= (sum%10) + '0';
		ac=sum/10;
	}
	while(c.length() > 0 && c[0]== '0' )
	 	c.erase( c.begin() );
	return c;
}

int main()
{
	int i, j,c,coins[]={1,2,5,10,20,50,100,200};
	string nway[201];
	for(i=0;i<200;i++)
		nway[i+1]='0';
	nway[0]='1';
	for( i=0 ; i<8 ; i++ ){
		c=coins[i];
		for(j=c;j<=200;j++)
			nway[j]=suma(nway[j-c],nway[j]);
	}
	printf("The differents ways that we can to repart 200 pounds are ");
	cout << nway[200] << endl;
	return 0;
}
