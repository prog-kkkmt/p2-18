Attribute VB_Name = "Module3"
Sub selectcase()
Rem ��������� ���������, � ����� �� �������� ������ ��������� � ���������� �����.
Dim a As Integer, b As String
a = InputBox("������� ����� �� 1 �� 30", "������ 2", 1)
    Select Case a
        Case 1 To 10
            b = "����� " & a & " ������ � ������ �������"
        Case 11 To 20
            b = "����� " & a & " ������ �� ������ �������"
        Case 21 To 30
            b = "����� " & a & " ������ � ������ �������"
        Case Else
            b = "����� " & a & " �� ������ � ������ ��� �������"
    End Select
MsgBox b
End Sub

