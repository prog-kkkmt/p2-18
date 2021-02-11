{Даны целые положительные числа M и N. Сформировать целочисленную
матрицу размера M × N, у которой все элементы J-го столбца имеют
значение 5·J (J = 1, …, N)}
type matrix = array[1..100, 1..100] of integer;
var
a:matrix;
m, n, i, j:integer;
begin
  readln(m);
  readln(n);
  for i:= 1 to m do
    for j:= 1 to n do
      a[i, j]:= 5 * j;
  for i:= 1 to m do
  begin
    for j:= 1 to n do
      write(a[i, j], ' ');
    writeln();
  end;
end.