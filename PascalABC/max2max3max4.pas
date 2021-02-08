function max2(a, b: real): real;
begin
  if a > b then
    max2 := a
  else
    max2 := b;
end;

function max3(a, b, c: real): real;
begin
  max3 := max2(max2(a, b), c);
end;

function max4(a, b, c, d: real): real;
begin
  max4 := max2(max2(a,b),max2(c,d));
end;

var
  x, y, z, u: real;

begin
  readln(x, y, z, u);
  writeln(max2(x, y));
  writeln(max3(x, y, z));
  writeln(max4(x, y, z, u));
end.