#include <iostream>
#include <vector>
#include <set>
using namespace std;

const int INF = 1000000000;
 
int main() {
	int n, s, f;
	cin >> n >> s >> f;
	vector < vector < pair<int,int> > > g (n);
	vector <int> k(n);
	for (int i=0; i<n; i++) {
	    for (auto& a : k) {
		cin >> a;
	    }
	    for (int j=0; j<n; j++) {
		g[i][j] = make_pair(k[j], j);
	    }
	}
 
	vector<int> d (n, INF),  p (n);
	d[s] = 0;
	set < pair<int,int> > q;
	q.insert (make_pair (d[s], s));
	while (!q.empty()) {
		int v = q.begin() -> second;
		q.erase (q.begin());
 
		for (size_t j=0; j < g[v].size(); ++j) {
			int to = g[v][j].first;
			int len = g[v][j].second;
			if (d[v] + len < d[to]) {
				q.erase (make_pair (d[to], to));
				d[to] = d[v] + len;
				p[to] = v;
				q.insert (make_pair (d[to], to));
			}
		}
	}
	cout << d[f] << "\n";
}

