#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    printf("Enter integer: ");
    char input_str[20];
    fscanf(stdin, "%s", input_str);

    double double_input = atof(input_str);
    int integer_input = atoi(input_str);

    printf("Numbers are: %.2lf, %d\n", double_input, integer_input);

    return 0;
}