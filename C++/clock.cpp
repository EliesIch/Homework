#include <iostream>
using namespace std;
class clock
{
public:
    clock(int newH, int newM, int newS);
    void settime(int newH = 0, int newM = 0, int newS = 0);
    void showtime();

private:
    int hour = 0, minute = 0, second = 0;
};
clock::clock(int newH, int newM, int newS) : hour(newH), minute(newM), second(newS) {}
void clock::settime(int newH, int newM, int newS)
{
    hour = newH;
    minute = newM;
    second = newS;
}
void clock::showtime()
{
    cout << hour << ":" << minute << ":" << second << endl;
}

int main()
{

    clock myclock(0,0,0);
    myclock.settime(9, 10, 30);
    myclock.showtime();
    return 0;
}