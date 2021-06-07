#include <stdio.h>
#include <Stdlib.h>
int main() {
	int *p;
	
	int num_1;
	num_1=10;
	
	int num_2;
	num_2=15;
	
	int num_3=20; //posso declarar já atribuindo valor.
	
	printf("num_1: %d\n", num_1);
	printf("num_2: %d\n", num_2);
	printf("num_3: %d\n\n", num_3);
	
	p= &num_1; //endereçando
	*p= num_1; //pegando o valor residente no endereço
	printf("adress num_1: %d\n", p);
	printf("value of num_1: %d\n\n",*p);
	
	p= &num_2; 
	num_2=*p; //posso fazer a atribuição dessa forma também, a ordem aqui não interfere
	
	printf("adress num_2: %d\n", p);
	printf("value of num_2: %d\n\n",*p);
	
	p=&num_3; //basta endereçar com o "&" para a variável desejada que pondo o "*" antes já se obtem o valor atribuido à variável endereçada
	printf("adress num_3: %d\n", p);
	printf("value of num_3: %d\n\n",*p); //puxa diretamente o valor atribuído em num_3
	/* OBS: a seta "->" só pode ser utilizada, caso o ponteiro esteva acessando algum elemento de uma struct*/


	int prime[5]={1,2,3,5,7};
	int i;
	for(i=0;i<5;i++){
		printf("index: %d\t address: %d\t value: %d\n\n",i,prime+i,*(prime+i));
	}

	int marks[5][3] = { { 98, 76, 89},
	                    { 81, 96, 79},
	                    { 88, 86, 89},
	                    { 97, 94, 99},
	                    { 92, 81, 59}
	                  };
                                 
    printf("Value of 0th element of 0th array = %d\n", marks[0][0]);
	printf("Addition of 1 results in %d", marks[0][0] +1);
	
	
	
	return 0;
}
