{���� ��� ����� � ����� ����� N (0 < N < 27).
������� ��������� ���� � ��������� ������ � �������� � ����
N �����: ������ ������ ������ ��������� �������� (�. �. ���������)
��������� ����� �a�, ������ � ����� �ab�, ������ � ����� �abc� � �. �.;
��������� ������ ������ ��������� N ��������� �������� ���������
���� � ���������� �������}
var
f:text;
a, b, i, n:integer;
s:string;
begin
  b:= 97;
  assign(f, 'test2.txt');
  rewrite(f);
  readln(n);
  for a:= 1 to n do
  begin
    s:= s + chr(ord(b));
    writeln(f, s);
    inc(b);
  end;
  close(f);
end.