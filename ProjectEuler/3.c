#include <stdio.h>
#include <string.h>
#include <math.h>

int main()
{
    int j,primo[47000];
    long long a,num,i;
    memset(primo,0,sizeof(primo));
    for(i=2;i<47000;i++)
    {
        if(primo[i]==0){
          for(j=2*i;j<47000;j+=i)
              primo[j]=1;
                      }
    } 
    while(scanf("%lld",&num)==1 && num!=0)
    {
	a=num;
    	if(num>0)  printf("%lld =",num);
	    else      {printf("%lld = -1",num); num*=-1;}
	    for(i=2;i*i<=num;i++)
	    	{
        		if((!primo[i]) && num%i==0)
        	         {
        		           while(num%i==0)
        	                   {
					if	(a==num)printf(" ");
        	                        else 	printf(" x ");	
       		                   	num=num/i;
        	  	       	   	printf("%lld",i);
				   }
	       		 }
    		}
  	  if(num!=1)
  	  {
		 if(a==num)  printf(" %lld\n",num);
  	         else 	     printf(" x %lld\n",num);
  	  }
  	  else printf("\n");
    }
	return 0;
}
