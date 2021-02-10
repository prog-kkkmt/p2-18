function c(a, b:real):real;
begin
  c:= sqrt(sqr(a) + sqr(b));
end;
var
x, y:real;
begin
  readln(x, y);
  writeln('c = ', c(x, y));
  writeln('p = ', x + y + c(x, y));
end.