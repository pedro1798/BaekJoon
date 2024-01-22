#include <iostream>
#include <cmath>
#define min(a, b) (a) < (b) ? (a) : (b)

using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    
    ios_base::sync_with_stdio(false);

    double a, b, c, cmp, l, r, m, h1, h2;
    cin >> a >> b >> c;
    l = 0; r = min(a, b);

    while (r - l >= 0.001) {
        m = (l + r) / 2.0d;
        h1 = sqrt(pow(a, 2) - pow(m, 2));
        h2 = sqrt(pow(b, 2) - pow(m, 2));
        cmp = (h1 * h2) / (h1 + h2);
        if (cmp >= c) l = m;  // m이 커져야 cmp 줄어듦
        else r = m;  // m이 작아져야 cmp 커짐
    }
    cout << fixed;
    cout.precision(3);
    cout << r << "\n";
    
    return 0;
}
