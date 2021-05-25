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

int  compara(string c)
{
	int n[10],i,len,k;
	for(i=0; i<10; i++)
		n[i]=0;
	for(i=0; i<9;i++)
		n[ c[i]- '0' ]=1;
	if(n[1]==1 && n[2]==1 && n[3]==1 && n[4]==1 && n[5]==1 && n[6]==1 && n[7]==1 && n[8]==1 && n[9]==1){
		for(i=0; i<10;i++)
			n[i]=0;
		len=c.length()-1;
		for(i= len,k=0 ; k<9 ; k++ ,len--)
			n[ c[len] -'0' ]=1;
		if(n[1]==1 && n[2]==1 && n[3]==1 && n[4]==1 && n[5]==1 && n[6]==1 && n[7]==1 && n[8]==1 && n[9]==1)
			return 1;
		else return 0;
	}
	else return 0;
}

int main()
{	
	long long  cont=2;
	string fn, f1, f2;
	fn='0';f1='1';f2='1';
	while(fn.length()<10){
		fn=suma(f1,f2);
		cont++;
		f2=f1;f1=fn;
	}
	while(compara(fn)==0){
		fn=suma(f1,f2);
		cont++;
		f2=f1;f1=fn;
	}
	cout << "The first term in the Fibonacci sequence that the first and the last nine digits are 1-9 pandigital is "<< cont << endl; 
	cout << fn << endl;
	return 0;
}
