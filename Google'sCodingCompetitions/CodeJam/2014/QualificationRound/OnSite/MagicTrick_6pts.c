#include <stdio.h>
#include <string.h>

int main(){
     
     freopen("A-small-attempt0.in","r", stdin);
     freopen("salida.txt","w", stdout);
     int i, j, k, sol;
     int T, A[10][10];
     int r1, r2, R1[100], R2[100];
     scanf("%d", &T);
     for( i=1 ; i<=T ; i++ ){
          memset(R1, 0, sizeof R1);
          memset(R2, 0, sizeof R2);
          scanf("%d", &r1);
          for( j=0;j<16;j++ )
               scanf("%d", &A[j/4][j%4]);
          for( j=0;j<4;j++ )
               R1[ A[r1-1][j] ]=1;
          scanf("%d", &r2);
          for( j=0;j<16;j++ )
               scanf("%d", &A[j/4][j%4]);
          for( j=0;j<4;j++ )
               R2[ A[r2-1][j] ]=1;
          sol=0;
          for( j=1;j<=16;j++ )
               sol+=( R1[j]*R2[j] );
          switch( sol ){
               case 0 : printf("Case #%d: Volunteer cheated!\n", i); break;
               case 1 : for( j=1;j<=16;j++ ){
                              if( R1[j]==1 && R2[j]==1 ){
                                   printf("Case #%d: %d\n", i, j); 
                                   break;
                              }
                         }
                         break;
               default : printf("Case #%d: Bad magician!\n", i); break;
          }
     }
     return 0;
}
