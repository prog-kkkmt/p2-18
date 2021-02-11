function Dec(s:string):string;
var
n,i,k:integer;
begin
  n:=0;
  for i:=1 to length(s) do
  begin
    k:=ord(s[i])-ord('0');
    n:=n*2+k;
  end;
  Dec:=n;
end.