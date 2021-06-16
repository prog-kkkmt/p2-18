#include <iostream>
#include <string>
using namespace std;

class Question{
string question;
string answers[3];

int answer;
int trueAnswer;
bool correctly;
public:
    void isCorrect(){
    if(this->answer == this->trueAnswer){
        this->correctly = true;
    }
    }
};




int main()
{

   cout << "Hello world!" << endl;
    return 0;
}
