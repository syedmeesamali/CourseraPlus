#include <stdio.h>
#include <stdlib.h>

#define ans 16 //Define constant with name

//Always the main entry point for any program
int main()
{
    int x;
    x = ans;
    do {
        printf("Hello world! {%d}\n", x);
        x -= 1;
    } while (x != 0);

    conditional_1();
    conditional_switch();
}

//Simple conditional function
void conditional_1()
{
    if (ans == 15)
    {
        printf("Ans was defined as 15");
    } else
    {
        printf("Ans was NOT 15\n");
    }
}

//Simple conditional switch
void conditional_switch()
{
    switch(ans)
    {
    case 14:
        printf("Switch 14");
        break;
    case 15:
        printf("Switch 15");
        break;
    default:
        printf("Switch: Not 14 or 15");
        break;
    }
}
