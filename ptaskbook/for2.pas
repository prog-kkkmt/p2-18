{���� ��� ����� ����� A � B (A < B).
������� � ������� ����������� ��� ����� �����, ������������� �����
A � B (������� ���� ����� A � B), � ����� ���������� N ���� �����}
var a, b, i, n:integer;
begin
  readln(a, b);
  if a < b then
  begin
    for i:= a to b do
    begin
      writeln(i);
      inc(n);
    end;
  end;
  writeln(n);
end.