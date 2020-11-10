object Form1: TForm1
  Left = 280
  Top = 175
  Anchors = []
  AutoScroll = False
  BorderIcons = []
  Caption = 'Library'
  ClientHeight = 625
  ClientWidth = 734
  Color = clBackground
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  Scaled = False
  PixelsPerInch = 96
  TextHeight = 13
  object Button1: TButton
    Left = 40
    Top = 8
    Width = 65
    Height = 33
    Caption = 'Show List'
    TabOrder = 0
    OnClick = Button1Click
  end
  object Memo1: TMemo
    Left = 112
    Top = 8
    Width = 617
    Height = 585
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -16
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    TabOrder = 1
  end
  object Button2: TButton
    Left = 8
    Top = 8
    Width = 25
    Height = 33
    Caption = 'X'
    TabOrder = 2
    OnClick = Button2Click
  end
  object Edit1: TEdit
    Left = 112
    Top = 600
    Width = 617
    Height = 21
    TabOrder = 3
  end
  object Button3: TButton
    Left = 8
    Top = 48
    Width = 97
    Height = 33
    Caption = 'Add Author'
    TabOrder = 4
    OnClick = Button3Click
  end
  object Button4: TButton
    Left = 8
    Top = 88
    Width = 97
    Height = 33
    Caption = 'Del Author'
    TabOrder = 5
    OnClick = Button4Click
  end
  object Button5: TButton
    Left = 8
    Top = 128
    Width = 97
    Height = 33
    Caption = 'Find Author'
    TabOrder = 6
  end
  object Button6: TButton
    Left = 8
    Top = 168
    Width = 97
    Height = 33
    Caption = 'Button6'
    TabOrder = 7
  end
  object Button7: TButton
    Left = 8
    Top = 208
    Width = 97
    Height = 33
    Caption = 'Button7'
    TabOrder = 8
  end
  object Button8: TButton
    Left = 8
    Top = 248
    Width = 97
    Height = 33
    Caption = 'Button8'
    TabOrder = 9
  end
end
