{���� ��� ����� � ����� ����� N (0 < N < 27). ������� ��������� ����
� ��������� ������ � �������� � ���� N ����� ����� N; ������ � �������
K (K = 1, �, N) ������ ��������� K ��������� ��������� (�. �. ���������)
��������� ����, ����������� ������ ��������� �*� (���������).
��������, ��� N = 4 ���� ������ ��������� ������
�A***�, �AB**�, �ABC*�, �ABCD�}
var
f:text;
j, b, i, n:integer;
s:string;
star:char;
begin
  b:= 97;
  star:= '*';
  assign(f, 'test3.txt');
  rewrite(f);
  readln(n);
  for i:= 1 to n do
  begin
    s:= s + chr(b);
    inc(b);
    write(f, s);
    for j:= 1 to n - i do
      write(f, '*');
    writeln(f);
  end;
  close(f);
end.