#include <stdio.h>
#include <stdlib.h>

int main()
{
    int i = 128;
    float a = 0.0;
    for (i = 1025; i >= 0; i--)
    {
        a *= 10;

    }
    printf("%f\n", a);
}
