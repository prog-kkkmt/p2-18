/* https://stepik.org/lesson/13377/step/7?unit=3571
*/

/*Предположим, что в программе определён макрос sqr.

#define sqr(x) x * x


Какое значение будет иметь следующее выражение?

sqr(3 + 0)
*/

//выражение будет иметь значение 3, чтобы в этом убедитсья напишем программу

#include <iostream>
using namespace std;

#define sqr(x) x * x
int main(){
    cout << sqr(3 + 0);

    return 0;
}
