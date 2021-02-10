var
  a, b, t: real;

begin
  readln(a, b);
  if(a > b) then
  begin
    t := a;
    a := b;
    b := t;
  end;
  writeln(a);
  writeln(b);
end.
