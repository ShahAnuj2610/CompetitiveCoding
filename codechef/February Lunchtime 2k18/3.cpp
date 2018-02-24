#include <bits/stdc++.h>

using namespace std;

int main()
{
    string characters = "abcab";
    int matchCount = 0, prefixIndex = 0;
    int *cumulativeCharMatches = new int[characters.size()];
    for (int i = 0; i < 2; i++)
    {
        if (characters[i] == characters[prefixIndex])
        {
            matchCount += 1;
            prefixIndex += 1;
        }
        else
        {
            matchCount = 0;
            prefixIndex = 0;
        }

        cumulativeCharMatches[i] = matchCount;
    }
    cout << *max_element(cumulativeCharMatches, cumulativeCharMatches + characters.size()) << endl;
    // cout << 2 << endl;
    return 0;
}