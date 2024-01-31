#include <iostream>
#include <numeric>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

vector<int> visited;
vector<vector<int>> digraph;
unordered_map<int, vector<int>> result;

void dfs(int root) {
    if (!visited[root]) {
        visited[root] = 1;
    }
    for (int next : digraph[root]) {
        if (!visited[next]) {
            dfs(next);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n, m;
    cin >> n >> m;

    digraph.resize(n + 1);

    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        digraph[b].push_back(a);
    }

    int maxCount = 0;

    for (int i = 1; i <= n; ++i) {
        visited.assign(n + 1, 0);
        dfs(i);
        int n_m = accumulate(visited.begin(), visited.end(), 0);
        if (n_m >= maxCount) {
            maxCount = n_m;
            result[maxCount].push_back(i);
        }
    }
    
    sort(result[maxCount].begin(), result[maxCount].end());
	for (int node : result[maxCount]) {
        cout << node << " ";
    }
    return 0;
}