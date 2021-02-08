function vi(a,b,c:real):real;
begin
  vi:=a * b * c;
end;
function vi_2(a,b,c:real):real;
begin
  vi_2:=2 * (a * b + b * c + a * c);
end;
var
x,y,z:real;
begin
  readln(x,y,z);
  writeln(vi(x,y,z));
  writeln(vi_2(x,y,z));
end.