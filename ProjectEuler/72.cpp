#include <cstdio>
#include <bitset>

using namespace std;

#define lli long long int
#define L1 500001
#define L2 1000001

bitset<L2> esprimo;
lli phi[L2 + 1];
lli sol[L2 + 1];

void criba(){
	esprimo.set();
	esprimo.reset(0);
	esprimo.reset(1);
	for(int i=2;i<L2;i++)
		phi[i]=(lli)i;
	for(int i=2;i<L2;i++)
		if( esprimo.test(i) ){
			phi[i]=(lli)i-1;
			for(int j=i+i;j<L2;j+=i){
				esprimo.reset(j);
				phi[j]=(lli)phi[j]/i;
				phi[j]=(lli)phi[j]*(i-1);
			}
		}
}


int main(){
	criba();
	phi[0]=phi[1]=0;
	for(int i=2;i<L2;i++){
		sol[i]=sol[i-1];
		sol[i]+=phi[i];
	}
	printf("el valor de phi[%d] es %lld\n",1000000,sol[1000000]);
	/*for(int i=1;i<10;i++)
		printf("EL valor de phi[%d] es %lld\n", i, phi[i]);*/
	return 0;
}
