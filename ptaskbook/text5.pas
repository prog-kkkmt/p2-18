{Дана строка S и текстовый файл. Добавить строку S в конец файла}
var
f:text;
s:string;
begin
  assign(f, 'test5.txt');
  append(f);
  readln(s);
  writeln(f);
  write(f, s);
  close(f);
end.