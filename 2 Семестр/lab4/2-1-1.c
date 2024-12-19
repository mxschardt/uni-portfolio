#define MY_SIZE 12
#include <stdio.h>

int main(void)
{
    char my_string[MY_SIZE];
    fscanf(stdin, "%s", my_string);

    int string_size = 0;
    for (int i = 0; my_string[i]; i++)
    {
        string_size = i;
    }
}