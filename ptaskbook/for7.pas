{���� ��� ����� ����� A � B (A < B).
����� ����� ���� ����� ����� �� A �� B ������������}
var a, b, i, n:integer;
begin
  readln(a, b);
  if a < b then
  begin
    for i:= a to b do
      inc(n, i);
  end;
  writeln(n);
end.