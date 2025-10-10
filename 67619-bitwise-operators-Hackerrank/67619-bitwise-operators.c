#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
    
  //Write your code here.
  int numbersToConsider[n];
    //Numbers in answer array will represent biggest and, or, xor in sequence
  int answer[3] = {0, 0, 0};
  
  //Making an array of numbers from 1 to n
  for(int i = 0; i < n; i++){
    numbersToConsider[i] = i+1;
  } 
  
  for(int i = 0; i < numbersToConsider[n-1]; i++){
    for(int j = 1; numbersToConsider[i] + j <= n ; j++){
        int and;
        and = numbersToConsider[i] & numbersToConsider[i+j];
        if(and > answer[0] && and < k){
            answer[0] = and;
        }
        int or;
        or = numbersToConsider[i] | numbersToConsider[i+j];
        if(or > answer[1] && or < k){
            answer[1] = or;
        }
        int xor;
        xor = numbersToConsider[i] ^ numbersToConsider[i+j];
        if(xor > answer[2] && xor < k){
            answer[2] = xor;
        }
    }
  }
  printf("%d\n%d\n%d", answer[0], answer[1], answer[2]);
}
int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}
