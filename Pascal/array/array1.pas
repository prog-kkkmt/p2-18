// Дано целое число N (> 0). Сформировать и вывести целочисленный массив 
// размера N, содержащий N первых положительных нечетных чисел: 1, 3, 5, … .
var
a:array[1..100] of integer;
n,i:integer;
begin
  readln(n);
  a[1]:=-1;
  for i:=2 to n do
  begin
    a[i]:=a[i-1]+2;
    writeln(a[i]);
  end;
end.