#include<iostream>
using std::cin;
using std::cout;

int sum_of_two_digits(int a, int b)
{
    return a+b;
}

int main()
{
    int a = 0;
    int b = 0;
    cin >> a;
    cin >> b;
    cout << sum_of_two_digits(a, b);
    return 0;
}
