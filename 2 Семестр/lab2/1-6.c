/*
Определите переменную целого типа int a = 1234567890; и выведите побайтово её содержимое на экран, используя указатель char ∗.
*/
#include <stdio.h>

int main(void)
{
    int a = 1234567890;

    for (char *start = (char *)&a; start < (char *)&a + sizeof(int); start++)
        printf("%hhx ", *start);
    printf("\n");
    return 0;
}