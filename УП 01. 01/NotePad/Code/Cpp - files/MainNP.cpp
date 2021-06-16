//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "MainNP.h"
#include "About.h"
#include "ShellAPI.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"

TNotePadF *NotePadF;
//---------------------------------------------------------------------------
__fastcall TNotePadF::TNotePadF(TComponent* Owner)
	: TForm(Owner)
{
	NotePadF->Caption = "���������� � �������"; //��������� �� ���������
	Size = 100;
	//to_Enlarge->ShortCut = TextToShortCut("Ctrl+NUM +"); //������� ������� +
	//Reduce->ShortCut = TextToShortCut("Ctrl+NUM -"); //������� ������� -

}
//---------------------------------------------------------------------------

void __fastcall TNotePadF::StatusBarResize(TObject *Sender)
{
	//������� ��������� �(���) �������� ����� ������ ����
	StatusBar->Panels->Items[0]->Width = NotePadF->Width/1.250;
}
//---------------------------------------------------------------------------

//------------������� �������� �����/���������� ����������-------------------
void __fastcall TNotePadF::FormClose(TObject *Sender, TCloseAction &Action)
{
	SavedTF();
	TRegistry *reg = new TRegistry; //������� ������ REG ������ TREgistry
	reg->RootKey = HKEY_LOCAL_MACHINE; //������ � ������� ����� ������
	UnicodeString key = "SOFTWARE\\NotePadF"; //���� ��� �������� ��� �������� ��������

	reg->CreateKey(key);
	if(reg->OpenKey(key, true)){ //������� �(���) ��������� ��� ������������ �(���) ��������� �������
		reg->WriteInteger("WindowsPosDY", Left); //����� ������� �����
		reg->WriteInteger("WindowsPosDX", Top); //����� �����
		reg->WriteInteger("WindowsPosX", Width); //������ �����
		reg->WriteInteger("WindowsPosY", Height); //����� �����

		reg->WriteString("FontName", MText->Font->Name); //���������� ������
		reg->WriteInteger("FontSize", MText->Font->Size); //���������� ������� ������

		reg->WriteBool("NightSubject", NightS->Checked); //������ ����
		reg->WriteBool("WordWrap", MText->WordWrap); //������� ����

		reg->WriteBool("StatusBar", StatusBar->Visible); //������ ���

		reg->CloseKey(); //�������� �����
	}
	delete reg; //����������� ������
}
//---------------------------------------------------------------------------

//-----------������� �������� �����/���������� ����������--------------------
void __fastcall TNotePadF::FormCreate(TObject *Sender)
{
	TRegistry *reg = new TRegistry; //������� ������ REG ������ TREgistry
	reg->RootKey = HKEY_LOCAL_MACHINE; //������ � ������� ����� ������
	UnicodeString key = "SOFTWARE\\NotePadF"; //���� ��� �������� ��� �������� ��������

		reg->CreateKey(key);
		if(reg->OpenKey(key, true)){ //������� �(���) ��������� ��� ������������ �(���) ��������� �������
			Left =   reg->ReadInteger("WindowsPosDY"); //����������� ����������� �������� ����� ������� �����
			Top =    reg->ReadInteger("WindowsPosDX"); //����������� ����������� �������� ������� ������� �����
			Width =  reg->ReadInteger("WindowsPosX"); //����������� ����������� �������� ������ �����
			Height = reg->ReadInteger("WindowsPosY"); //����������� ����������� �������� ����� ������� �����

			MText->Font->Name = reg->ReadString("FontName"); //���������� ������ ����
			MText->Font->Size = reg->ReadInteger("FontSize"); //���������� ������� ������ ����
			FontD->Font->Name = reg->ReadString("FontName"); //���������� ������ �����
			FontD->Font->Size = reg->ReadInteger("FontSize"); //���������� ������� ������ �����

			NightS->Checked = reg->ReadBool("NightSubject"); //������ ����
			MText->WordWrap = reg->ReadBool("WordWrap"); //������� ����


			StatusBar->Visible = reg->ReadBool("StatusBar"); //������ ���
			reg->CloseKey(); //�������� �����
		}
		delete reg;

	if (NightS->Checked == true) {
		NightS->Checked = true;
		MText->Color = clWindowText;
		MText->Font->Color = clWhite;
	}
	if(!MText->WordWrap){ //�������� �������� � �������
	   MText->WordWrap = false; //��������� ������� ������
	   Word_Wrap->Checked = false; //������ ���������� ������
	   MText->ScrollBars = ssBoth; //������ Scroll Bar � MText(Memo1)
	}
	if(!StatusBar->Visible){ //��������� ������� �� ������
		StatusBar->Visible = false; //������ ��� ���������
		Status_Bar->Checked = false; //������ ������ �� ��������
		MText->Height = NotePadF->Height - 60; //������� MText(Memo1) ����
	}
}
//---------------------------------------------------------------------------

