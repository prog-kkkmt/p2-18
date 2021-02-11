// Дана непустая строка S. Вывести строку, содержащую символы строки S, 
// между которыми вставлено по одному пробелу.
var
s,c:string;
n,i:integer;
begin
  readln(s);
  c:=s[1];
  for i:=1 to length(s) do
    c:=c + ' ' + s[i];
  writeln(c);  
end.