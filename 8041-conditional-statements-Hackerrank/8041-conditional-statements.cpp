#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long n=0;
    cin>>n;
    string number[]={"one","two","three","four","five","six","seven","eight","nine"};
    if (n<=9){cout<<number[n-1];} else cout<<"Greater than 9";
}
