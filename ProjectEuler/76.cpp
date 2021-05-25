#include <iostream>
#include <string>

using namespace std;

string suma(string a, string b)
{
	int l = 1 + ( a.length() > b.length() ? a.length() : b.length() );
	string c( l, '0' );
	a = string( l - a.length(), '0' ) + a;
	b = string( l - b.length(), '0' ) + b;
	int ac=0, sum = 0;
	for(int i=l-1; i>=0; i--){
		sum = a[i] + b[i] - '0' - '0' + ac ;
		c[i] = (sum % 10) + '0';
		ac=sum/10;
	}
	while( c.length() > 0 && c[0] == '0' )
		c.erase( c.begin () );
	return c;
	
}

int main()
{
	string  nway[101];
	int i, j, c, coins[100];
	for(i=0;i<100;i++){
		coins[i]=i+1;
		nway[i+1]='0';
	}
	nway[0]='1';
	for(i = 0 ; i < 99 ; i++ ){
		c=coins[i];
		for( j=c ; j<= 100 ; j++ )
			nway[j]=suma(nway[j-c],nway[j]);
	}
	cout << nway[100] << endl;
	return 0;
}
