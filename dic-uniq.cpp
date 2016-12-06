#include <iostream>
#include <string>
#include <set>
using namespace std;

int main(){
	string s;
	set<string> ss;
	
	while(cin>>s){
		if(ss.find(s)==ss.end()){
			cout<<s<<"\n";
			ss.insert(s);
		}
	}
	
	return 0;
}
