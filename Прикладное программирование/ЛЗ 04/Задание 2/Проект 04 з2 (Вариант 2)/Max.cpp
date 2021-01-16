//Функция поиска максимального числа массива
int Max(int array[], int size){
	system("cls");
	int i = 0;
    int Max = array[i];
    for (i = 1; i < size; i++){
        if (array[i] > Max)
            Max = array[i];
	}
    return Max;
}
