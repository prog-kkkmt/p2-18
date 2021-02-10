function average(a, b:real):real;
begin
  average:= (a + b) / 2;
end;
var
x, y:real;
begin
  readln(x, y);
  writeln(average(x, y));
end.