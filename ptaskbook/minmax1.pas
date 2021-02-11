{ƒано целое число N и набор из N чисел.
Ќайти минимальный и максимальный из элементов данного
набора и вывести их в указанном пор€дке}
var
i, n:integer;
max, min, a, b:real;
begin
  readln(n);
  max:= -min;
  min:= MaxInt;
  for i:= 1 to n do
  begin
    readln(a);
    if min > a then
      min:= a;
    if max < a then
      max:= a;
  end;
  writeln(max, ' ', min);
end.