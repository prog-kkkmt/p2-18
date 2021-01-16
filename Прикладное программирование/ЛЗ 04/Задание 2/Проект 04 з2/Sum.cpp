//Функция суммы чисел массива
int Sum(int array[], int size){
	system("cls");
	int sum = 0;
    for (int i = 0; i < size; i++){
        sum = sum + array[i];
    }
    return sum;
}
