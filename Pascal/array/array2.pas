{ Дано целое число N (> 0). Сформировать и вывести целочисленный массив размера 
N, содержащий степени двойки от первой до N-й: 2, 4, 8, 16, … .}
var
a:array[1..100] of integer;
n,i:integer;
begin
  readln(n);
  a[1]:=0;
  for i:=2 to n do
  begin
    a[i]:=a[i-1]+2;
    writeln(a[i]);
  end;
end.