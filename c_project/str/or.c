/**********************************************************
* File Name: or.c
* Author: Pchwu
* Created Time: 2017年06月22日 星期四 14时45分32秒
********************************************************/

#include<stdio.h>
int main()
{
    int value = 3;
    //int
    printf("%d\n", value | value << 4);
    printf("%d\n", 17 & (value| value << 4));
}
