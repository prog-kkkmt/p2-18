function sum(a,b:real):real;
begin
  sum:=a * b;
end;
function sum_2(a,b:real):real;
begin
  sum_2:=2 * (a + b);
end;
var
x,y:real;
begin
  readln(x,y);
  writeln(sum(x,y));
  writeln(sum_2(x,y));
end.