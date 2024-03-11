#include <iostream>
long mod = 1000000007;
long pow(long a, long b)
{
  long r = 1;
  while(b)
  {
    if(b%2)
    {
      r = (r*a)%mod;
    }
    a = (a*a)%mod;
    b >>= 1;
  }
  return r;
}

int main()
{
  long m, res = 0, n, s;
  scanf("%ld", &m);
  while(m--) {
    scanf("%ld %ld", &n, &s);
    res += (s * pow(n, mod-2)) % mod;
  }
  printf("%ld\n", res % mod);
}