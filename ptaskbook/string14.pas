{Дана строка. Подсчитать количество содержащихся в ней прописных латинских букв}
var
  s:string;
  i, j, a:integer;
begin
  readln(s);
  for i:= 1 to length(s) do
    if s[i] in ['A'..'Z'] then
      j:= j + 1;
  if j > 0 then writeln(j);
end.