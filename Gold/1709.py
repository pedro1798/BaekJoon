#include <iostream>
#define LL long long

using namespace std;

LL dist(LL x, LL y) {
	return (x * x) + (y * y);
}

int main() {
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
    
	int count;
	LL x, y, n, r, n_d;
	
	cin >> n;
	r = n / 2;  // 반지름 r
	
	x = 0; y = r - 1; count = 0;
	
	while (x <= r && y >= 0) {
		n_d = dist(x + 1, y);
		
		if (n_d <= r * r) x++;
        if (n_d >= r * r) y--;
		count ++;
	}
	printf("%d\n", count * 4);
}
