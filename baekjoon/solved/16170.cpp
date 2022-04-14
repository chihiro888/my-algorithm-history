#include <iostream>
#include <ctime>

using namespace std;

int main() {
    time_t rawtime;
    tm* timeinfo;
    char year[10];
    char month[10];
    char day[10];

    time(&rawtime);
    timeinfo = localtime(&rawtime);

    strftime(year, 10, "%Y", timeinfo);
    strftime(month, 10, "%m", timeinfo);
    strftime(day, 10, "%d", timeinfo);
    
    cout << year << endl;
    cout << month << endl;
    cout << day << endl;
    return 0;
}