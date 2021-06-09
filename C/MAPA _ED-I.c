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
	/*define a distância com base na relação entre os nós.
	
	disntância deve ser com base em cada número do meu RA x 100 (20019623-5).
	
	sendo assim [(1-2)->200,(1-3)->100,(2-4)->900,(2-5)->600,(3-2)->200,(3-5)->300,(4-5)->500].*/
	return edge;
}

//definir mesmo se essa função retorna void
void shortest_distance(){
	/*utilizar a relação entre os nós e suas arestas para testar qual a menor distância, 
	printar todas as sequências de nós e seu valor "peso".
	
	destacar o valor do menor caminho.
	
	definir que sempre se parte do nó 1 e termina-se no nó 5.
	*/
}

int main(){
	
	/*adicionar o RA para o cálculo das arestas*/
	/*iniciar os vértices a serem utilizados*/
	/**/
	
	return 0;
}
