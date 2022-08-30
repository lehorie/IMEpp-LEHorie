#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int a[10];
    for (int i = 0; i < 10; i++)
    {
        cin >> a[i];
    }
    
    sort(a, a+10);
    for (int i = 0; i < 10; i++)
    {
        cout << a[i] << "\n";
    }

    if (binary_search(a , a+10, 7))
    {
        cout << "7 is present in array the array \n";
    } 
}