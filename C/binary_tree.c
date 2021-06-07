#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
	int value;
	struct node *left;
	struct node *right;
} Node;

Node *tree_insert(Node *root_node, int number)
{
	if (root_node == NULL)
	{
		// typecast "(Node *) para a fun��oo malloc (que retorna um ponteiro void) funcionar para o ponteiro e o tamanho definido pela struct "Node".
		Node *new_node = (Node *)malloc(sizeof(Node)); 
		new_node->value = number;
		new_node->left = NULL;
		new_node->right = NULL;
		root_node = new_node;
	}
	else if (number > root_node->value)
	{ 
	  	//define qual dire��o tomar� o valor inserido em root_node comparado ao valor da raiz do n�.
		root_node->left = tree_insert(root_node->left, number);
	}
	else if (number < root_node->value)
	{
		root_node->right = tree_insert(root_node->right, number);
	}
	return root_node;
}

//Printa o conte�do inserido na �rvore.
void tree_display(Node *root_node)
{ 
	if (root_node != NULL)
	{
		printf("%d ", root_node->value);
		tree_display(root_node->left);
		tree_display(root_node->right);
	}
}

//Para liberar"desalocar" o espa�o da mem�ria do PC.
void tree_free(Node *root_node)
{ 
	if (root_node != NULL)
	{
		tree_free(root_node->left);
		tree_free(root_node->right);
		free(root_node);
	}
}

int main()
{
	int number;
	Node *root = NULL;	  //Inicializa o primeiro n� (raiz) da �rvore com um valor NULO.
	root =	tree_insert(root, 10); 
	root =  tree_insert(root, 15);
	root =	tree_insert(root, 20);
	root = 	tree_insert(root, 12);
	root = 	tree_insert(root, 5);
	tree_display(root);

	printf("\n");
	tree_free(root); //Libera o espa�o alocado na mem�ria.

	return 0;
}
