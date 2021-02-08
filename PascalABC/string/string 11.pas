var
  s: string;
  i: byte;
begin
  readln(s);
  for i:= 1 to length(s) do
  write(s[i],' ');
end.