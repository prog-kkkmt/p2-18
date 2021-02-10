{Дано целое число N (> 1), а также первый член A и разность D арифметической
прогрессии. Сформировать и вывести массив размера N, содержащий N первых членов
данной прогрессии: A,    A + D,    A + 2·D,    A + 3·D,    … .}
var
a:array[1..100] of integer;
n, i, b:integer;
begin
  writeln('Разность арифм. прогрессии: '); 
  readln(b);
  writeln('Количество элементов в массиве: '); 
  readln(n);
  for i:= 1 to n do
  begin
    readln(a[i]);
    dec(a[i], b);
  end;
  for i:= 1 to n do
    writeln(a[i]); 
end.