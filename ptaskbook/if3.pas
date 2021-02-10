var
a, b, c, p, n:integer;
begin
  n:= 3;
  readln(a, b, c);
  if(a >= 0) then
    p:= p + 1;
  if(b >= 0) then
    p:= p + 1;
  if(c >= 0) then
    p:= p + 1;
  n:= n - p;
  writeln('Положительных: ', p);
  writeln('Отрицательных: ', n);
end.