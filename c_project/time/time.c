#include <stdio.h>
#include <stdlib.h>
//#include <sys/time.h>
#include <time.h>

void getCurTime(char *time_str, int len)
{
    time_t rawtime;
    struct tm * timeinfo;

    time ( &rawtime );
    timeinfo = localtime ( &rawtime );
    strftime ( time_str,80,"%a %b %d %H:%M:%S %Y",timeinfo);
}

int main()
{
    char time[100] = {0};
    getCurTime(time, 100);
    printf("%s\n", time);
}
