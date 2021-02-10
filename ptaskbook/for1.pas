{Даны целые числа K и N (N > 0). Вывести N раз число K}
var k, n, i:integer;
begin
  i:= 0;
  readln(n, k);
  for i:=n downto 1 do
  begin
    writeln(k);
  end;
end.