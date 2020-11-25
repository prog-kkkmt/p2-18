#ifndef Unit1H
#define Unit1H
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
#include <Menus.hpp>
#include <Grids.hpp>
#include <Buttons.hpp>
#include <memory>

#include <iostream>
#include <fstream>
#include <string>

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#include <Menus.hpp>

using namespace std;

//---------------------------------------------------------------------------
class TForm1 : public TForm
{
__published:	// IDE-managed Components
        TButton *BTShowList;
        TButton *BTExit;
        TButton *BTAddAuthor;
        TButton *BTdelauthor;
        TButton *BTFindAuthor;
        TButton *BTsortAuthor;
        TButton *BTsortBook;
        TButton *BTsortYear;
        TMemo *Memo1;
        TEdit *Edit1;
        TButton *BTFindBook;

        void __fastcall BTExitClick(TObject *Sender);
        void __fastcall BTAddAuthorClick(TObject *Sender);
        void __fastcall BTdelauthorClick(TObject *Sender);
        void __fastcall BTShowListClick(TObject *Sender);
        void __fastcall BTsortAuthorClick(TObject *Sender);
        void __fastcall BTsortBookClick(TObject *Sender);
        void __fastcall BTsortYearClick(TObject *Sender);
        void __fastcall BTFindAuthorClick(TObject *Sender);
        void __fastcall BTFindBookClick(TObject *Sender);
        
private:	// User declarations
public:		// User declarations
      __fastcall TForm1(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TForm1 *Form1;
//---------------------------------------------------------------------------
#endif
