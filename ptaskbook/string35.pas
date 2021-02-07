{Даны строки S и S0. Удалить из строки S первую подстроку, совпадающую с S0
Если совпадающих подстрок нет, то вывести строку S без изменений}
uses crt;
var
string1, string2:string;
i:integer;
begin
  textbackground(black);
  clrscr;
  textcolor(9);
  readln(string1);
  readln(string2);
  for i:= 1 to length(string1) - length(string2) do
    if copy(string1, i, length(string2)) = string2 then
      delete(string1, i, length(string2));
  writeln(string1);
end.