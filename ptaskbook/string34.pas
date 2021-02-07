{Даны строки S и S0. Удалить из строки S последнюю подстроку, совпадающую с S0
Если совпадающих подстрок нет, то вывести строку S без изменений}
uses crt;
var
string1, string2:string;
i, n:integer;
begin
  n:= 0;
  textbackground(black);
  clrscr;
  textcolor(9);
  readln(string1);
  readln(string2);
  for i:= length(string1) - length(string2) downto 1 do
    if n = 0 then
      if copy(string1, i, length(string2)) = string2 then
      begin
        delete(string1, i, length(string2));
        inc(n);
      end;
  writeln(string1);
end.