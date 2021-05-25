#include <stdio.h>
#include <cstring>
#include <iostream>

using namespace std;

int cuenta(int n,int m)
{
	int cnt=0;	
	int base=m;
	while(n/base > 0 ){
	cnt+=n/base;
	base*=m;
	}
	return cnt;
}


string borrar_ceros(string a)
{
	int i=0;
	while(a[i]=='0' && i < ( a.size() - 1 ) )
		i++;
	return a.substr(i, a.size() - i );
}

string mult(string a, string b)
{
	int n=a.size(), m=b.size(), t, k, i, j;
	string ans( m + n , '0' );
	for(j=m; j>0; j--){
		for(i=n, k=0 ;i>0; i-- ){
			t=( (a[i-1] - '0')*(b[j-1] - '0') );
			t+=( ans[i+j-1] - '0' )  + k;
			ans[i+j-1]=(t%10) + '0';
			k=t/10;
			}
		ans[j-1]= k +'0';
	}
	return borrar_ceros(ans);
}

int main()
{
	string  ar[]={ "1", "2", "3", "4", "5", "6", "7", "8", "9","10",
		      "11","12","13","14","15","16","17","18","19","20",
		      "21","22","23","24","25","26","27","28","29","30",
		      "31","32","33","34","35","36","37","38","39","40",
		      "41","42","43","44","45","46","47","48","49","50",
		      "51","52","53","54","55","56","57","58","59","60",
		      "61","62","63","64","65","66","67","68","69","70",
		      "71","72","73","74","75","76","77","78","79","80",
		      "81","82","83","84","85","86","87","88","89","90",
		      "91","92","93","94","95","96","97","98","99","100"};
	string res="1";
	int i, cont=0;
	for(i=0;i<100 ;i++)
		res=mult(res,ar[i]);
	for(i=0;i<res.length();i++)
		cont+=res[i] - '0';
	cout << res <<" SUMA DE LOS DIGITOS = "<<cont << endl; 	
	return 0;
}

