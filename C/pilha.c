#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 10

typedef struct stack
{
    int values[MAX_SIZE];
    int top;
} stack;

stack my_stack;

void start_stack(stack *pointer)
{
    //a seta significa: acessando a propriedade último da struct p
    pointer->top = -1;
}

void push(stack *pointer, int value)
{
    //criou-se um parâmetro que é um ponteiro para uma stack e o outro é o value para inserção
    //se o valor da ultima posição for igual ao tamnho-1, a stack tá cheia
    if (pointer->top == MAX_SIZE - 1)
    {
        printf("stack FULL!\n");
    }
    else
    {
        pointer->top++;
        pointer->values[pointer->top] = value;
    }
}

int pop(stack *pointer)
{
    if (pointer->top == -1)
    {
        printf("stack EMPTY!\n");
    }
    else
    {
        int value=pointer->values[pointer->top];
        pointer->top--;
        return value;
    }
}

void display(stack *pointer)
{
    int i= pointer->top;
    while (i>=0)
    {
        printf("Value in position %d: %d \n", i, pointer->values[i]);
        i--;
    }
}

int main()
{
    start_stack(&my_stack);
    pop(&my_stack);
    push(&my_stack,5);
    push(&my_stack,10);
   //push(&my_stack,15);
    int value=pop(&my_stack);
    printf("Value popped: %d \n", value);
    display(&my_stack);
    system("pause");
    return 0;
}
