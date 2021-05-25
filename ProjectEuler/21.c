#include <stdio.h>
#include <string.h>

#define max 10001

int sumadiv(int n){
	
	int i, sum=0;
	if(n==0) return -1;
	for(i=1;i<=n/2;i++)
		if(n%i==0)
			sum+=i;
	return sum;
}

int main(){
	int i, j,marca[max], sum, total=0;
	memset(marca,0, sizeof marca);
	for( i=2;i<max;i++){
		if(marca[i]==0){
			sum=0;
			for( j=1;j<=i/2;j++ ){
				if( i%j==0 )
					sum+=j;
			}
			if( sumadiv(sum)==i && sum!=i){
				printf("%d %d\n", i, sum);
				marca[i]=1;
				marca[sum]=1;
				total+=(i+sum);
			}
		}
	}		
	printf(" The sum of all the amicabe numbers under 10000 is %d \n", total);
	return 0;
}


