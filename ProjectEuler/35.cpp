#include <stdio.h>
#include <bitset>
#include <cstring>
#include <map>

using namespace std;

#define L1 1001
#define L2 1000001
			 
bitset <L2> esprimo;

int sol[L2];


void criba(){
     esprimo.set();
     esprimo.reset(0);
     esprimo.reset(1);
     for (int i=2; i<L1; i++){
         if ( esprimo.test(i) ){
            for (int j=i+i; j<L2; j+=i)
                esprimo.reset(j);
         }
     }
}


int  ndigits(int  n)
{
	int  cont=0;
	while(n>0){
		cont++;
		n/=10;
	}
	return cont;
}


int circular(int n){
	int temp, pot, i;
	temp = n%10;
	n/=10;
	pot = ndigits(n);
	for(i=0;i<pot;i++)
		temp*=10;
	return n + temp;
}


int main()
{
	int ncases, nd, i, j;
	int a, b, band, s, t;
	criba();
	for(int i=100;i<L2;i++){
		sol[i]=sol[i-1];
		nd=ndigits(i);
		band=1;t=i;
		for(j=0;j<nd && band;j++){
			if( !esprimo.test(t) )
				band=0;
			t=circular(t);
		}
		sol[i] +=band;
	}
	while( scanf("%d%d", &a, &b)==2  && a!=-1){
			s = sol[b] - sol[a];
			nd=ndigits(a);
			band=1;
			for(i=0;i<nd && band;i++){
				if( !esprimo.test(a) )
					band=0;
				a=circular(a);
			}
			s+=band;
			if(s==0) printf("No Circular Primes.\n");
			else if(s==1) printf("1 Circular Prime.\n");
					else printf("%d Circular Primes.\n", s);			
			
	}
	return 0;
}
