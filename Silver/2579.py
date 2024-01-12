#include <iostream>
#include <string.h>
#include <bitset>
#include <vector>
using namespace std;


int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n;
    cin >> n;
    vector<int> stairs = vector<int>(n, 0);

    for (int i = 0; i < n; ++i) {
        int a;
        cin >> a;
        stairs[i] = a;
    }
    
    if (n == 1) {
        printf("%d\n", stairs[0]);
    } else if (n == 2) {
        printf("%d\n", stairs[0] + stairs[1]);
    } else {
        vector<vector<int>> dp = vector<vector<int>>(n, vector<int>(2, 0));
        
        dp[0][0] = stairs[0];
        dp[1][0] = stairs[1]; dp[1][1] = stairs[0] + stairs[1]; 
		
  		// dp[j][0]은 연속으로 밟을 수 있는 계단, dp[j][1]은 연속으로 밟을 수 없는 계단
        
        for (int j = 2; j < n; ++j) {
            dp[j][0] = max(dp[j-2][0], dp[j-2][1]) + stairs[j];
            dp[j][1] = dp[j-1][0] + stairs[j];
        }
        printf("%d\n", max(dp[n-1][0], dp[n-1][1]));
    }
    
    return 0;
}
