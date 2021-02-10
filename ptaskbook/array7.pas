{Дан массив размера N. Вывести его элементы в обратном порядке}
var
a:array[1..100] of integer;
n, i:integer;
begin
  writeln('Количество элементов в массиве: '); 
  readln(n);
  for i:= 1 to n do
  begin
    readln(a[i]);
  end;
  for i:= n downto 1 do
    writeln(a[i]); 
end.