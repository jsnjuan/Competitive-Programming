#include <stdio.h>
long long int potencia(int a,int n)
{
    long long int i,c=1;
    for(i=1;i<=n;i++)
             c=((c*a)%10000000000);       
    return c;
} 

int main()
{
    long long int i,n,s=0;
    for(i=1;i<=1000;i++)
         s=(s+potencia(i,i))%10000000000;
    printf("LOS ULTIMOS DIEZ DIGITOS DE LA SUMA DE 1^1+2^2+...1000^1000 SON %lld.\n",s);
    return 0;
}
