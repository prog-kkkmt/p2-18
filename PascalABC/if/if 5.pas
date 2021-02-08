var
  a, b, c, k, n: integer;

begin
  readln(a, b, c);
  if a >= 0 then
    k := k + 1;
  if b >= 0 then
    k := k + 1;
  if c >= 0 then
    k := k + 1;
  if a < 0 then
    n := n + 1;
  if b < 0 then
    n := n + 1;
  if c < 0 then
    n := n + 1;
  writeln('Положительных :',k);
  writeln('Отрицательных :',n);
end.
