#include <iostream>

using namespace std;

int main()
{
//Дано целое число N и набор из N чисел. Найти минимальный и максимальный из элементов данного набора и вывести их в указанном порядке.
    int n;
    cin >> n;//размер массива
    int arr[n];

      for(int i = 0; i < n; ++i){//заполняем массив
        cin >> arr[i];
      }
        int min = arr[0], max = arr[0];// даем им изначальные данные(первые в списке)
      for(int i = 0; i < n; ++i){
          if(min > arr[i]){ //находим минимальное
              min = arr[i];
          }
          if(max < arr[i]){// находим максимальное
              max = arr[i];
          }
      }
      cout << "max = " <<  max << " min = " <<  min; // вывод
    }

