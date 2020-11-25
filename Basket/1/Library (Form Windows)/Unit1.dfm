object Form1: TForm1
  Left = 1323
  Top = 114
  Anchors = []
  AutoScroll = False
  BorderIcons = []
  Caption = 'Library'
  ClientHeight = 627
  ClientWidth = 749
  Color = clBackground
  TransparentColorValue = clInactiveCaptionText
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  Position = poScreenCenter
  Scaled = False
  PixelsPerInch = 96
  TextHeight = 13
  object BTShowList: TButton
    Left = 48
    Top = 8
    Width = 97
    Height = 17
    Caption = 'Show List'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    TabOrder = 0
    OnClick = BTShowListClick
  end
  object Memo1: TMemo
    Left = 152
    Top = 8
    Width = 593
    Height = 585
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -21
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    ScrollBars = ssVertical
    TabOrder = 1
  end
  object BTExit: TButton
    Left = 8
    Top = 8
    Width = 33
    Height = 17
    Caption = 'X'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    TabOrder = 2
    OnClick = BTExitClick
  end
  object Edit1: TEdit
    Left = 152
    Top = 600
    Width = 593
    Height = 21
    TabOrder = 3
  end
  object BTAddAuthor: TButton
    Left = 8
    Top = 32
    Width = 65
    Height = 17
    Caption = '+ Author'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    TabOrder = 4
    OnClick = BTAddAuthorClick
  end
  object BTdelauthor: TButton
    Left = 80
    Top = 32
    Width = 65
    Height = 17
    Caption = '- Author'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    TabOrder = 5
    OnClick = BTdelauthorClick
  end
  object BTFindAuthor: TButton
    Left = 8
    Top = 56
    Width = 137
    Height = 17
    Caption = 'Find Author'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    TabOrder = 6
    OnClick = BTFindAuthorClick
  end
  object BTsortAuthor: TButton
    Left = 8
    Top = 104
    Width = 137
    Height = 17
    Caption = 'Sort by Author'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    TabOrder = 7
    OnClick = BTsortAuthorClick
  end
  object BTsortBook: TButton
    Left = 8
    Top = 128
    Width = 137
    Height = 17
    Caption = 'Sort by Book'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clRed
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    TabOrder = 8
    OnClick = BTsortBookClick
  end
  object BTsortYear: TButton
    Left = 8
    Top = 152
    Width = 137
    Height = 17
    BiDiMode = bdLeftToRight
    Caption = 'Sort by Year'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Style = []
    ParentBiDiMode = False
    ParentFont = False
    ParentShowHint = False
    ShowHint = False
    TabOrder = 9
    OnClick = BTsortYearClick
  end
  object BTFindBook: TButton
    Left = 8
    Top = 80
    Width = 137
    Height = 17
    Caption = 'Find Book'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -13
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    TabOrder = 10
    OnClick = BTFindBookClick
  end
end
