// Formatted code with proper identation
// Fuck codechef (same code didn't work in python)
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t;
    string s;
    cin >> t;
    while (t--)
    {
        cin >> s;
        map<char, int> count;
        map<char, vector<int>> pos;
        int ans[s.size()];
        int odd = 0;
        char index = NULL;
        map<char, int>::iterator iter;
        for (int i = 0; i < s.size(); i++)
        {
            pos[s[i]].push_back(i + 1);
            count[s[i]]++;
        }
        for (iter = count.begin(); iter != count.end(); iter++)
        {
            if ((iter->second) % 2)
                odd++;
        }
        if (odd > 1)
            cout << -1;
        else
        {
            int start = 0;
            int end = s.size() - 1;
            for (iter = count.begin(); iter != count.end(); iter++)
            {
                if (!(iter->second % 2))
                {
                    for (int i = 0; i < (iter->second) / 2; i++)
                    {
                        ans[start] = pos[iter->first].back();
                        pos[iter->first].pop_back();
                        ans[end] = pos[iter->first].back();
                        pos[iter->first].pop_back();
                        start++;
                        end--;
                    }
                }
                else
                    index = iter->first;
            }
            if (index != NULL)
            {
                for (int i = 0; i < (count[index] - 1) / 2; i++)
                {
                    ans[start] = pos[index].back();
                    pos[index].pop_back();
                    ans[end] = pos[index].back();
                    pos[index].pop_back();
                    start++;
                    end--;
                }
                ans[start] = pos[index].back();
            }
            for (int i = 0; i < s.size(); i++)
                cout << ans[i] << " ";
        }
        cout << endl;
    }
    return 0;
}