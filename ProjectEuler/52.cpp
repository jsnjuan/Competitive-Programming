#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> cuenta(int n){
	vector<int> vec;
	while(n>0){
		vec.push_back(n%10);
		n/=10;
	}
	sort(vec.begin(), vec.end());
	return vec;
}

int igual(vector<int> v1, vector<int> v2){
	int t1=v1.size(), t2=v2.size();
	if(t1!=t2) return 0;
	for(int i=0;i<t1;i++)
		if(v1[i]!=v2[i]) return 0;
	return 1;
}


int main(){
	int bn=1;
	int n=10;
	vector<int> x;
	while(bn){
		int cont=0;
			x=cuenta(n);
		for(int i=0;i<5;i++){
			vector<int> nx=cuenta( (i+2)*n );
			if(igual(x,nx)) cont++;
		}
		if(cont==5) break;
		n++;
	}
	printf("The number is %lld\n", n);
	return 0;
}

