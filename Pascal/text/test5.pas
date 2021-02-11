// Дана строка S и текстовый файл. Добавить строку S в конец файла.
var
f:text;
s:string;
begin
  assign(f,'test5.txt');
  reset(f);
  while not eof(f) do
  begin
    readln(f,s);
    writeln(s);
  end;
  close(f);
end.