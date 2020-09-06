/*Case2∞. ƒано целое число K. ¬ывести строку-описание оценки, соответствующей числу K (1 Ч Ђплохої, 2 Ч Ђнеудовлетворительної, 3 Ч Ђудовлетворительної, 4 Ч Ђхорошої, 5 Ч Ђотличної).
 ≈сли K не лежит в диапазоне 1Ц5, то вывести строку Ђошибкаї.
 «адание выполн€ли: Ѕурлаев и ўепкин*/
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    setlocale(0, "");
    int k;
    cout << "k = ";
    cin >> k;
    switch (k)
    {
        case 1:cout<<"плохо";
        break;
        case 2:cout<<"неудовлетворительно";
        break;
        case 3:cout<<"удовлетворительно";
        break;
        case 4:cout<<"хорошо";
        break;
        case 5:cout<<"отлично";
        break;
        default:cout<<"ошибка";
    }
    cout << endl;
}
