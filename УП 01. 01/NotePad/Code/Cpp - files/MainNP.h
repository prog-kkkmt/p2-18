//---------------------------------------------------------------------------

#ifndef MainNPH
#define MainNPH
//---------------------------------------------------------------------------
#include <System.Classes.hpp>
#include <Vcl.Controls.hpp>
#include <Vcl.StdCtrls.hpp>
#include <Vcl.Forms.hpp>
#include <Vcl.Menus.hpp>
#include <Vcl.ComCtrls.hpp>
#include <Vcl.Dialogs.hpp>
#include <Vcl.ExtDlgs.hpp>

#include <Registry.hpp>
#include <Xml.xmldom.hpp>
#include <Xml.XMLIntf.hpp>
//---------------------------------------------------------------------------
class TNotePadF : public TForm
{
__published:	// IDE-managed Components

//----------------------------���������� ����--------------------------------
	TMainMenu *MainMenu;
	TMenuItem *File;
	TMenuItem *Edit;
	TMenuItem *Format;
	TMenuItem *Viwe;
	TMenuItem *Reference;
	TMenuItem *Create;
	TMenuItem *Open;
	TMenuItem *Save;
	TMenuItem *Save_Ass;
	TMenuItem *N10;
	TMenuItem *Page_Settings;
	TMenuItem *Printing;
	TMenuItem *N13;
	TMenuItem *Exit;
	TMenuItem *Undo;
	TMenuItem *N15;
	TMenuItem *Cut;
	TMenuItem *Copy;
	TMenuItem *Paste;
	TMenuItem *Delete;
	TMenuItem *N20;
	TMenuItem *Bing;
	TMenuItem *Find;
	TMenuItem *Find_Next;
	TMenuItem *Repalce;
	TMenuItem *GoTo;
	TMenuItem *N25;
	TMenuItem *Selete_All;
	TMenuItem *Time_Date;
	TMenuItem *Word_Wrap;
	TMenuItem *Font;
	TMenuItem *Scale;
	TMenuItem *to_Enlarge;
	TMenuItem *Reduce;
	TMenuItem *Restore_to_default;
	TMenuItem *Status_Bar;
	TMenuItem *Viwe_Help;
	TMenuItem *N36;
	TMenuItem *About_the_Programm;
//---------------------------------------------------------------------------

//-----------------------���������� ����� ��������---------------------------
	TMemo *MText; //�������� ����� ������ ������
	TStatusBar *StatusBar; //������ ���
	TOpenTextFileDialog *OpenTF; //���������� ����, ��� �������� ������
	TSaveTextFileDialog *SaveTF; //���������� ����, ��� ���������� ������
	TFontDialog *FontD; //�����
	TFindDialog *FindD; //���������� ���� ������
	TPageSetupDialog *PageSetupD; //��������� ��������
	TPrintDialog *PrintD; //������
	TReplaceDialog *ReplaceD; //���������� ���� ������
	TMenuItem *Review;
	TMenuItem *NightS; //�����
//---------------------------------------------------------------------------

//-------------------------������� ��������----------------------------------
	void __fastcall StatusBarResize(TObject *Sender); //��������� ��������
	void __fastcall FormClose(TObject *Sender, TCloseAction &Action); //������� �������� �����/���������� ����������
	void __fastcall FormCreate(TObject *Sender); //������� �������� �����/�������������� ����������
	void __fastcall Status_BarClick(TObject *Sender); //StatusBar
	void __fastcall MTextKeyUp(TObject *Sender, WORD &Key, TShiftState Shift);
	void __fastcall MTextChange(TObject *Sender);
	void __fastcall MTextClick(TObject *Sender);

	//��������� ������� File (������� MainMenu);
	void __fastcall Save_AssClick(TObject *Sender); //��������� ���
	void __fastcall OpenClick(TObject *Sender); //�������
	void __fastcall SaveClick(TObject *Sender); //���������
	void __fastcall CreateClick(TObject *Sender); //�������
	void __fastcall Page_SettingsClick(TObject *Sender); //��������� ��������
	void __fastcall PrintingClick(TObject *Sender); //������
	void __fastcall ExitClick(TObject *Sender); //�����

	//��������� ������� Edit (������� MainMenu)
	void __fastcall UndoClick(TObject *Sender); //������
	void __fastcall CutClick(TObject *Sender); //��������
	void __fastcall CopyClick(TObject *Sender); //����������
	void __fastcall PasteClick(TObject *Sender); //��������
	void __fastcall DeleteClick(TObject *Sender); //�������
	void __fastcall BingClick(TObject *Sender); //����� � ������� Bing
	void __fastcall FindClick(TObject *Sender); //�����
	void __fastcall Find_NextClick(TObject *Sender); //����� �����
	void __fastcall RepalceClick(TObject *Sender); //������
	void __fastcall GoToClick(TObject *Sender); //�������
	void __fastcall Selete_AllClick(TObject *Sender); //�������� ��
	void __fastcall Time_DateClick(TObject *Sender); //����� � ����

