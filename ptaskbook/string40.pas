{Дана строка, содержащая по крайней мере один символ пробела.
Вывести подстроку, расположенную между первым и вторым пробелом исходной строки.
Если строка содержит только один пробел, то вывести пустую строку}
var
s:string;
position1, position2, i:integer;
begin
  readln(s);
  position1:= pos(' ', s);
  delete(s, position1, 1);
  position2:= pos(' ', s);
  writeln(copy(s, position1, position2 - position1));
end.