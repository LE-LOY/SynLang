//This is not over yet!!!
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
using namespace std;

int main(int argc, char* argv[]){
	string dic_eng = argv[1];
	string dic_syn = argv[2];
	
	ifstream f_eng (dic_eng, in);
	ifstream f_syn (dic_syn, in);
	
	string s;
	vector<string> d_syn[100];
	
	while(f_eng>>s){
		d_syn[s.length()].push_back(s);
	}
	
	return 0;
}
