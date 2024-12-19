#include <stdio.h>

int main(void)
{
    int input1, input2;
    printf("Input 2 numbers: \n");
    scanf("%i", &input1);
    scanf("%i", &input2);
    printf("Sum of your numbers is: %d\n", input1 + input2);

    return 0;
}