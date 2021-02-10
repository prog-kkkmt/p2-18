{Даны два целых числа A и B (A < B).
Найти произведение всех целых чисел от A до B включительно}
var a, b, i, n:integer;
begin
  n:= 1;
  readln(a, b);
  if a < b then
  begin
    for i:= a to b do
      n:= n * i;
  end;
  writeln(n);
end.