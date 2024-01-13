#include <iostream>
#include <vector>

using namespace std;

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    
    int n;
    cin >> n;

    vector<int> dp(n + 1, 0);

    for (int i = 2; i < n + 1; ++i) {
        dp[i] = dp[i-1] + 1;
        if (i % 3 == 0) dp[i] = min(dp[i / 3] + 1, dp[i]);
        if (i % 2 == 0) dp[i] = min(dp[i / 2] + 1, dp[i]);
    }
    cout << dp[n] << "\n";
    
    return 0;
}
