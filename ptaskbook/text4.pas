{Дан текстовый файл. Вывести количество содержащихся в нем символов и строк}
var
f:text;
a, b, i, n:integer;
s:string;
begin
  assign(f, 'test4.txt');
  reset(f);
  while not eof(f) do
  begin
    readln(f, s);
    inc(n, length(s));
    inc(a);
  end;
  close(f);
  writeln(n);
  writeln(a);
end.