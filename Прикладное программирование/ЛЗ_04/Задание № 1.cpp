//https://stepik.org/lesson/Указатели-и-массивы-539/step/9?unit=862
//Выполнил Щепкин М.В
/*В этой задаче вам нужно реализовать функцию, которая сдвигает содержимое массива влево на заданное число позиций (циклический сдвиг).
На вход функция принимает массив, его размер и величину сдвига. 
Например, если на вход функции подан массив: int a[] = { 1, 2, 3, 4, 5 }; и требуется циклически сдвинуть его влево на 2 позиции, 
то на выходе мы получим числа в таком порядке: 3, 4, 5, 1, 2.
Обратите внимание, что величина сдвига может быть нулевой, а может быть и больше размера массива, все эти случаи нужно учесть.*/

void rotate(int a[], unsigned size, int shift)
{
    while(shift! = 0)
    {
        int temp=a[0];
        for(int i = 1;i < size;i++)
        {
            a[i-1] = a[i];
        }
            a[size-1] = temp;shift--;
    } 
return;
}
