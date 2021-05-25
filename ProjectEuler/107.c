/*
peuler107.c
Projecteuler.net

*/

#include <stdio.h>
#include <string.h>
#define MAX 100
#define INF 999999999

/*
Algoritmo de Prim
*/

typedef struct n{
        int id, peso;
        struct n *next;
}nodo;

typedef struct{
        int u, v, w;
}arista;

typedef struct{
        int *p;
        int tope;
}pila;

void ini_pila(pila *pl,int N){
     pl->p=(int*)malloc( (N*N+1)*sizeof(int) );
     
     pl->tope=-1;
}

int pila_empty(pila pl){
    return pl.tope==-1;
}

int top(pila pl){
     return pl.p[ pl.tope ] ;
}

void push(pila *pl, int x){
    pl->p[++(pl->tope)]=x;
}

void pop( pila *pl){
     (pl->tope)--;
}

void ini_grafo(nodo *g,int tam){
     int i;
     for(i=0;i<tam;i++){
         g[i].id=i;
         g[i].peso=INF;
         g[i].next=NULL;
     }
     return ;
}

void inserta_arista( nodo  *g, int u, int v, int peso){
     nodo *p, *q;
     p=(nodo*)malloc( sizeof(nodo) );
     q=(nodo*)malloc( sizeof(nodo) );
     p->id=v; p->peso=peso;     
     q->id=u; q->peso=peso;
     p->next=g[u].next; g[u].next=p;
     q->next=g[v].next; g[v].next=q;
     return ;
}

int*  profundidad( nodo *g, int root, int tam){
      int status[tam], i, N, *parent;
      parent=(int*)malloc( tam*sizeof(int) );
      nodo *temp;
      for(i=0;i<tam;i++){
          status[i]=1;
          parent[i]=-1;
      }
      pila Pila;
      ini_pila(&Pila,tam);
      status[root]=2;
      push(&Pila,root);
      while( !pila_empty(Pila) ){
         N=top(Pila);pop(&Pila);
         status[N]=3;
         temp=g[N].next;
         while( temp!=NULL ){
                if( status[temp->id]==1 ){
                    parent[ temp->id ] = N;
                    push(&Pila,temp->id);
                    status[ temp->id ]=2;    
                }
                temp=temp->next;
         }
      }
    return parent;      
}

/*MERGE SORT*/
void merge(arista *A, int p, int q, int r ){
     int i, j, k, n1 = q - p + 1, n2 = r - q;
     arista L[n1],R[n2];
     for(i=p;i<=q;i++){
              L[i-p].u=A[i].u; 
              L[i-p].v=A[i].v; 
              L[i-p].w=A[i].w;
     }
     for(i=q+1;i<=r;i++){
              R[i-q-1].u=A[i].u;
              R[i-q-1].v=A[i].v;
              R[i-q-1].w=A[i].w;
     }
     i=0;j=0;
     for(k=p;k<=r;k++){
         if( j>=n2 || ( (i<n1) && L[i].w>=R[j].w ) ){
             A[k].u=L[i].u;
             A[k].v=L[i].v;
             A[k].w=L[i++].w;
         }
         else{ 
              A[k].u=R[j].u;
              A[k].v=R[j].v;
              A[k].w=R[j++].w;
         }
     }
     return ;
}

void merge_sort(arista *A,int p,int r){
     int q;
     if( p<r ){
         q=(p+r)/2;
         merge_sort(A,p,q);
         merge_sort(A,q+1,r);
         merge(A, p, q, r);
     }
}
/*******/

void remueve(nodo *T,arista A){
     nodo *t, *ant;
     ant=&T[A.u];
     t=T[A.u].next;
     while( t->id!=A.v ){
            ant=t;
            t=t->next;
     }
     free(t);
     ant->next=t->next;
     ant=&T[A.v];
     t=T[A.v].next;
     while( t->id!=A.u ){
            ant=t;
            t=t->next;
     }
     ant->next=t->next;
     free(t);
}

int desconectado(int *A,int tam ){
    int i, cont=0;
    for(i=0;i<tam;i++)
       if( A[i]==-1 ) cont++;
    return cont!=1;
}

/*El algorimto de Prim retorna el arbol de expansion minimo*/
nodo* Prim(nodo *g, int tam){
     int i, n_aristas=0, *parent;
     nodo *T, *t;
     arista A[MAX*MAX+1];
     T=(nodo*)malloc( tam*sizeof(nodo) );
     ini_grafo(T,tam);
     for(i=0;i<tam;i++){
         t=g[i].next;
             while( t!=NULL ){
                 if( i<(t->id) ){
                    inserta_arista(T,i,t->id,t->peso);
                    A[n_aristas].u=i;
                    A[n_aristas].v=t->id;
                    A[n_aristas].w=t->peso;
                    n_aristas++;
                 }
                 t=t->next;
             }
     }
     merge_sort(A,0,n_aristas-1);
     for( i=0;i<n_aristas;i++ ){
          remueve(T,A[i]);
          parent=profundidad(T,0,tam);
          if( desconectado(parent,tam)==1 )
             inserta_arista(T,A[i].u,A[i].v,A[i].w);
     }
     return T;
}

int main(){
    char buff[10005];
    FILE *fin;
    int i,j,nvert=40, sol, pos, acum,total, t;
    nodo g[nvert], *MST, *temp;
    fin=fopen("network.txt","r");
    ini_grafo(g,nvert);
    for(i=0;i<nvert;i++){
         fgets(buff,10000,fin);
         pos=0;
         for( j=0;j<nvert;j++,pos++){
            if( buff[pos]=='-' )
                pos++;
            else{
                 acum=0;
                 while( buff[pos]!='\n' && buff[pos]!=0 && buff[pos]!=','){
                       acum=acum*10 + (buff[pos]-'0');
                       pos++;
                 }        
                 if( i<j )
                     inserta_arista(g,i,j,acum);
            }
         }
    }
    
    fclose(fin);
    total=0;
    for(i=0;i<nvert;i++){
         temp=g[i].next;
             while( temp!=NULL ){
                  if( i<(temp->id) )  
                      total+=temp->peso;
                  temp=temp->next;
             }
    }
    
    MST=Prim(g,nvert);
    sol=0;
    for(i=0;i<nvert;i++){
         temp=MST[i].next;
             while( temp!=NULL ){
                  if( i<(temp->id) )  
                      sol+=temp->peso;
                  temp=temp->next;
             }
    }
    printf("ARBOL DE EXPANSION MINIMA\nUTILIZANDO EL ALGORITMO DE PRIM.\n\n");
    printf("El peso del arbol es %d\n", total);
    printf("El peso del arbol de expansion minimo es %d\n", sol);
    printf("la solucion es %d\n", total-sol);

    getchar();
    return 0;
}

