#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

int main() {
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    int n; i64 k; scanf("%d %lld", &n, &k);
    if ((k + 1) % (1 << n) == 0) printf("Case #%d: %s\n", Ti, "ON");
    else printf("Case #%d: %s\n", Ti, "OFF");
  }
  return 0;
}
