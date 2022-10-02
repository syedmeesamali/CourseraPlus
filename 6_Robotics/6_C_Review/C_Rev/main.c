#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x;
    x = 10;
    do {
        printf("Hello world!\n");
        x -= 1;
    } while (x != 0);
    getchar();
}
