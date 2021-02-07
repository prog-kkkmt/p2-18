{Дано целое число N (> 1), а также первый член A и разность D арифметической
прогрессии. Сформировать и вывести массив размера N, содержащий N первых членов
данной прогрессии}
uses crt;
var
a:array[1..100] of integer;
n, i, b:integer;
begin
  textcolor(9);
  readln(n);
  readln(b);
  for i:= 1 to n do
  begin
    readln(a[i]);
    inc(a[i], b);
  end;
  writeln(a);
end.