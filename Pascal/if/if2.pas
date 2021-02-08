var
a:integer;
begin
  readln(a);
  if a > 0 then
    a:= a - 8
  else if a < 0 then
    a:= a + 6
  else
    a:= a + 10;
  writeln(a);
end.