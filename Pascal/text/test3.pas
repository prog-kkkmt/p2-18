// Дано имя файла и целое число N (0 < N < 27). Создать текстовый файл с 
// указанным именем и записать в него N строк длины N; строка с номером K 
// (K = 1, …, N) должна содержать K начальных прописных (т. е. заглавных) 
// латинских букв, дополненных справа символами «*» (звездочка). Например, 
// для N = 4 файл должен содержать строки «A***», «AB**», «ABC*», «ABCD».
var
f:text;
st:char;
j,i,n,a:integer;
s:string;
begin
  a:=97;
  st:='*';
  assign(f,'test3.txt');
  rewrite(f);
  readln(n);
  for i:=1 to n do
  begin
    s:=s+chr(a);
    inc(a);
    write(f,s);
  for j:=1 to n-i do  
    write(f,st);
  writeln(f);
  end;  
  close(f);
end.