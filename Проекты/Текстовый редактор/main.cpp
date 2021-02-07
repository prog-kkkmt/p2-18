//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "main.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TTE *TE;
//---------------------------------------------------------------------------
__fastcall TTE::TTE(TComponent* Owner)
        : TForm(Owner)
{
	N = 100;
}

void __fastcall TTE::FormResize(TObject *Sender)
{
        TE->DoubleBuffered = true;
	MText->Height=TE->Height/2;
        MText->Width=TE->Width/2;
}
//---------------------------------------------------------------------------

void __fastcall TTE::CopyClick(TObject *Sender)
{
        MText->CopyToClipboard();
        if(Clipboard()->HasFormat(CF_TEXT)){ Paste->Enabled = true; }
        else{ Paste->Enabled = false; }
}
//---------------------------------------------------------------------------

void __fastcall TTE::PasteClick(TObject *Sender)
{
        MText->PasteFromClipboard();
}
//---------------------------------------------------------------------------

void __fastcall TTE::ClearClick(TObject *Sender)
{
        MText->CutToClipboard();
}
//---------------------------------------------------------------------------

void __fastcall TTE::BackClick(TObject *Sender)
{
        MText->Undo();
}
//---------------------------------------------------------------------------

void __fastcall TTE::OpenClick(TObject *Sender)
{
	if (OpenFile->Execute()){
        FWay = ExtractFileDir(OpenFile->FileName);
        FName = ExtractFileName(OpenFile->FileName);
        FWayName = ExtractFilePath(OpenFile->FileName);
		Caption = FName + " - Блокнот";
		MText->Lines->LoadFromFile(OpenFile->FileName);
                Way->Caption = FWay;
                Save->Enabled = true;
        }
}
//---------------------------------------------------------------------------

void __fastcall TTE::DelClick(TObject *Sender)
{
	MText->ClearSelection();

}
//---------------------------------------------------------------------------

void __fastcall TTE::MTextChange(TObject *Sender)
{
        Xstr = "|Строка ";
	Ystr = ", столбец ";
	X = MText->Perform(EM_LINEFROMCHAR, MText->SelStart, 0);
	Y = MText->SelStart - MText->Perform(EM_LINEINDEX, X, 0);
		X += 1;
		Y += 1;
	PosXY->Caption = Xstr + X + Ystr + Y;
}
//---------------------------------------------------------------------------

void __fastcall TTE::font1Click(TObject *Sender)
{
	if(Font->Execute()){MText->Font = Font->Font;}
}
//---------------------------------------------------------------------------

void __fastcall TTE::SaveClick(TObject *Sender)
{
        MText->Lines->SaveToFile(FWayName+FName);
}
//---------------------------------------------------------------------------

void __fastcall TTE::SaveAsClick(TObject *Sender)
{
	if(MText->Lines->Count > 0 && SaveFile->Execute()){
           MText->Lines->SaveToFile(SaveFile->FileName);
           Save->Enabled = true;
        }
}

//---------------------------------------------------------------------------

void __fastcall TTE::WordWrapClick(TObject *Sender)
{
        TE->DoubleBuffered = true;
	if(WordWrap->Checked == true){
		MText->WordWrap = false;
		WordWrap->Checked = false;
		MText->ScrollBars = ssBoth;
	}else{
		MText->WordWrap = true;
		WordWrap->Checked = true;
		MText->ScrollBars = ssVertical;
	 }
}

//---------------------------------------------------------------------------

void __fastcall TTE::to_EnlargeClick(TObject *Sender)
{
    if (N < 500){
		MText->Font->Size += 1;
		Size_Font->Caption ="|" + IntToStr(N+=10) + "%";
    }
}
//---------------------------------------------------------------------------

void __fastcall TTE::ReduceClick(TObject *Sender)
{
    if (N > 10){
        MText->Font->Size -= 1;
        Size_Font->Caption ="|" + IntToStr(N-=10) + "%";
    }
}
//---------------------------------------------------------------------------

void __fastcall TTE::Restore_default_scaleClick(TObject *Sender)
{
   MText->Font->Size = 12;
}
//---------------------------------------------------------------------------


void __fastcall TTE::Status_barClick(TObject *Sender)
{
   if(Status_bar->Checked == true){
        PosXY->Visible = false;
        Size_Font->Visible = false;
        Status_bar->Checked = false;
        Way->Visible = false;
        MText->Height = TE->Height - 60;
    }else{
        PosXY->Visible = true;
        Size_Font->Visible = true;
        Status_bar->Checked = true;
        Way->Visible = true;
        MText->Height = TE->Height - 75;
     }
}
//---------------------------------------------------------------------------

void __fastcall TTE::ExitClick(TObject *Sender)
{
        Clipboard()->Clear();
        Close();
}
//---------------------------------------------------------------------------

void __fastcall TTE::TTEClose(TObject *Sender, TCloseAction &Action)
{
        Clipboard()->Clear();

        if(FName == "\0" && MText->Lines->Count > 0 && MessageDlg("Вы хотите сохранить данные?",
            mtConfirmation  , TMsgDlgButtons() << mbNo << mbYes, 0) == mrYes && SaveFile->Execute()){
			MText->Lines->SaveToFile(SaveFile->FileName);
        }else if(FName != "\0" && MText->Lines->Count > 0 && MessageDlg("Вы хотите сохранить изменения в файле " + FWay + "\\" + FName,
                        mtConfirmation  , TMsgDlgButtons() << mbNo << mbYes, 0) == mrYes){
                        MText->Lines->SaveToFile(FWayName+FName);
         }
}
//---------------------------------------------------------------------------







