{Даны целые положительные числа M и N. Сформировать целочисленную
матрицу размера M × N, у которой все элементы I-й строки имеют
значение 10·I (I = 1, …, M)}
type matrix = array[1..100, 1..100] of integer;
var
a:matrix;
m, n, i, j:integer;
begin
  readln(m);
  readln(n);
  for i:= 1 to m do
    for j:= 1 to n do
      a[i, j]:= 10 * i;
  for i:= 1 to m do
  begin
    for j:= 1 to n do
      write(a[i, j], ' ');
    writeln();
  end;
end.