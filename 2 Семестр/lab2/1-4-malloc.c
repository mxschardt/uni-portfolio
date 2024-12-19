#include <stdio.h>
#include <stdlib.h>
/*
Напишите программу, которая создаёт одномерный динамический
массив из чисел с плавающей точкой двойной точности, заполняет его
значениями с клавиатуры и распечатывает все элементы этого массива, 
используя арифметику указателей (оператор +), а не обычный
оператор доступа к элементу массива - [].
*/

// Память под массив выделяется с помощью malloc.
int main(void)
{
    int length;
    printf("Enter length of array: ");
    scanf("%d", &length);

    if (length <= 0)
        return -1;

    double *array = (double *)malloc(length * sizeof(double));
    double *array_end = array + length * sizeof(double);

    double input;
    for (double *start = array; start <= array_end; start += sizeof(double))
    {
        printf("array[%d]: ", (int)((start - array) / sizeof(double)));
        scanf("%lf", &input);

        *start = input;
    }
    printf("Array: ");
    for (double *start = array; start <= array_end; start += sizeof(double))
        printf("%lf ", *start);
    free(array);
    return 0;
}