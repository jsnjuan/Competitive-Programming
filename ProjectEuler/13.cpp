#include <stdio.h>
#include <iostream>
#include <string>

using namespace std;

string suma(string a, string b)
{
	int l = 1 + (a.length() > b.length() ? a.length() : b.length() ), ac=0, sum=0, i;
	string c(l,'0');
	a=string(l- a.length(), '0' ) + a;
	b=string(l- b.length(), '0' ) + b;
	for(i=l-1; i>=0;i--){
		sum= a[i] + b[i] - '0' - '0' + ac;
		c[i]=( sum%10 ) + '0';
		ac=sum/10;
	}
	while(c.length() > 0 && c[0] == '0' )
		c.erase ( c.begin() );
	return  c;
}

int main()
{
	string a,b;
	b='0';
	while(getline(cin,a))
		b=suma(a,b);
	cout << "THE FIRST TEN DIGITS ARE: " << endl ;
	for(int i=0;i < 10 ; i++ )
		cout << b[i] ;
	cout << endl;
	return 0;
}
