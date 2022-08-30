#include <iostream>
#include <stdio.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);

    int A, B, N;
    cin>>N>> A>> B;
    cout<<N-A+B;
}