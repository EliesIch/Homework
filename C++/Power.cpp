#include <iostream>
using namespace std;

double power(double x, int n);


double power(double x, int n){
    double val = 1.0;
    while (n--)
    {
        val *= x;
    }
    return val;
}

int main()
{
    int value = 0;
    cout << "Please enter 8 bit number:";
    for (int i = 7; i >= 0; i--)
    {
        char ch;
        cin >> ch;
        if (ch == '1')
        {
            value += static_cast<int>(power(2, i));
        }
    }

    cout << "value is:" << value << endl;
    return 0;
}