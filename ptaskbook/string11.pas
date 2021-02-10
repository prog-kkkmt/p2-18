var
s, container:string;
i, n:integer;
begin
  readln(s);
  container:= s[1];
  for i:= 1 to length(s) do
    container:= container + ' ' + s[i];
  writeln(container);
end.