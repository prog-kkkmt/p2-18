{Дана строка. Преобразовать в ней все прописные латинские буквы в строчные}
var
string1:string;
i:integer;
begin
  readln(string1);
  for i:= 1 to length(string1) do
    if ord(string1[i]) in [65..90] then
      string1[i]:= chr(ord(string1[i])+32);
  writeln(string1);
end.