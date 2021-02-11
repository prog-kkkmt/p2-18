// Дан непустой текстовый файл. Удалить из него первую строку.
const MaxN=1000;
var
a:array[1..MaxN] of string;
i,n:integer;
s:string;
f:text;
text13:string;
begin
  readln(text13);
  assign(f,text13);
  reset(f);
  n:=0;
  while not (eof(f)) do
  begin
    n:=n+1;
    readln(f,a[n]);
  end;
  close(f);
  rewrite(f);
  for i:=2 to n do
    writeln(f,a[i]);
    close(f);
end.