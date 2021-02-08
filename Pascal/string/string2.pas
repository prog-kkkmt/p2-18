{Дана строка. Подсчитать количество содержащихся в ней цифр.}

var
s:string;
i,j,n:integer;
begin
  readln(s);
  for i:=1 to length(s) do
    if s[i] in ['0'..'9'] then
      j:= j + 1;
  if j > 0 then writeln(j);
end.