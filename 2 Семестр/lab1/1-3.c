#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void)
{
    double x, y;
    double result, denominator, divider;

    printf("Input x and y: ");
    scanf("%lf%lf", &x, &y);

    denominator = 1 + sin(x + y) * sin(x + y);
    divider = 2 + abs((x - (2 * x * x) / (1 + abs(sin(x + y)))));
    result = denominator / divider;

    printf("Result: %lf\n", result);

    return 0;
}