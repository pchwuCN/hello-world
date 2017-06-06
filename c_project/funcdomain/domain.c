#include <stdio.h>
#define func(aa) (printf("start func.\n")|(aa>0)?2:printf("heiheihei\n"))
#define funa(aa) do {\
aa+=2;               \
} while(0)
int main()
{
    int a = 1;
    int b = 0;
    printf("--------------\n");
    a= func(1);
    printf("a = %d\n", a);
    funa(a);
    printf("a = %d\n", a=134);
    return 1;
}
