#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    //taking input
int a, b;
cin >> a >> b;

    // creating a array of lowercase letter
string numString[] = {"one","two", "three", "four", "five", "six", "seven", "eight", "nine"};

    // creating a for loop and initialize it with a & b
for(int i = a; i <= b; i++) {
            // checking if it's greater than 1 & smaller than 9
    if(i >= 1 && i <= 9) {
                // if yes printing the letter
        cout << numString[i - 1] << endl;
    } else {
                    // if, > 9 then checking it's odd or even
        cout << (i % 2 == 0 ? "even" : "odd") << endl;
    }
}

return 0;
    return 0;
}
