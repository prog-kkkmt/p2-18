{Даны два целых числа A и B (A < B).
Вывести в порядке убывания все целые числа, расположенные между A и B
(не включая числа A и B), а также количество N этих чисел}
var a, b, i, n:integer;
begin
  readln(a, b);
  if a < b then
  begin
    inc(a);
    dec(b);
    for i:= b downto a do
    begin
      writeln(i);
      inc(n);
    end;
  end;
  writeln(n);
end.