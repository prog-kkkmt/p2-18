object Client: TClient
  Left = 188
  Top = 160
  Width = 425
  Height = 641
  BorderIcons = []
  Caption = #1063#1072#1090' - '#1050#1083#1080#1077#1085#1090
  Color = clDefault
  Font.Charset = RUSSIAN_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'Segoe Print'
  Font.Style = []
  OldCreateOrder = False
  Position = poScreenCenter
  PixelsPerInch = 96
  TextHeight = 19
  object Info: TLabel
    Left = 336
    Top = 72
    Width = 64
    Height = 19
    Caption = 'Version 1.0'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -11
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentFont = False
  end
  object Host: TEdit
    Left = 8
    Top = 8
    Width = 161
    Height = 25
    AutoSize = False
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clFuchsia
    Font.Height = -11
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 0
    Text = 'Host'
  end
  object Port: TEdit
    Left = 176
    Top = 8
    Width = 161
    Height = 27
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clFuchsia
    Font.Height = -11
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 1
    Text = 'Port'
  end
  object Login: TEdit
    Left = 8
    Top = 40
    Width = 161
    Height = 27
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clAqua
    Font.Height = -11
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 2
    Text = 'Login'
  end
  object Password: TEdit
    Left = 176
    Top = 40
    Width = 161
    Height = 27
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clAqua
    Font.Height = -11
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 3
    Text = 'Password'
  end
  object BTlogIn: TButton
    Left = 344
    Top = 8
    Width = 57
    Height = 25
    Caption = 'Connect'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -11
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 4
    OnClick = BTlogInClick
  end
  object MText: TMemo
    Left = 8
    Top = 96
    Width = 393
    Height = 465
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -12
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentFont = False
    ReadOnly = True
    ScrollBars = ssVertical
    TabOrder = 5
  end
  object Enter: TEdit
    Left = 8
    Top = 568
    Width = 361
    Height = 27
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -11
    Font.Name = 'Segoe Print'
    Font.Style = []
    ParentFont = False
    TabOrder = 6
  end
  object BTSend: TButton
    Left = 376
    Top = 568
    Width = 25
    Height = 25
    Caption = 'GO'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWindowText
    Font.Height = -11
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 7
    OnClick = BTSendClick
  end
  object RBTLogIn: TRadioButton
    Left = 8
    Top = 72
    Width = 105
    Height = 17
    Caption = #1040#1074#1090#1086#1088#1080#1079#1072#1094#1080#1103
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -12
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentColor = False
    ParentFont = False
    TabOrder = 8
  end
  object RBTRegister: TRadioButton
    Left = 176
    Top = 72
    Width = 105
    Height = 17
    Caption = #1056#1077#1075#1080#1089#1090#1088#1072#1094#1080#1103
    Color = clNone
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -12
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentColor = False
    ParentFont = False
    TabOrder = 9
  end
  object REText: TRichEdit
    Left = 8
    Top = 96
    Width = 393
    Height = 465
    BiDiMode = bdLeftToRight
    BorderStyle = bsNone
    Color = clBlack
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWindowText
    Font.Height = -13
    Font.Name = 'Segoe Print'
    Font.Style = []
    ParentBiDiMode = False
    ParentFont = False
    ReadOnly = True
    ScrollBars = ssVertical
    TabOrder = 10
  end
  object BTDisconnect: TButton
    Left = 344
    Top = 40
    Width = 57
    Height = 25
    Caption = 'Disconnect'
    Font.Charset = RUSSIAN_CHARSET
    Font.Color = clWhite
    Font.Height = -9
    Font.Name = 'Segoe Print'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 11
    OnClick = BTDisconnectClick
  end
  object ClientSocket: TClientSocket
    Active = False
    ClientType = ctNonBlocking
    Port = 0
    OnConnect = ClientSocketConnect
    OnDisconnect = ClientSocketDisconnect
    OnRead = ClientSocketRead
    OnError = ClientSocketError
    Left = 376
  end
end
