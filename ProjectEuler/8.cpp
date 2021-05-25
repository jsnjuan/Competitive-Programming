#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int main(){
	int tam, maxim=-1, s;
	string cad;
	cin>>cad;
	tam=cad.length();
	for(int i=0;i<tam-4;i++){
		s=(cad[i]-'0')*(cad[i+1]-'0')*(cad[i+2]-'0')*(cad[i+3]-'0')*(cad[i+4]-'0');
		if(s>maxim) maxim=s;
	}
	printf("The maximum  five digit product is %d\n", maxim);

	return 0;
}
