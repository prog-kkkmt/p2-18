{Даны целые положительные числа M, N и набор из
M чисел. Сформировать матрицу размера M × N, у которой в каждом
столбце содержатся все числа из исходного набора (в том же порядке)}
type matrix = array[1..100, 1..100] of integer;
var
a:matrix;
m, n, i, j, b:integer;
begin
  readln(m);
  readln(n);
  for i:= 1 to m do
  begin
    readln(b);
    for j:= 1 to n do
      a[i, j]:= b;
  end;
  for i:= 1 to m do
  begin
    for j:= 1 to n do
      write(a[i, j], ' ');
    writeln();
  end;
end.