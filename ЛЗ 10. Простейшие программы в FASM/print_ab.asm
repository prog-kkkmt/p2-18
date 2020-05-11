name print_ab
; Гусятинер Л.Б., 11.05.2020
org 100h ; Для .com

MOV AH, 02h  ; Функция печати
MOV DL, 41h  ; ASCII-код символа 'A'
INT 21h      ; Вызов функции
MOV DL, 0Dh  ; chr(13), возврат каретки
INT 21h      ; 
MOV DL, 0Ah  ; chr(10), перевод на новую строку
INT 21h      ; 
MOV DL, 'B'  ;
INT 21h      ;

ret
