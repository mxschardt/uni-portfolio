#include <stdio.h>
#include <math.h>

#define MARS_ORBIT_RADIUS 228
#define EARTH_ORBIT_RADIUS 150
#define MARS_ORBITAL_PERIOD 687
#define EARTH_ORBITAL_PERIOD 365

int main(void)
{
    const float MARS_W = 2 * 3.14 / MARS_ORBITAL_PERIOD;
    const float EARTH_W = 2 * 3.14 / EARTH_ORBITAL_PERIOD;

    for (int time = 0; time < 30; time++)
    {
        float x = MARS_ORBIT_RADIUS * cos(MARS_W * time) - EARTH_ORBIT_RADIUS * cos(EARTH_W * time);
        float y = MARS_ORBIT_RADIUS * sin(MARS_W * time) - EARTH_ORBIT_RADIUS * sin(EARTH_W * time);
        printf("x: %f, y: %f (million km per day)\n", x, y);
    }

    return 0;
}