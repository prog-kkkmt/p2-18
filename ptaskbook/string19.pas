var
s:string;
i, n, tochka:integer;
begin
  readln(s);
  for i:= 1 to length(s) do
  begin
    if (i >= 2) and (s[i] = '.') then
      inc(tochka);
    if (s[i] in ['0'..'9']) and (s[1] <> '.') then
    begin
      n:= 1;
    if (n = 1) and (tochka = 1) then
      n:= 2;
    end
    else
      n:= 0;
  end;
  writeln(n);
end.