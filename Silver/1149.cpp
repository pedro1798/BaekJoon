#include <iostream>
#include <vector>
#include <deque>
using namespace std;

int bfs(int n, const vector<vector<int>>& arr){
    vector<vector<int>> dp;
    dp = vector<vector<int>>(n, vector<int>(3, 0));  // x층 각 열에서의 최솟값보다 계산한 값이 크면 가지치기
    dp[0][0] = arr[0][0]; dp[0][1] = arr[0][1]; dp[0][2] = arr[0][2];
    
    deque<vector<int>> q;
    q.push_back(vector<int>{-1, 0, 0});  
    int cur_sum;
    
    while (!q.empty()) {
        int cur_row = q.front()[0];
        int cur_col = q.front()[1];
        int cur_sum = q.front()[2];
        q.pop_front();

        if (cur_row >= n - 1) continue;

        for (int next_col = 0; next_col < 3; ++next_col) {
            int next_sum = cur_sum + arr[cur_row + 1][next_col];
            vector<int> next_node = vector<int>{cur_row + 1, next_col, next_sum};
                
            if (cur_row == -1) {  // cur_row가 0이면 r, g, b 전부 enqueue해야함
                q.push_back(next_node);
            } else { 
                if (next_col == cur_col) continue;  // cur_row가 n (n > 0)일 때 n-1 행의 열과 같은 색 사용 못함
                
                if (!dp[cur_row + 1][next_col]) {  // dp가 초기화 되어 있지 않다면
                    dp[cur_row + 1][next_col] = next_sum;  // dp에 값을 할당한다.
                    q.push_back(next_node);
                } else {
                    if (dp[cur_row + 1][next_col] <= next_sum) continue;
                    else {
                        dp[cur_row + 1][next_col] = next_sum;  //dp가 더 크다면 dp 갱신
                        q.push_back(next_node);
                    }
                }
            }
        }
    }

    printf("%d\n", min(min(dp[n-1][0], dp[n-1][1]), dp[n-1][2]));

    return 0;
}


int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios_base::sync_with_stdio(false);

    int n;
    vector<vector<int>> arr;
    cin >> n;
    
    for (int i = 0; i < n; ++i) {
        int r, g, b;
        cin >> r >> g >> b;
        arr.push_back(vector<int>{r, g, b});
    }

    bfs(n, arr);
    
    return 0;
}
