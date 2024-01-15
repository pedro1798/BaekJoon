#include <iostream>
#define min(a, b) (a) < (b) ? (a) : (b)
using namespace std;

int a, b, c, A, B, C;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int tc, T;
    tc = 1;
    
    while (cin >> T, T) {
        cin >> A >> B >> C;  // 초깃값
        A = 987654321; C += B;
        for (int i = 1; i < T; ++i) {
            cin >> a >> b >> c;
            a += min(A, B);
            b += min(min(min(a, A), B), C);
            c += min(min(b, B), C);
            A = a; B = b; C = c;
        }
        printf("%d. %d\n", tc++, B);
    }
}
