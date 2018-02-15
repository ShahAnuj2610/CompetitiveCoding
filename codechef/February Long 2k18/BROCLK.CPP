#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<ll> vi;
typedef vector<vi> vvi;
const ll mod = 1e9 + 7;

ll power(ll x, ll y)
{
    ll temp;
    if (y <= 0)
        return 1;
    temp = power(x, y / 2) % mod;
    if (y % 2 == 0)
        return (temp * temp) % mod;
    else
        return x * temp % mod * temp % mod;
}

vvi matrixUnit(ll n)
{
    vvi res(n, vi(n));
    for (ll i = 0; i < n; i++)
        res[i][i] = 1;
    return res;
}

vvi matrixAdd(const vvi &a, const vvi &b)
{
    ll n = a.size();
    ll m = a[0].size();
    vvi res(n, vi(m));
    for (ll i = 0; i < n; i++)
        for (ll j = 0; j < m; j++)
            res[i][j] = (a[i][j] + b[i][j]) % mod;
    return res;
}

vvi matrixMul(const vvi &a, const vvi &b)
{
    ll n = a.size();
    ll m = a[0].size();
    ll k = b[0].size();
    vvi res(n, vi(k));
    for (ll i = 0; i < n; i++)
        for (ll j = 0; j < k; j++)
            for (ll p = 0; p < m; p++)
                res[i][j] = (res[i][j] + (ll)a[i][p] * b[p][j]) % mod;
    return res;
}

vvi matrixPow(const vvi &a, ll p)
{
    if (p == 0)
        return matrixUnit(a.size());
    if (p & 1)
        return matrixMul(a, matrixPow(a, p - 1));
    return matrixPow(matrixMul(a, a), p / 2);
}

vvi matrixPowSum(const vvi &a, ll p)
{
    ll n = a.size();
    if (p == 0)
        return vvi(n, vi(n));
    if (p % 2 == 0)
        return matrixMul(matrixPowSum(a, p / 2), matrixAdd(matrixUnit(n), matrixPow(a, p / 2)));
    return matrixAdd(a, matrixMul(matrixPowSum(a, p - 1), a));
}

int main()
{
    ios_base::sync_with_stdio(false);
    ll t, l, d, time;
    cin >> t;
    while (t--)
    {
        cin >> l >> d >> time;
        ll oriL = l;
        vvi a(2, vi(2));
        ll temp = __gcd(d, l);
        d /= temp;
        l /= temp;
        l %= mod;
        d %= mod;
        a[0][0] = (2 * d) % mod;
        a[0][1] = (-l * l) % mod;
        a[1][0] = 1;
        time--;
        vvi b = matrixPow(a, time);
        ll ans = (b[0][0] * d % mod + b[0][1] % mod) % mod;
        ll raisedPower = power(l, time + 1);
        // cout << raisedPower << endl;
        // cout << ans << endl;
        ans = (ans + mod) % mod;
        // cout << raisedPower << " " << ans << endl;
        // cout << power(raisedPower, mod - 2) % mod << endl;
        cout << oriL * ans % mod * power(raisedPower, mod - 2) % mod << endl;
    }
}