#include <iostream>
using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n;
    while (cin >> n, n) {
        int sum = n;
        while (n--)
            sum += n;
        printf("%d\n", sum);
    }
    
    return 0;
}
