#include <iostream>
#include <cstdio>
using namespace std;

// Implement the function to return the maximum of four integers
int max_of_four(int a, int b, int c, int d) {
    int max1 = (a > b) ? a : b;
    int max2 = (c > d) ? c : d;
    return (max1 > max2) ? max1 : max2;
}

int main() {
    int a, b, c, d;
    // The input format in the prompt suggests four integers, one per line or space-separated
    // Using scanf to be consistent with the sample
    scanf("%d %d %d %d", &a, &b, &c, &d);
    int ans = max_of_four(a, b, c, d);
    printf("%d", ans);
    
    return 0;
}
