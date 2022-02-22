#include <cstdlib>
#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

//First original version of program
long long MaxPairWiseProduct(const vector<int>& numbers)
{
    long long result = 0;
    int n = numbers.size();
    for (int i=0; i<n; ++i)
    {
        for (int j=i + 1; j<n; ++j)
        {
            if (((long long)numbers[i]) * numbers[j] > result)
            {
                result = ((long long)numbers[i]) * numbers[j];
            }
        }
    }
    return result;
}

//Faster version
long long MaxPairWiseProductFast(const vector<int> &numbers)
{
	int n = numbers.size();
	int max_index1 = -1;
	for (int i=0; i<n; ++i)
	{
		if ((max_index1 == -1) || (numbers[i] > numbers[max_index1]))
		{
			max_index1 = i;
		}
	}
	int max_index2 = -1;
	for (int j=0; j<n; ++j)
	{
		if ((j != max_index1) && ((max_index2 == -1) || (numbers[j] > numbers[max_index2])))
		{
			max_index2 = j;
		}
	}

	cout << max_index1 << ' ' << max_index2 << "\n";
	return ((long long)(numbers[max_index1])) * numbers[max_index2];
}

//Main loop of program
int main()
{
    while(true)
    {
        int n = rand() % 10 + 2;
        cout << n << "\n";
        vector<int> a;
        for (int i=0; i<n; ++i)
        {
            a.push_back(rand() % 10000);
        }
        for (int i=0; i<n; ++i)
        {
            cout << a[i] << ' ';
        }
        cout << "\n";
        long long res1 = MaxPairWiseProduct(a);
        long long res2 = MaxPairWiseProductFast(a);
        if (res1 != res2)
        {
            cout << "Wrong ans!" << res1 << ' ' << res2 << "\n";
            break;
        } else
        {
            cout << "OKAY";
        }

    }

    int n;
    cout << "Total numbers: ";
    cin >> n;
    vector<int> numbers(n);
    for (int i=0; i<n; ++i)
    {
        cin >> numbers[i];
    }
    long long result = MaxPairWiseProduct(numbers);
    cout << "Result: " << result ;
    cout << "\n";
    return 0;
}
