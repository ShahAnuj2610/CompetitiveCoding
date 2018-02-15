#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, c, d, s;
    cin >> t;
    while (t--)
    {
        cin >> n;
        int a[n];
        priority_queue<double, vector<double>, greater<double>> heapTime;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        cin >> c >> d >> s;
        double toInc = (1.0 * d) / s;
        double var = 0;
        for (int i = 0; i < n; i++)
        {
            heapTime.push(a[i] + var);
            var += toInc;
        }
        for (int i = 0; i < c; i++)
        {
            double temp = heapTime.top();
            heapTime.pop();
            temp *= 2;
            heapTime.push(temp);
        }
        double ans = INT_MIN;
        while (!heapTime.empty())
        {
            ans = max(ans, heapTime.top());
            heapTime.pop();
        }
        cout.precision(10);
        cout << ans / 2 << endl;
    }
    return 0;
}