{Дано имя файла и целые положительные числа N и K.
Создать текстовый файл с указанным именем и записать в него N строк,
каждая из которых состоит из K символов «*» (звездочка)}
var
f:text;
a, b, i, n, k:integer;
s:string;
begin
  assign(f, 'test.txt');
  rewrite(f);
  readln(n);
  readln(k);
  for a:= 1 to k do
    s:= s + '*';
  for i:= 1 to n do
  begin
    writeln(f, s);
  end;
  close(f);
end.