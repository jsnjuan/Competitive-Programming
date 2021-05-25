/************************************************/
/*
/*    http://www.freewebs.com/permute/soda_submit.html para ver un algortimo para generar
/*    permutaciones "rapido". . .
/*
/*
/*
/*
/*
/*
/*
/*
/*
/************************************************/
#include <stdio.h>
#include <cstring>
#include <algorithm>
#include <iostream>

using namespace std;

int main(){
    
    freopen("salida.txt", "w", stdout);
    
    string cad="0123456789";
    int cont=0, band=1;
    printf("permutaciones de ");
    cout<< cad <<endl;
    do{
          cont++;
          cout<<cad<<endl;
          if( cont==1000000 ){ cout<< "esta es la elegida "<<endl; band=0; }
          
    }while( band==1 && next_permutation(cad.begin()  ,cad.end() ) );

    return 0;
}
