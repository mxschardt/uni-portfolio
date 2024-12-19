#include <stdio.h>

struct date
{
    unsigned int day : 5;   // < 32
    unsigned int month : 4; // < 16
    unsigned int year : 12; // < 4096
};

int main(void)
{
    struct date date1 = {02, 02, 2002};
    struct date date2 = {31, 11, 1999};
    struct date date3 = {14, 02, 2011};
    printf("date: %d.%d.%d\n", date1.day, date1.month, date1.year);
    return 0;
}
