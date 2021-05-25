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
	string  nway[20001];
	int i, j, c, coins[20000], band;
	for(i=0;i<20000;i++){
		coins[i]=i+1;
		nway[i+1]='0';
		
	}
	nway[0]='1';
	for(i = 0 ; i < 20000 ; i++ ){
		c=coins[i];
		for( j = c ; j <= 20000 ; j++ )
			nway[j]=suma(nway[j-c],nway[j]);
	}band=0;
	for(i=1; i<=20000; i++){
		if(nway[i][nway[i].length()-1]=='0' && nway[i][nway[i].length()-2]=='0' && nway[i][nway[i].length()-3]=='0' && nway[i][nway[i].length()-4]=='0' && nway[i][nway[i].length()-5]=='0' && nway[i][nway[i].length()-6]=='0'){
			printf("THE NUMBER n IS %d.\n",i);
			cout << nway[i] << endl;
			band=1; break;
		}
	}
	if(band==0)	printf("SINCE 1 TO 5000 THERE ISN'T A NUMBER THAT IS DIVISIBLE BY ONE MILLION.\n");
	return 0;
}
