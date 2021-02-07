{Дано целое число N (> 0). Сформировать и вывести целочисленный массив
размера N, содержащий степени двойки от первой до N-й: 2, 4, 8, 16}
var n,i:integer;
a:array[1..100] of real;
begin
repeat
readln(n);
until n in [1..100];
a[1]:=1;
for i:=2 to n do
 begin
  a[i]:=a[i-1]*2;
  writeln(a[i]:0:0);
 end;
end.