//Дана непустая строка S и целое число N (>0). Вывести строку, содержащую символы строки S, между которыми вставлено по N символов <*>

#include <iostream>
#include <string>

using namespace std;

main(){
    int i,n;
    string S;
        getline(cin,S);
        cin >> n;
        string N(n, '*');
    for(i=0;i<S.size();i++){
        cout << S[i] << N;
    }
    cout << endl;
}
