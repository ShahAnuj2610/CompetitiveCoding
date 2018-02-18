#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, k, b;
    cin >> t;
    while (t--)
    {
        cin >> n >> k >> b;
        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];
        sort(a, a + n);
        int curr = 0;
        int next = 1;
        int count = 1;
        while (next < n)
        {
            if (a[curr] * k + b <= a[next])
            {
                curr++;
                next++;
                count++;
            }
            else
                next++;
        }
        cout << count << endl;
    }
    return 0;
}