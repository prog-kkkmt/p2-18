var
a: string;
b: integer;
c: byte;
begin
  writeln('');
  readln(a);
  c:= 1;
  for b := 1 to length (a) do
    if (a[b] < '0') or (a[b] > '9') then
      if (c = 1) and ( a[b] = '.') then
        c:= 2
        else
        c:= 0;
        writeln(c);
        readln       
end.
