#include <iostream>
#include <string>

using namespace std;

string suma(string a, string b)
{
	int l = 1 + (a.length() > b.length() ? a.length() : b.length() );
	string c(l,'0');
	a=string( l - a.length() , '0' ) + a;
	b=string( l - b.length() , '0' ) + b;
	int ac=0, sum=0;
	for(int i= l - 1; i>=0; i--){
		sum = a[i] + b[i] - '0' - '0' +ac;
		c[i] = ( sum % 10 ) + '0';
		ac=sum/10;
	}
	while(c.length() > 0  && c[0]=='0' )
		c.erase( c.begin() );
	return c;
}

int main()
{	
	int cont=2;
	string fn, f1, f2;
	fn='0';f1='1';f2='1';
	while(fn.length()<1000)
	{
		fn=suma(f1,f2);
		cont++;
		f2=f1;f1=fn;
	}
	cout << "The first term in the Fibonacci sequence to contain 1000 digits is "<< cont << endl; 
	return 0;
}
