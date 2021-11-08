Attribute VB_Name = "Module7"
Rem Созание и заполнение массива через цикл

Sub arrayDemo()
Const N As Integer = 10
Dim arr(1 To N) As Integer, i As Integer
Dim max As Integer
    For i = 1 To N
        arr(i) = i ^ 2
    Next i
    max = arr(1)
    For i = 2 To N
        If arr(i) > max Then
            max = arr(i)
        End If
    Next
    MsgBox (max)
End Sub

