var
a:integer;
begin
readln(a);
  if(a > 0) then
    a:= a - 8;
  if(a < 0) then
    a:= a + 6;
  if(a = 0) then
    a:= 10;
  writeln(a);
end.