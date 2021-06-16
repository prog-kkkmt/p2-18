#include <iostream>
#include <locale>
#include <stack>

using namespace std;

int main()
{
	setlocale(0,"");
		int n,button;
		stack <int> Stack;
		cin >> n;
		int i;
            for(i=0;i<n;i++)
            {
                cin >> button;
                if(i == 0){
                    Stack.push(button);
                }
                if (i > 0){
                        if ( button > Stack.top()){
                            Stack.push(button);
                        }
                }
            }
            cout << "Размер stack: " << Stack.size();
  return 0;
}
