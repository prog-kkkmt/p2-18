object Form1: TForm1
  Left = 1322
  Top = 121
  Anchors = []
  AutoScroll = False
  BorderIcons = []
  Caption = 'Library'
  ClientHeight = 617
  ClientWidth = 738
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
  object BTShowList: TButton
    Left = 40
    Top = 0
    Width = 65
    Height = 33
    Caption = 'Show List'
    TabOrder = 0
    OnClick = BTShowListClick
  end
  object Memo1: TMemo
    Left = 112
    Top = 0
    Width = 617
    Height = 585
    Color = clNone
    Constraints.MaxHeight = 720
    Constraints.MaxWidth = 1240
    Constraints.MinHeight = 585
    Constraints.MinWidth = 617
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
    Top = 0
    Width = 25
    Height = 33
    Caption = 'X'
    TabOrder = 2
    OnClick = BTExitClick
  end
  object Edit1: TEdit
    Left = 112
    Top = 592
    Width = 617
    Height = 21
    TabOrder = 3
  end
  object BTAddAuthor: TButton
    Left = 8
    Top = 40
    Width = 97
    Height = 33
    Caption = 'Add Author'
    TabOrder = 4
    OnClick = BTAddAuthorClick
  end
  object BTdelauthor: TButton
    Left = 8
    Top = 80
    Width = 97
    Height = 33
    Caption = 'Del Author'
    TabOrder = 5
    OnClick = BTdelauthorClick
  end
  object BTFindAuthor: TButton
    Left = 8
    Top = 120
    Width = 97
    Height = 33
    Caption = 'Find Author'
    TabOrder = 6
    OnClick = BTFindAuthorClick
  end
  object BTsortAuthor: TButton
    Left = 8
    Top = 160
    Width = 97
    Height = 33
    Caption = 'Sort by Author'
    TabOrder = 7
    OnClick = BTsortAuthorClick
  end
  object BTsortBook: TButton
    Left = 8
    Top = 200
    Width = 97
    Height = 33
    Caption = 'BTsortBook'
    TabOrder = 8
    OnClick = BTsortBookClick
  end
  object BTsortYear: TButton
    Left = 8
    Top = 240
    Width = 97
    Height = 33
    Caption = 'BTsortYear'
    TabOrder = 9
    OnClick = BTsortYearClick
  end
end
