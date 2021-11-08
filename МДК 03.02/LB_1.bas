Attribute VB_Name = "Module2"
Sub p04()
  Rem Программа находит наибольшее число из четырёх представленных.
  Dim a As Integer, b As Integer, c As Integer, d As Integer, max As Integer
  a = InputBox("1")
  b = InputBox("2")
  c = InputBox("3")
  d = InputBox("4")
  max = a
  If b > max Then max = b
  If c > max Then max = c
  If d > max Then max = d
  MsgBox max
End Sub

