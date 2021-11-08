Attribute VB_Name = "Module6"
Function sum(a As Integer, b As Integer) As Integer
    sum = a + b
End Function

Sub sum_proc(ByVal a As Integer, ByVal b As Integer, ByRef summa As Integer)
    summa = a + b
End Sub


Sub sum_demo()
    Rem Функции и процедуры
    
    Dim x As Integer, c As Integer
    x = InputBox("")
    Call sum_proc(x, 5, c)
    MsgBox ("Function -> " & sum(x, 5) & vbNewLine & "Sub--> " & c)

End Sub