	//��������� ������� ������ (������� MainMenu)
	void __fastcall FontClick(TObject *Sender); //���� � �����, ������ (Font)
	void __fastcall Word_WrapClick(TObject *Sender); //������� ����

	//��������� ������� ��� (������� MainMenu)
	void __fastcall to_EnlargeClick(TObject *Sender); //��������� �����
	void __fastcall ReduceClick(TObject *Sender); //��������� �����
	void __fastcall Restore_to_defaultClick(TObject *Sender); //������� �� ���������

	//��������� ������� ������� (������� MainMenu)
	void __fastcall Viwe_HelpClick(TObject *Sender); //���������� �������
	void __fastcall About_the_ProgrammClick(TObject *Sender); //� ���������...
	void __fastcall FindDFind(TObject *Sender); //�������� ������� ������
	void __fastcall ReplaceDFind(TObject *Sender); //������ F4
	void __fastcall ReplaceDReplace(TObject *Sender); //������ ����
	void __fastcall ReviewClick(TObject *Sender);
	void __fastcall NightSClick(TObject *Sender); //�����
	

//---------------------------------------------------------------------------


//-------------------�������� ������� � ����������---------------------------
private:	// User declarations
public:		// User declarations
	bool Saved; //����� ����������
	AnsiString FName, FPath, Xstr = "��� ", Ystr = ", ���� "; //���� � �������� ������
    int N, X, Y, FoundAt, StartPos, ToEnd;
	int Size; //������ ������ � %
	__fastcall TNotePadF(TComponent* Owner);
	void __fastcall SavedTF(); //�������� ������� ���������� � �������� ������
	void __fastcall PosCarriage(); //������� �������
    void __fastcall FindNP(); //����� ����
};
//---------------------------------------------------------------------------
extern PACKAGE TNotePadF *NotePadF;
//---------------------------------------------------------------------------


void __fastcall TNotePadF::SavedTF(){
	FName = ExtractFileName(OpenTF->FileName); //������ ��� �����
	FPath = ExtractFilePath(OpenTF->FileName); //������ ���� �����
	if(!Saved && FName == "\0" && MText->Lines->Count > 0 && MessageDlg("�� ������ ��������� ������?",
		mtConfirmation  , TMsgDlgButtons() << mbNo << mbYes, 0) == mrYes && SaveTF->Execute()){//���������, �������� �� ����, ���� ��, �� ��������� ���� ��������, ���� ��� �� ����������
		MText->Lines->SaveToFile(SaveTF->FileName); //��������� ����� � MText (Memo)
		Application->Title = "�������"; //��������������� �����
		}else if(!Saved && FName != "\0" && MText->Lines->Count > 0 && MessageDlg("�� ������ ��������� ��������� � ����� " + FPath + FName,
				mtConfirmation  , TMsgDlgButtons() << mbNo << mbYes, 0) == mrYes){
				MText->Lines->SaveToFile(FPath+FName);
				}
	Saved = false;
}

void __fastcall TNotePadF::PosCarriage(){
	X = MText->Perform(EM_LINEFROMCHAR, MText->SelStart, 0); //���������� X
	Y = MText->SelStart - MText->Perform(EM_LINEINDEX, X, 0); //���������� Y
		X += 1; //�� ���� ������ ���, �� ��� ��������
		Y += 1; //�� ���� ������ ���, �� ��� ��������
	StatusBar->Panels->Items[1]->Text = Xstr + X + Ystr + Y; //���� � ������� ���
}

void __fastcall TNotePadF::FindNP(){
	StartPos = MText->SelStart; //������� ������ ������ (��������� �������)
	Find_Next->Enabled = true; //������ �������� ������ ������ �����

	if(MText->SelLength) //��������� ��� �������
		StartPos += MText->SelLength; //��� �������� �������
		ToEnd = MText->Text.Length() - StartPos; //���� ����� ������

	//����� � ������ ��� ��� ����� ��������
	if(FindD->Options.Contains(frMatchCase))
		FoundAt = StartPos + MText->Text.SubString(StartPos + 1, ToEnd).Pos(FindD->FindText);
	else FoundAt = StartPos + MText->Text.SubString(StartPos + 1, ToEnd).LowerCase().Pos(FindD->FindText.LowerCase());

	if(FoundAt != StartPos){
		MText->SetFocus();
		MText->SelStart = FoundAt-1;
		MText->SelLength = FindD->FindText.Length();
	}else ShowMessage("�� ������� ����� \""  + FindD->FindText + "\"");
		Application->Title = "�������";
}
#endif
