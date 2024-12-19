#include <math.h>
#include <stdio.h>

struct vector
{
    int x;
    int y;
    int z;
    char name[20];
};

int main(void)
{
    struct vector a = {-1, 2, -3, "first"};
    struct vector b = {0, -4, 1, "second"};
    // Модуль вектора
    double a_length = sqrt(a.x * a.x + a.y * a.y + a.z * a.z);
    // Скалярное умножение
    int dot_product = a.x * b.x + a.y * b.y + a.z * b.z;
    // Векторное умножение
    struct vector cross_product;
    cross_product.x = a.z * b.y - a.y * b.z
    ;
    cross_product.y = a.x * b.z - a.z * b.x;
    cross_product.z = a.x * b.y - a.y * b.x;
    // Вывод вектора
    printf("%s {%d, %d, %d}\n", a.name, a.x, a.y, a.z);
    printf("%s {%d, %d, %d}\n", b.name, b.x, b.y, b.z);

    printf("Dot product: %d\n", dot_product);
    printf("Cross product: {%d, %d, %d}\n", b.x, b.y, b.z);

    return 0;
}