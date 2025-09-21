#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n,r=0,s=0;
    scanf("%d", &n);
    while(n!=0){
        r=n%10;
        s=s+r;
        n=n/10;
    }
    printf("%d",s);
    //Complete the code to calculate the sum of the five digits on n.
    return 0;
}
