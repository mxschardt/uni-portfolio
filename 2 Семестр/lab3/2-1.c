#include <stdio.h>

union myUnion
{
    int decimalNumber;
    float floatNumber;
};

int main(void)
{
    union myUnion a;
    union myUnion *b = &a;

    a.decimalNumber = 10;
    printf("before: %d, %f\n", a.decimalNumber, a.floatNumber);

    b->floatNumber = 11.1;
    printf("after: %d, %f\n", b->decimalNumber, b->floatNumber);

    return 0;
}