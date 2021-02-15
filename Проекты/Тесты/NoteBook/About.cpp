//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "About.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TAbout_the_program *About_the_program;
//---------------------------------------------------------------------------
__fastcall TAbout_the_program::TAbout_the_program(TComponent* Owner)
        : TForm(Owner)
{
}
//---------------------------------------------------------------------------
void __fastcall TAbout_the_program::exClick(TObject *Sender)
{
        Close();
}
//---------------------------------------------------------------------------
