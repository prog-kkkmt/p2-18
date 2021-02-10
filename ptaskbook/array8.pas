{Дан целочисленный массив размера N. Вывести все содержащиеся в данном
массиве нечетные числа в порядке возрастания
их индексов, а также их количество K}
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
  for i:= 1 to n do
    if a[i] mod 2 <> 0 then
      writeln(a[i]); 
end.