{
menu2
Входной файл
Дата | ФИО | Группа | Кол-во пропусков
Отчёты
кол-во пропусков за период
1. По студенту
2. По группе
3. Всего
MENU
1. Добавить строку
2. Отчёт по группе за период
3. Отчёт по студенту за период
4. Выход
5. О программе
}
const
  MAXN = 1000;
type
  TDate = Record
    year:integer;
    month:integer;
    day:integer;
    a:integer;
    string_mas:string;
end;
procedure menu1;
var
filetext:text;
i, n, a, b, y, j, choise, count:integer;
s:string;
arr:array[1..MAXN] of TDate;
begin
  for i:= 1 to 10 do
  begin
    arr[i].day:= random(1, 31);
    arr[i].month:= random(1, 12);
    arr[i].year:= random(2018, 2021);
    arr[i].a:= random(count);
  end;
  assign(filetext, 'spisok.txt');
  append(filetext);
  while not eof(filetext) do
  begin
    readln(filetext, s);
    for i:= 1 to length(s) do
    begin
      if s[1] then
      begin
        if (arr[i].month = 2) and (arr[i].day > 28) then
          inc(b)
        else
          writeln(filetext, arr[i].day, '.', arr[i].month, '.', arr[i].year);
      end;
    end;
    inc(a);
  end;
  close(filetext);
end;
procedure p2_18;
var
choise:integer;
begin
  repeat
    writeln('Меню\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\');
    writeln('1 - Добавить строку\\\\\\\\\\\\\\\\\\\');
    writeln('2 - Отчет по группе за период\\\\\\\\\');
    writeln('3 - Отчет по студенту за период\\\\\\\');
    writeln('4 - О программе\\\\\\\\\\\\\\\\\\\\\\\');
    writeln('0 - В главное меню\\\\\\\\\\\\\\\\\\\\');
    readln(choise);
    case(choise) of
        1: menu1;
        0: choise:= 4;
    end;
  until choise = 4;
end;
var
  filetext:text;
  i, n, a, b, y, j, choise, choise2, count:integer;
  s, s2, s3:string;
  arr:array[1..MAXN] of TDate;
begin
  begin
  repeat
    writeln('1 - P1-18\\\\\\\\\');
    writeln('2 - P2-18\\\\\\\\\');
    writeln('0 - Выход\\\\\\\\\');
    readln(choise);
    case(choise) of
      // 1: p1_18;
      2: p2_18;
      0: choise:= 4;
    end;
  until choise = 4;
  end;
end.