#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main(void)
{
    int a, b;
    scanf("%d\n%d", &a ,&b);
    const char *nbword[10] = {"zero", "one", "two", "three", "four" ,"five", "six", "seven" ,"eight", "nine"};
    
    int i = a;
    while (i <= b)
    {
        if (i >= 1 && i <= 9)
            printf("%s\n", nbword[i]);
        else 
        {
            if (!(i % 2 == 0))
                printf("odd\n");
            else
                printf("even\n");
        }
        i++;
    }
}
