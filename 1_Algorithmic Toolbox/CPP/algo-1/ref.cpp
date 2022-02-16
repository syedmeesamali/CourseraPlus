#include <iostream>
#include <iomanip>
#include <array>

using namespace std;

int main2()
{
    array<int, 5> n {32, 33, 35, 29, 15};
    for (size_t i{0}; i<n.size(); ++i)
        {
            cout << n.at(i) << "_";
        }
    cout << endl;
    return 0;
}
