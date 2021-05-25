#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	char cad[100], aux;
	int tam, band=1;
	vector<string> nombres;
	freopen("names.txt","r", stdin);
	scanf("%c", &aux);
	while( scanf("%[^\"]s", cad)==1 ){
		string str="";
		scanf("%c", &aux);
		scanf("%c", &aux);
		scanf("%c", &aux);
		tam=strlen(cad);
		for(int i=0;i<tam;i++)
				str+=cad[i];
		nombres.push_back(str);	
	}
	sort( nombres.begin() , nombres.end() );
	tam=nombres.size();
	long long int suma=0;
	for(int i=1;i<=tam;i++){
		int tot=0;
		for(int k=0;k<nombres[i-1].length();k++)
			tot+=(nombres[i-1][k]-'A' + 1);
		suma+=tot*i;
	}
	printf("La suma total es %d\n",suma);
	return 0;
}

