#include <stdlib.h>
#include <time.h>
#include <stdio.h>

struct myStruct
{
    union myUnion
    {
        int decimal;
        float floating;
    } value;
    enum
    {
        DECIMAL,
        FLOATING
    } type;
};

int main(void)
{
    srandom(time(NULL));
    const int size = 5;
    struct myStruct *array = (struct myStruct *)malloc(sizeof(struct myStruct) * size);

    for (int i = 0; i < size; i++)
    {
        if (random() > RAND_MAX / 2) // 50%
        {
            array[i].type = DECIMAL;
            array[i].value.decimal = random();
        }
        else
        {
            array[i].type = FLOATING;
            array[i].value.floating = (float)RAND_MAX / (float)random();
        }
    }
    for (int i = 0; i < size; i++)
    {
        if (array[i].type == DECIMAL)
            printf("[%d]: %d\n", i, array[i].value.decimal);
        else
            printf("[%d]: %f\n", i, array[i].value.floating);
    }

    free(array);
    return 0;
}