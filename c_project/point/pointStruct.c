#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct{
    int a;
    int b;
    int c;
}testStruct;

int main()
{
    testStruct * a = (testStruct *) malloc(sizeof(testStruct) * 2);
    printf("[a: %p][b: %p][c: %p][++: %p]\n",
            &a->a, &a->b, &a->c, a+1);
    void *b = malloc(sizeof(testStruct)*2);
    printf("[a: %p][b: %p][c: %p][++: %p]\n",
            &((testStruct *)b)->a, &((testStruct *)b)->b, &((testStruct *)b)->c, b+1);
}
