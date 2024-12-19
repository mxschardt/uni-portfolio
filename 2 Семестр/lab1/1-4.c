#include <stdio.h>
#include <math.h>

int main(void)
{
    // float a = 0.12, b = 3.5, c = 2.4, x = 1.4;
    // float a = 0.12, b = 3.5, c = 2.4, x = 1.6;
    float a = 0.27, b = 3.9, c = 2.8, x = 1.8;

    float result, denominator, divider;

    denominator = x - a;
    divider = pow((x * x + a * a), -3);
    result = -denominator / divider;

    denominator = 4 * pow(pow((x * x + b * b), 3), -4);
    divider = 2 + a + b + c + pow((x - c) * (x - c), -3);

    result = result - denominator / divider;

    printf("%s %f\n", "Result:", result);

    return 0;
}
