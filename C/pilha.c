#include <stdio.h>
#include <stdlib.h>

#define tam 10

typedef struct pilha{
    int dado[tam];
    int primeiro;
    int ultimo;
    }pilha;

pilha p;
void PUSH(int elemento){

}
void POP(){
    p.dado[p.ultimo]=0;
    p.ultimo--;
}
void DISPLAY(){

}
int main(){

    return 0;
}

/*FIXME
adicionar a função PUSH
adicionar a função DISPLAY
adicionar o main*/