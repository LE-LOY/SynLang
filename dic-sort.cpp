#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
	string s;
	vector<string> vs;
	
	while(cin>>s){
		vs.push_back(s);
	}
	
	sort(vs.begin(), vs.end());
	
	int len = vs.size();
	for(int i=0; i<len; ++i){
		cout<<vs[i]<<"\n";
	}
	
	return 0;
}