//---------------------------������� ��������--------------------------------
void __fastcall TNotePadF::CreateClick(TObject *Sender)
{
	SavedTF(); //�������� ������� ��������
	if(MText->Lines->Count > 0){MText->Clear();} //������ �����, ���� �� ����
	NotePadF->Caption = "���������� � �������";
}
//---------------------------------------------------------------------------

//---------------------------������� ��������--------------------------------
void __fastcall TNotePadF::OpenClick(TObject *Sender)
{
	SavedTF(); //�������� ��������� � ������
	if(OpenTF->Execute()){ //�������� ���������� ���� ��������
		FName = ExtractFileName(OpenTF->FileName); //���� �������� ����� (��� �����)
		NotePadF->Caption = FName + " � �������"; //������ ��������� (��� ����� + �������)

		MText->Lines->LoadFromFile(OpenTF->FileName); //������� ���������� � ����� � MText(Memo1)
		Save->Enabled = true; //������ �������� ������ ���������� (MainMenu)
		Saved = false; //������ ���� ���������� False
	}
}
//---------------------------------------------------------------------------

//---------------------------������� ����������------------------------------
void __fastcall TNotePadF::SaveClick(TObject *Sender)
{
	MText->Lines->SaveToFile(FPath + FName); //��������� ���� (����������, ���� �� ���� ��������� ���/�������)
	Caption = "" + FName + " � �������";
	Saved = true; //������ ���� TRUE � Bool Saved
}
//---------------------------------------------------------------------------

//--------------------------������� ���������� ���---------------------------
void __fastcall TNotePadF::Save_AssClick(TObject *Sender)
{
	if(!Saved && SaveTF->Execute()){
		MText->Lines->SaveToFile(SaveTF->FileName); //��������� ���� ����� � ����

		Save->Enabled = true; //������ ������ Save ��������
		Saved = true; //���� ���������� True

		FName = ExtractFileName(SaveTF->FileName); //��� �������� �����
		NotePadF->Caption = FName + " � �������"; //��������������� �����
	}
}
//---------------------------------------------------------------------------

//------------------------��������� ��������---------------------------------
void __fastcall TNotePadF::Page_SettingsClick(TObject *Sender)
{
	if(PageSetupD->Execute()){}; //�������� ���������� ���� ��������� ��������
}
//---------------------------------------------------------------------------

//-------------------------������� ������------------------------------------
void __fastcall TNotePadF::PrintingClick(TObject *Sender)
{
	if(PrintD->Execute()){}; //�������� ���������� ���� ������
}
//---------------------------------------------------------------------------

//-------------------------������� �����-------------------------------------
void __fastcall TNotePadF::ExitClick(TObject *Sender)
{
	SavedTF(); //�������� ���������� � ������
	Close(); //�������� �����
}
//---------------------------------------------------------------------------

//------------------------������� ������-------------------------------------
void __fastcall TNotePadF::UndoClick(TObject *Sender)
{
	MText->Undo(); //������
}
//---------------------------------------------------------------------------

//------------------------������� ��������-----------------------------------
void __fastcall TNotePadF::CutClick(TObject *Sender)
{
	MText->CutToClipboard(); //�������� ���������� �����
}
//---------------------------------------------------------------------------

//---------------------������� ����������------------------------------------
void __fastcall TNotePadF::CopyClick(TObject *Sender)
{
	MText->CopyToClipboard(); //�������� ���������� �����
}
//---------------------------------------------------------------------------

//--------------------������� ��������---------------------------------------
void __fastcall TNotePadF::PasteClick(TObject *Sender)
{
	MText->PasteFromClipboard(); //��������� ���������� �����
}
//---------------------------------------------------------------------------

//-------------------������� ��������----------------------------------------
void __fastcall TNotePadF::DeleteClick(TObject *Sender)
{
    MText->ClearSelection(); //������� ���������� �����
}
//---------------------------------------------------------------------------

//--------------------����� � ������� Bing-----------------------------------
void __fastcall TNotePadF::BingClick(TObject *Sender)
{
	AnsiString Word = MText->SelText; //���������� ��� ��������� ����� � MText
	AnsiString URL = "https://www.bing.com/search?q=" + Word; //��������� ����� � ������
	ShellExecute(Handle, L"open", String(URL).c_str(), NULL, NULL, SW_SHOWDEFAULT); //��������� ������� � ��������
}
//---------------------------------------------------------------------------

