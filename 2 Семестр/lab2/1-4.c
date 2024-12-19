/*
Напишите программу, которая создаёт одномерный динамический
массив из чисел с плавающей точкой двойной точности, заполняет его
значениями с клавиатуры и распечатывает все элементы этого массива,
используя арифметику указателей (оператор +), а не обычный
оператор доступа к элементу массива - [].
*/
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int length;
    printf("Enter length of array: ");
    scanf("%d", &length);

    double *array = (double *)malloc(length * sizeof(int));

    double input;
    for (double *start = array; start < &array[length]; start++)
    {
        printf("[%ld]: ", start - array);
        scanf("%lf", &input);

        *start = input;
    }
    printf("\nArray: [ ");
    for (double *start = array; start < &array[length]; start++)
        printf("%lf, ", *start);
    printf("]\n");

    return 0;
}