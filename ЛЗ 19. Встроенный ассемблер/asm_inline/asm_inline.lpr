// Михаил "Lanode" П1-18
// License: GNU GPL
program asm_inline;

{$asmMode intel}

function SumBytes(x, y: Byte): Byte;
var
  r: Byte;
begin
  asm
    MOV AH, x
    ADD AH, y
    MOV r, AH
  end;
  exit(r);
end;

var
  a, b, c: Byte;
begin
  Write('a: ');
  ReadLn(a);
  Write('b: ');
  Readln(b);
  c := SumBytes(a, b);
  WriteLn(c, ' = ', a, ' + ', b);
end.
