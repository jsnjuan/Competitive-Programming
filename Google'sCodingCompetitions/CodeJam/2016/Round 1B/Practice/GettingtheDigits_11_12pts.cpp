#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int T, sol, ABC[300], PHONE[15];
int orden_n[] = {0, 2, 4, 6, 8, 1, 3, 5, 7, 9};
char orden_c[] = {'Z','W','U','X','G','O','T','F','S','E'};
string NUMEROS[] ={"ZERO", "ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};

void upd(int digit, int res){
	for( int i=0;i<NUMEROS[digit].length();i++){
		ABC[NUMEROS[digit][i]] -= res;
	}
}

int main(){
	using namespace std;

	//freopen("A-large-practice.in","r", stdin);
	//freopen("A-large-practice.out","w", stdout);
	
	string cad, d;	
	scanf("%d\n", &T);
	for(int i=0;i<T;i++){
		memset(ABC, 0, sizeof (ABC));
		memset(PHONE, 0, sizeof (PHONE));
		getline (cin, cad);
		printf("Case #%d: ", i+1);
		
		for( int j=0;j<cad.length();j++){
			ABC[ cad[j] ]+=1; 
		}
		for (int j=0;j<10;j++){
			if( ABC[ orden_c[ j ] ]!=0 ){
				PHONE[ orden_n[j] ] = ABC[ orden_c[j] ];
				upd(orden_n[j], PHONE[ orden_n[j] ]);
			}
		}


		for(  int j=0;j<10;j++){
			if(PHONE[j]!=0){
				for(int k = 0 ; k<PHONE[j];k++)
					printf("%d", j);
			}
		}
		putchar('\n');
	}
	return 0;
}

