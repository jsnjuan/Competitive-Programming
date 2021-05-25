#include <cstdio>
#include <bitset>
#include <stdlib.h>

using namespace std;

#define lli long long int
#define L1 1001
#define L2 1000001

bitset<L2> esprimo;
int phi[L2];

void criba(){
	 esprimo.set();
	 esprimo.reset(0);
	 esprimo.reset(1);
	 phi[0]=phi[1]=1;
	 for(int i=2;i<L2;i++)
	         phi[i]=i;
	 for(int i=2;i<L2;i++)
	         if(esprimo.test(i)){
				  phi[i]=i-1;
				  for(int j=i+i;j<L2;j+=i){
				          esprimo.reset(j);
				          phi[j]/=i;
				          phi[j]*=(i-1);
				  }
			 }
}

int main(){
	int value=0;
	double maxim=0.0;
	criba();
	for(int i=1;i<L2;i++){
			if( (double)i/(double)phi[i] > maxim ){
			    value=i;
			    maxim=(double)i/(double)phi[i];
			}
	}
	printf("The value that n/phi[n] is maximum below 1,000,000 is %d\n", value);
	getchar();
	return 0;
}
