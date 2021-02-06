#include <iostream>
using namespace std;

int main()
{
    int sum = 0, a = 0;
    cout << "Please input some number" << endl;
    for (; cin >> a;)
    {
        sum += a;
    }

    cout << "sum is" << sum << endl;
    return 0;
}