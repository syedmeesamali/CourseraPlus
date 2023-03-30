#include <iostream>
#include <vector>
using std::cin;
using std::cout;


long long CalculateGCD(int a, int b)
{

}

//Main function
int main() {

    //STRESS TEST BELOW WHILE
    /*
    while (true)
    {
        int n = rand() % 10 + 2;
        cout << n << "\n";
        vector<int> a;
        for (int i = 0; i < n; ++i)
        {
            a.push_back(rand() % 10);
        }
        for (int i = 0; i < n; ++i)
        {
            cout << a[i] << ' ';
        }
        cout << "\n";
        long long res1 = MaxPairwiseProduct(a);
        long long res2 = MaxPairwiseProductFast(a);
        if (res1 != res2)
        {
            cout <<"Wrong answer: "<< res1 << ' ' << res2 << "\n";
            break;
        } else
        {
            cout << "OK \n";
        }
    } //END OF STRESS TEST
    */

    //Main original code below
    vector<int> numbers(2);
    for (int i = 0; i < n; ++i)
    {
        cin >> numbers[i];
    }
    long long result = MaxPairwiseProductFast(numbers);
    cout << result << "\n";
    return 0;
}
