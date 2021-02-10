{Даны два целых числа A и B (A < B).
Вывести в порядке возрастания все целые числа, расположенные между
A и B (включая сами числа A и B), а также количество N этих чисел}
var a, b, i, n:integer;
begin
  readln(a, b);
  if a < b then
  begin
    for i:= a to b do
    begin
      writeln(i);
      inc(n);
    end;
  end;
  writeln(n);
end.