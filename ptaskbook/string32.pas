{Даны строки S и S0. Найти количество вхождений строки S0 в строку S}
uses crt;
var
string1, string2:string;
i, n, j:integer;
begin
  textbackground(black);
  clrscr;
  textcolor(3);
  readln(string1);
  readln(string2);
  for i:= 1 to length(string1) do
    if copy(string1, i, length(string2)) = string2 then
      inc(n);
  writeln(n);
end.