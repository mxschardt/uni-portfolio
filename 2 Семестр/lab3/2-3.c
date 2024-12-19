#include <stdio.h>

int main(void)
{
    enum weekDays
    {
        MONDAY,    // 0
        TUESDAY,   // 1
        WEDNESDAY, // 2
        THURSDAY,  // 3
        FRIDAY,    // 4
        SATURDAY,  // 5
        SUNDAY     // 6
    } day = MONDAY;

    for (int i = 0; i <= 6; i++)
        printf("%d ", day + i);

    printf("\n");
    return 0;
}