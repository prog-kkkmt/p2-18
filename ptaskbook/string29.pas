{Дан символ C и строки S, S0. Перед каждым вхождением символа C в строку S
вставить строку S0}
var
string1, string2, container:string;
c:char;
i:integer;
begin
  readln(string1);
  readln(string2);
  readln(c);
  for i:= 1 to length(string1) do
    if string1[i] = c then
      container:= container + string2 + c
    else
      container:= container + string1[i];
  writeln(container);
end.