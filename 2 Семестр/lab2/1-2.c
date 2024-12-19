/*
Напишите программу, которая складывает два числа с использованием указателей на эти числа.
*/
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *pointer1 = (int *)malloc(sizeof(int));
    int *pointer2 = (int *)malloc(sizeof(int));
    *pointer1 = 2;
    *pointer2 = 4;

    printf("Value: %d\n", *pointer1 + *pointer2);

    return 0;
}