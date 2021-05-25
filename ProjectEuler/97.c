#include <stdio.h>
#include <stdlib.h>

int main()
{
	long long  s=1,i,n,a,b,c;
	for(i=1;i<=7830457;i++)
	{
		s=((s%10000000000)*2)%10000000000;
		//printf("THE POWER IS %lld, THE NUMBER IS %lld.\n",i,s);
		//getchar();
	}
	s=(s*28433+1)%10000000000;
	printf("THE LAST TEN DIGITS OF THIS NON MERSENNE PRIME 28433*(2^7830457)+1 ARE: %lld.\n",s);
	return 0;
}
