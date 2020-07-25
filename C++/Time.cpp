#include <iostream>
using namespace std;

struct Mytimestruct
{
    unsigned int year;
    unsigned int month;
    unsigned int day;
    unsigned int hour;
    unsigned int min;
    unsigned int sec;
};
int main()
{
    Mytimestruct mytime = {2019, 3, 2, 14, 30};
    cout << "please input year:" << endl;
    cin >> mytime.year;
    cout << "please input month:" << endl;
    cin >> mytime.month;
    cout << "please input day:" << endl;
    cin >> mytime.day;
    cout << "please input hour:" << endl;
    cin >> mytime.hour;
    cout << "please input min:" << endl;
    cin >> mytime.min;
    cout << "please input sec:" << endl;
    cin >> mytime.sec;

    cout << "time is:" << mytime.year << "/" << mytime.month << "/" << mytime.day << "/" << mytime.hour << ":" << mytime.min << ":" << mytime.sec << endl;

    return (0);
}
