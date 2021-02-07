{Даны строки S, S1 и S2. Заменить в строке S
первое вхождение строки S1 на строку S2}
uses crt;
var
string1, string2, string3, container:string;
i, n, j:integer;
begin
  n:= 0;
  textbackground(black);
  clrscr;
  textcolor(9);
  readln(string1);
  readln(string2);
  readln(string3);
  for i:= 1 to length(string1) do
    if n = 0 then
    begin
      if copy(string1, i, length(string2)) = string2 then
      begin
        writeln(length(container));
        container:= container + string3;
        writeln(length(container));
      end
      else
      begin
        writeln(length(container));
        container:= container + string1[i];
        delete(container, i - length(string2) + 1, length(string2));
      end;
    end;
  writeln(container);
end.

{delete(string1, i, length(string2));}