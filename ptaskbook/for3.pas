{���� ��� ����� ����� A � B (A < B).
������� � ������� �������� ��� ����� �����, ������������� ����� A � B
(�� ������� ����� A � B), � ����� ���������� N ���� �����}
var a, b, i, n:integer;
begin
  readln(a, b);
  if a < b then
  begin
    inc(a);
    dec(b);
    for i:= b downto a do
    begin
      writeln(i);
      inc(n);
    end;
  end;
  writeln(n);
end.