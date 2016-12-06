#include <iostream>
#include <string>
#include <utility>
#include <algorithm>
#include <vector>
using namespace std;

bool comp(pair<int, string> &a, pair<int, string> &b){
	return a.first < b.first;
}

int main(){
	vector< pair<int, string> > vis;
	string s;
	
	while(cin>>s){
		vis.push_back( make_pair(s.length(), s) );
	}
	
	sort(vis.begin(), vis.end());
	
	int len = vis.size();
	for(int i=0; i<len; ++i){
		cout<<vis[i].second<<"\n";
	}
	
	return 0;
}
