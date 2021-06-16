object NotePadF: TNotePadF
  Left = 0
  Top = 0
  Caption = #1041#1083#1086#1082#1085#1086#1090
  ClientHeight = 393
  ClientWidth = 589
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Tahoma'
  Font.Style = []
  Menu = MainMenu
  OldCreateOrder = False
  OnClose = FormClose
  OnCreate = FormCreate
  DesignSize = (
    589
    393)
  PixelsPerInch = 96
  TextHeight = 13
  object MText: TMemo
    Left = 1
    Top = 1
    Width = 588
    Height = 374
    Anchors = [akLeft, akTop, akRight, akBottom]
    BorderStyle = bsNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWindowText
    Font.Height = -15
    Font.Name = 'Consolas'
    Font.Style = []
    ParentFont = False
    ScrollBars = ssVertical
    TabOrder = 0
    WantTabs = True
    WordWrap = False
    OnChange = MTextChange
    OnClick = MTextClick
    OnKeyUp = MTextKeyUp
  end
  object StatusBar: TStatusBar
    Left = 0
    Top = 373
    Width = 589
    Height = 20
    Anchors = [akLeft, akRight]
    Color = clWhite
    DoubleBuffered = False
    Enabled = False
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clBlack
    Font.Height = -12
    Font.Name = 'Segoe UI'
    Font.Style = []
    Panels = <
      item
        Alignment = taRightJustify
        Bevel = pbRaised
        BiDiMode = bdLeftToRight
        ParentBiDiMode = False
        Text = 'Windows (CRLF)'
        Width = 0
      end
      item
        Alignment = taCenter
        Bevel = pbRaised
        BiDiMode = bdLeftToRight
        ParentBiDiMode = False
        Text = #1057#1090#1088' 1, '#1089#1090#1083#1073' 1'
        Width = 110
      end
      item
        Bevel = pbRaised
        BiDiMode = bdLeftToRight
        ParentBiDiMode = False
        Text = '100%'
        Width = 50
      end>
    ParentDoubleBuffered = False
    UseSystemFont = False
    StyleElements = []
    OnResize = StatusBarResize
  end
  object MainMenu: TMainMenu
    BiDiMode = bdLeftToRight
    ParentBiDiMode = False
    Left = 16
    Top = 16
    object File: TMenuItem
      Caption = '&'#1060#1072#1081#1083
      object Create: TMenuItem
        Caption = #1057#1086#1079#1076'&'#1072#1090#1100
        ShortCut = 16462
        OnClick = CreateClick
      end
      object Open: TMenuItem
        Caption = '&'#1054#1090#1082#1088#1099#1090#1100'...'
        ShortCut = 16463
        OnClick = OpenClick
      end
      object Save: TMenuItem
        Caption = '&'#1057#1086#1093#1088#1072#1085#1080#1090#1100
        Enabled = False
        ShortCut = 16467
        OnClick = SaveClick
      end
      object Save_Ass: TMenuItem
        Caption = #1057#1086#1093#1088#1072#1085#1080#1090#1100' &'#1082#1072#1082'...'
        OnClick = Save_AssClick
      end
      object N10: TMenuItem
        Caption = '-'
      end
      object Page_Settings: TMenuItem
        Caption = #1055#1072#1088#1072'&'#1084#1077#1090#1088#1099' '#1089#1090#1088#1072#1085#1080#1094#1099'...'
        OnClick = Page_SettingsClick
      end
      object Printing: TMenuItem
        Caption = '&'#1055#1077#1095#1072#1090#1100'...'
        ShortCut = 16464
        OnClick = PrintingClick
      end
      object N13: TMenuItem
        Caption = '-'
      end
      object Exit: TMenuItem
        Caption = #1042'&'#1099#1093#1086#1076
        OnClick = ExitClick
      end
    end
    object Edit: TMenuItem
      Caption = '&'#1055#1088#1072#1074#1082#1072
      object Undo: TMenuItem
        Caption = '&'#1054#1090#1084#1077#1085#1072
        Enabled = False
        ShortCut = 16474
        OnClick = UndoClick
      end
      object N15: TMenuItem
        Caption = '-'
      end
      object Cut: TMenuItem
        Caption = '&'#1042#1099#1088#1077#1079#1072#1090#1100
        Enabled = False
        ShortCut = 16472
        OnClick = CutClick
      end
      object Copy: TMenuItem
        Caption = '&'#1050#1086#1087#1080#1088#1086#1074#1072#1090#1100
        Enabled = False
        ShortCut = 16451
        OnClick = CopyClick
      end
      object Paste: TMenuItem
        Caption = #1042#1089#1090'&'#1072#1074#1080#1090#1100
        ShortCut = 16470
        OnClick = PasteClick
      end
      object Delete: TMenuItem
        Caption = '&'#1059#1076#1072#1083#1080#1090#1100
        Enabled = False
        ShortCut = 46
        OnClick = DeleteClick
      end
      object N20: TMenuItem
        Caption = '-'
      end
      object Bing: TMenuItem
        Caption = '&'#1055#1086#1080#1089#1082' '#1089' '#1087#1086#1084#1086#1097#1100#1102' Bing...'
        ShortCut = 16453
        OnClick = BingClick
      end
      object Find: TMenuItem
        Caption = '&'#1053#1072#1081#1090#1080'...'
        Enabled = False
        ShortCut = 16454
        OnClick = FindClick
      end
      object Find_Next: TMenuItem
        Caption = #1053#1072#1081#1090#1080' &'#1076#1072#1083#1077#1077
        Enabled = False
        ShortCut = 114
        OnClick = Find_NextClick
      end
      object Repalce: TMenuItem
        Caption = '&'#1047#1072#1084#1077#1085#1080#1090#1100'...'
        ShortCut = 16456
        OnClick = RepalceClick
      end
      object GoTo: TMenuItem
        Caption = #1055#1077#1088#1077#1081'&'#1090#1080'...'
        Enabled = False
        ShortCut = 16455
        OnClick = GoToClick
      end
      object N25: TMenuItem
        Caption = '-'
      end
      object Selete_All: TMenuItem
        Caption = #1042#1099#1076#1077#1083#1080#1090#1100' '#1074'&'#1089#1105
        ShortCut = 16449
        OnClick = Selete_AllClick
      end
      object Time_Date: TMenuItem
        Caption = #1042#1088#1077#1084'&'#1103' '#1080' '#1076#1072#1090#1072
        ShortCut = 116
        OnClick = Time_DateClick
      end
    end
    object Format: TMenuItem
      Caption = #1060#1086#1088'&'#1084#1072#1090
      object Word_Wrap: TMenuItem
        Caption = '&'#1055#1077#1088#1077#1085#1086#1089' '#1087#1086' '#1089#1083#1086#1074#1072#1084
        Checked = True
        OnClick = Word_WrapClick
      end
      object Font: TMenuItem
        Caption = '&'#1064#1088#1080#1092#1090'...'
        OnClick = FontClick
      end
    end
    object Viwe: TMenuItem
      Caption = '&'#1042#1080#1076
      object Scale: TMenuItem
        Caption = '&'#1052#1072#1089#1096#1090#1072#1073
        object to_Enlarge: TMenuItem
          Caption = '&'#1059#1074#1077#1083#1080#1095#1080#1090#1100
          ShortCut = 16491
          OnClick = to_EnlargeClick
        end
        object Reduce: TMenuItem
          Caption = '&'#1059#1084#1077#1085#1100#1096#1080#1090#1100
          ShortCut = 16493
          OnClick = ReduceClick
        end
        object Restore_to_default: TMenuItem
          Caption = '&'#1042#1086#1089#1089#1090#1072#1085#1086#1074#1080#1090#1100' '#1084#1072#1089#1096#1090#1072#1073' '#1087#1086' '#1091#1084#1086#1083#1095#1072#1085#1080#1102
          ShortCut = 16432
          OnClick = Restore_to_defaultClick
        end
      end
      object Status_Bar: TMenuItem
        Caption = '&'#1057#1090#1088#1086#1082#1072' '#1089#1086#1089#1090#1086#1103#1085#1080#1103
        Checked = True
        OnClick = Status_BarClick
      end
      object NightS: TMenuItem
        Caption = #1058#1077#1084#1085#1072#1103' '#1090#1077#1084#1072
        OnClick = NightSClick
      end
    end
    object Reference: TMenuItem
      Caption = '&'#1057#1087#1088#1072#1074#1082#1072
      object Viwe_Help: TMenuItem
        Caption = #1055#1086#1089'&'#1084#1086#1090#1088#1077#1090#1100' '#1089#1087#1088#1072#1074#1082#1091
        OnClick = Viwe_HelpClick
      end
      object N36: TMenuItem
        Caption = '-'
      end
      object Review: TMenuItem
        Caption = #1054#1089#1090#1072#1074#1080#1090#1100' '#1086#1090#1079#1099#1074'...'
        OnClick = ReviewClick
      end
      object About_the_Programm: TMenuItem
        Caption = '&'#1054' '#1087#1088#1086#1075#1088#1072#1084#1084#1077
        OnClick = About_the_ProgrammClick
      end
    end
  end
  object OpenTF: TOpenTextFileDialog
    Filter = #1058#1077#1082#1089#1090#1086#1074#1099#1077' '#1076#1086#1082#1091#1084#1077#1085#1090#1099' (*.txt)|*.txt|'#1042#1089#1077' '#1092#1072#1081#1083#1099' (*.*)|*.*'
    Options = [ofHideReadOnly, ofNoChangeDir, ofOldStyleDialog, ofEnableSizing]
    Title = #1054#1090#1082#1088#1099#1090#1080#1077
    Left = 48
    Top = 16
  end
  object SaveTF: TSaveTextFileDialog
    DefaultExt = '.txt'
    Filter = #1058#1077#1082#1089#1090#1086#1074#1099#1077' '#1076#1086#1082#1091#1084#1077#1085#1090#1099' (*.txt)|*.txt|'#1042#1089#1077' '#1092#1072#1081#1083#1099' (*.*)|*.*'
    Options = [ofOverwritePrompt, ofHideReadOnly, ofNoChangeDir, ofOldStyleDialog, ofEnableSizing]
    Title = #1057#1086#1093#1088#1072#1085#1077#1085#1080#1077
    Left = 48
    Top = 48
  end
  object FontD: TFontDialog
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'Tahoma'
    Font.Style = []
    Left = 80
    Top = 16
  end
  object FindD: TFindDialog
    OnFind = FindDFind
    Left = 112
    Top = 16
  end
  object PageSetupD: TPageSetupDialog
    MinMarginLeft = 0
    MinMarginTop = 0
    MinMarginRight = 0
    MinMarginBottom = 0
    MarginLeft = 2500
    MarginTop = 2500
    MarginRight = 2500
    MarginBottom = 2500
    PageWidth = 21000
    PageHeight = 29700
    Left = 144
    Top = 16
  end
  object PrintD: TPrintDialog
    Left = 144
    Top = 48
  end
  object ReplaceD: TReplaceDialog
    OnFind = ReplaceDFind
    OnReplace = ReplaceDReplace
    Left = 112
    Top = 48
  end
end
