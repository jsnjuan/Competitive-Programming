#include <cstdio>
#include <bitset>
#include <vector> 
#include <map>

using namespace std;

#define L1 1001
#define L2 1000001

bitset<L2> esprimo;
vector<int> primo;

void criba(){
	esprimo.set();
	esprimo.reset(0);
	esprimo.reset(1);
	for(int i=2;i<L1;i++)
		if( esprimo.test(i) ){
			primo.push_back(i);
			for(int j= i+i;j<L2;j+=i)
				esprimo.reset(j);
		}
}

void factoriza(long long n,map<int, char> &f){
	int i=0;
	if(n==1){
		f[1]++;
		return ;
	}
	while(n>1 && i<primo.size() ){
		while( !( n%primo[i] ) ){
			f[primo[i]]++;
			n/=primo[i];
		}
		i++;
	}
	if(n>1) f[n]++;
}


int divisors(long long nt){
	int nd=1;
	map<int, char> f;	
	factoriza(nt, f);
	map<int, char> :: iterator  ini=f.begin();
	map<int, char> :: iterator  end=f.end();
	while(ini!=end){
		nd*=(ini->second + 1);
		ini++;
	}
	return nd;
}


int main(){
	long long t=7, nt;
	int b=1;
	criba();
	
	while(b){
		nt=t*(t+1)/2;
		t++;
		if( divisors(nt) > 500 )
			b=0;
	}	
	printf("The first triangular number to have over five hundred divisors is %lld\n", nt);
	
	return 0;
}

