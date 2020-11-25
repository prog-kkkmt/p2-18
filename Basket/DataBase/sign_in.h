//---------------------------------------------------------------------------

#ifndef sign_inH
#define sign_inH
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
#include <ExtCtrls.hpp>
#include <jpeg.hpp>
//---------------------------------------------------------------------------
class TFAuthorization : public TForm
{
__published:	// IDE-managed Components
        TImage *Fon;
        TLabel *sign_in;
        TLabel *sign_up;
        TLabel *Label1;
        TLabel *Label2;
        TEdit *EDpassword;
        TEdit *EDlogin;
        TButton *BTsign_in;
        TLabel *Label3;
        TLabel *Label4;

private:	// User declarations
public:		// User declarations
        __fastcall TFAuthorization(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TFAuthorization *FAuthorization;
//---------------------------------------------------------------------------
#endif
