Attribute VB_Name = "Module3"
Sub selectcase()
Rem Программа вычисляет, в какой из десятков входит введенное с клавиатуры число.
Dim a As Integer, b As String
a = InputBox("Введите число от 1 до 30", "Пример 2", 1)
    Select Case a
        Case 1 To 10
            b = "Число " & a & " входит в первую десятку"
        Case 11 To 20
            b = "Число " & a & " входит во вторую десятку"
        Case 21 To 30
            b = "Число " & a & " входит в третью десятку"
        Case Else
            b = "число " & a & " не входит в первые три десятки"
    End Select
MsgBox b
End Sub