//-------------------������ �����-------------------------------------------
void __fastcall TNotePadF::FindClick(TObject *Sender)
{
	FindD->FindText = MText->SelText; //�������� ���� ����� � Memo (MText)
	FindD->Execute();//�������� � ������� FindDFind
}
//---------------------------------------------------------------------------

//-------------------������� �����-------------------------------------------
void __fastcall TNotePadF::FindDFind(TObject *Sender)
{
	FindNP();
}
//---------------------------------------------------------------------------

//-------------------������� ����� �����-------------------------------------
void __fastcall TNotePadF::Find_NextClick(TObject *Sender)
{
	FindNP();
}
//---------------------------------------------------------------------------

//-------------------������� ��������----------------------------------------
void __fastcall TNotePadF::RepalceClick(TObject *Sender)
{
	ReplaceD->FindText = MText->SelText; //�������� ���� ����� � Memo (MText)
	ReplaceD->Execute(); //�������� ���������� ���� ������
}
//---------------------------------------------------------------------------

//-------------------������� ��������----------------------------------------
 void __fastcall TNotePadF::ReplaceDReplace(TObject *Sender)
{
	if (MText->SelText != "") //��������� ���� �� ���������� �����
		MText->SelText = ReplaceD->ReplaceText;

	else if(ReplaceD->Options.Contains(frReplace)){
		ShowMessage("�� ������� �����\"" + ReplaceD->FindText +  "\"");
		Application->Title = "�������";
		return;
	}

	if(ReplaceD->Options.Contains(frReplaceAll)) //������������ � �������� �������
	ReplaceDFind(Sender);

}
//---------------------------------------------------------------------------

//-------------------������� ��������-----------------------------------------
void __fastcall TNotePadF::ReplaceDFind(TObject *Sender)
{
	FoundAt = 0; //������� ������� � ������
	StartPos = MText->SelStart; //��������� �������

	if(MText->SelStart) //��������� ��������� �������
		StartPos += MText->SelLength; //��������� ������� = ��������� �������
		ToEnd = MText->Text.Length() - StartPos; //�������� ��������� ������

	//����� � ������ ��� ��� ����� ��������
	if(FindD->Options.Contains(frMatchCase))
		FoundAt = StartPos + MText->Text.SubString(StartPos+1, ToEnd).Pos(ReplaceD->FindText);
	else FoundAt = StartPos + MText->Text.SubString(StartPos+1, ToEnd).LowerCase().Pos(ReplaceD->FindText.LowerCase());

	if(FoundAt != StartPos){
		MText->SetFocus();
		MText->SelStart = FoundAt-1; //������ ������� �� ������
		MText->SelLength = ReplaceD->FindText.Length(); //���� � ������ �����
	}else{
		ShowMessage("�� ������� ����� \""  + ReplaceD->FindText + "\""); //������� ���������� ���� � �������
		Application->Title = "�������"; //������ �������� �.�.
		MText->SetFocus(); //������ ����� �� Memo (MText)
		MText->CaretPos = Point(0, 0); //������� ������� �� 0 0
		return;
	 }

	if(ReplaceD->Options.Contains(frReplaceAll)) //� ������ ������� ������ �������� ��
		ReplaceDReplace(Sender); //�������� ������� ReplaceDReplace
}
//---------------------------------------------------------------------------

//-------------------������� �������-----------------------------------------
void __fastcall TNotePadF::GoToClick(TObject *Sender)
{
FName;
}
//---------------------------------------------------------------------------

//-------------------������� �������� ��------------------------------------
void __fastcall TNotePadF::Selete_AllClick(TObject *Sender)
{
	MText->SelectAll();
}
//---------------------------------------------------------------------------

//-------------------������� ������� � ����----------------------------------
void __fastcall TNotePadF::Time_DateClick(TObject *Sender)
{
    MText->Lines->Add(Time().FormatString("hh:mm") + " " + Date());
}
//---------------------------------------------------------------------------

//------------------------������� �������� ����------------------------------
void __fastcall TNotePadF::Word_WrapClick(TObject *Sender)
{
	if(Word_Wrap->Checked == True){
		MText->WordWrap = false; //��������� ������� ������
		Word_Wrap->Checked = false; //������ ���������� ������
		MText->ScrollBars = ssBoth; //������ Scroll Bar � MText(Memo1)
	}else{ //���� if �� �����������, �� �������� ������� � ������� Scroll Bar
		MText->WordWrap = true; //�������� ������� ������
		Word_Wrap->Checked = true; //������ �������� ������
		MText->ScrollBars = ssVertical; //������ Scroll Bar � MText(Memo1)
	 }
}
//---------------------------------------------------------------------------

