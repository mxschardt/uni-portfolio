/*
Напишите программу, которая находит максимальное число из двух
чисел, используя указатели на эти числа.
*/
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *ptr1 = (int *)malloc(sizeof(int));
    int *ptr2 = (int *)malloc(sizeof(int));

    printf("Enter a and b: ");
    scanf("%d", ptr1);
    scanf("%d", ptr2);

    if (*ptr1 > *ptr2)
        printf("a > b\n");
    else
        printf("a < b\n");

    return 0;
}