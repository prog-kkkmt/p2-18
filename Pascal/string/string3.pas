  {���� ������. ���������� ���������� ������������ 
� ��� ��������� ��������� ����.}
  var
s:string;
i,j,n:integer;
begin
  readln(s);
  for i:=1 to length(s) do
    if s[i] in ['A'..'Z'] then
      j:=j + 1;
  if j > 0 then writeln(j);
end.
