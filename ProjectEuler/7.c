#include <stdio.h>
#include <string.h>

int primo[47000];

int esprimo(int a)
{
	long long  i,band=0;
	for(i=2;(i*i)<=a;i++)
		if(!primo[i] && a%i==0)
			band++;
	if(band==0)	return 1;
	return 0;
}

int main()
{
    int k,j;
    long long cont=0,a,num,i;
    memset(primo,0,sizeof(primo));
    for(i=2;i<47000;i++)
    {
        if(primo[i]==0)
        {
          for(j=2*i;j<47000;j+=i)
              primo[j]=1;
        }
    }
    for(k=2;k<2000000;k++)
    {
	    //if(k>46995)
	    //{
		if(esprimo(k))
			cont++;
		if(cont==10001) break;
    }
    printf("The 10001_st prime %lld.\n",k);
    return 0;
}