void __fastcall TNotePadF::FontClick(TObject *Sender)
{
	if(FontD->Execute()){MText->Font = FontD->Font;}; //�������� ���������� ���� ������
}
//---------------------------------------------------------------------------

//--------------------������� ���������� ������------------------------------
void __fastcall TNotePadF::to_EnlargeClick(TObject *Sender)
{
	if(Size < 500){ //��������� ��������, ���� �� �� ���� ����� 500
		MText->Font->Size += 1; //���������� 1 ������� � ���������
		StatusBar->Panels->Items[2]->Text = IntToStr(Size += 10) + "%"; //������� � ������ ��� ����������
	}
}
//---------------------------------------------------------------------------

//--------------------������� ���������� ������------------------------------
void __fastcall TNotePadF::ReduceClick(TObject *Sender)
{
	if (Size > 10){ //�������� ��������
		MText->Font->Size -= 1; //�������� �������� ����� �� -1
		StatusBar->Panels->Items[2]->Text = IntToStr(Size -= 10) + "%"; //������� ���� � ��������� � %
	}
}
//---------------------------------------------------------------------------

//--------------------������� �������������� ������--------------------------
void __fastcall TNotePadF::Restore_to_defaultClick(TObject *Sender)
{
	Size = 100; //����������� 100% ������
	MText->Font->Size = 11; //��������������� ������ ������
	StatusBar->Panels->Items[2]->Text = "100%"; //������� ���� � ������ ���
}
//---------------------------------------------------------------------------

//-------------------������� ����������� ������ ����-------------------------
void __fastcall TNotePadF::Status_BarClick(TObject *Sender)
{
	if(Status_Bar->Checked == true){ //��������� ������� �� ������
		StatusBar->Visible = false; //������ ��� ���������
		Status_Bar->Checked = false; //������ ������ �� ��������
		MText->Height = NotePadF->Height - 60; //������� MText(Memo1) ����
	}else{
		StatusBar->Visible = true; //������� ��� �������
		Status_Bar->Checked = true; //������ ������ ��������
		MText->Height = NotePadF->Height - 78; //��������� MText(Memo1) �����
	 }
}
//---------------------------------------------------------------------------

//---------------------������� �������� �������------------------------------
void __fastcall TNotePadF::Viwe_HelpClick(TObject *Sender)
{
	ShellExecute(Handle, L"open", L"Help.html", NULL, NULL, SW_RESTORE); //��������� ���� �� ��������
}
//---------------------------------------------------------------------------

//-----------------------����� � ���������-----------------------------------
void __fastcall TNotePadF::About_the_ProgrammClick(TObject *Sender)
{
	About_the_program->ShowModal(); //�������� ����� About
}
//---------------------------------------------------------------------------

//---------------------------������ �����------------------------------------
void __fastcall TNotePadF::ReviewClick(TObject *Sender)
{
	AnsiString URL = "https://forms.gle/69xTfH7FC8xgxjrf6";
	ShellExecute(Handle, L"open", String(URL).c_str(), NULL, NULL, SW_SHOWDEFAULT);
}
//---------------------------------------------------------------------------

//-------------------������� ����������� ������� �������---------------------
void __fastcall TNotePadF::MTextKeyUp(TObject *Sender, WORD &Key, TShiftState Shift)
{
	PosCarriage();
}
//---------------------------------------------------------------------------

//------------------��������� � ������� �� MText-----------------------------
void __fastcall TNotePadF::MTextChange(TObject *Sender)
{
    Saved = false;
	PosCarriage();
	Undo->Enabled = true;

	if(!Saved && MText->Modified == true && FName != "\0"){ //�������� �� ��������� ������
		Caption = "*" + FName + " � �������"; //��������� ������ *
	}

	Undo->Enabled = true;
	Cut->Enabled = true;
	Copy->Enabled = true;
	Delete->Enabled = true;
	Find->Enabled = true;

}
//---------------------------------------------------------------------------

//----------------------------������� �� MText-------------------------------
void __fastcall TNotePadF::MTextClick(TObject *Sender)
{
	PosCarriage();
}
//---------------------------------------------------------------------------

void __fastcall TNotePadF::NightSClick(TObject *Sender)
{
	if (NightS->Checked == true) {
		NightS->Checked = false;
		MText->Color = clWindow;
		MText->Font->Color = clBlack;
	}
	else{
		NightS->Checked = true;
		MText->Color = clWindowText;
		MText->Font->Color = clWhite;
	}

}
//---------------------------------------------------------------------------

