function sum(a, b, c: real): real;
begin
  sum := a * b * c;
end;

function sum_2(a, b, c: real): real;
begin
  sum_2 := 2 * (a * b + b * c + a * c);
end;

var
  x, y, z: real;

begin
  readln(x, y, z);
  writeln(sum(x, y, z));
  writeln(sum_2(x, y, z));
end.