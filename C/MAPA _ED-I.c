#include<stdio.h>
#include<stdlib.h>

typedef struct node{
	int vertice;
	struct node *next;
}Node;

typedef struct adjacent_nodes{
	int vertice;
	Node *adjcent;
	struct adjacent_nodes *next;
}Neighbours;

int edge_value(){
	int edge;
	/*define a dist�ncia com base na rela��o entre os n�s.
	
	disnt�ncia deve ser com base em cada n�mero do meu RA x 100 (20019623-5).
	
	sendo assim [(1-2)->200,(1-3)->100,(2-4)->900,(2-5)->600,(3-2)->200,(3-5)->300,(4-5)->500].*/
	return edge;
}

//definir mesmo se essa fun��o retorna void
void shortest_distance(){
	/*utilizar a rela��o entre os n�s e suas arestas para testar qual a menor dist�ncia, 
	printar todas as sequ�ncias de n�s e seu valor "peso".
	
	destacar o valor do menor caminho.
	
	definir que sempre se parte do n� 1 e termina-se no n� 5.
	*/
}

int main(){
	
	/*adicionar o RA para o c�lculo das arestas*/
	/*iniciar os v�rtices a serem utilizados*/
	/**/
	
	return 0;
}
