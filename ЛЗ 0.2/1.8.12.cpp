#include <iostream>

using namespace std;

int main(){
    char c = '\0';
    bool a = true;
    while (cin.get(c)){
        if (c!=' '){
            cout << c;
            a = true;
        }
        else if(a){
            cout << c;
            a = false;
        }
    }
	return 0;
}
