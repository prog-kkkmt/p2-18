//---------------------------------------------------------------------------

#ifndef CChatH
#define CChatH
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
#include <ScktComp.hpp>
#include <ComCtrls.hpp>
//---------------------------------------------------------------------------
class TClient : public TForm
{
__published:	// IDE-managed Components
        TEdit *Host;
        TEdit *Port;
        TEdit *Login;
        TEdit *Password;
        TButton *BTlogIn;
        TMemo *MText;
        TEdit *Enter;
        TButton *BTSend;
        TRadioButton *RBTLogIn;
        TRadioButton *RBTRegister;
        TClientSocket *ClientSocket;
        TLabel *Info;
        TRichEdit *REText;
        TButton *BTDisconnect;
        void __fastcall BTlogInClick(TObject *Sender);
        void __fastcall ClientSocketConnect(TObject *Sender, TCustomWinSocket *Socket);
        void __fastcall ClientSocketRead(TObject *Sender, TCustomWinSocket *Socket);
        void __fastcall ClientSocketError(TObject *Sender, TCustomWinSocket *Socket, TErrorEvent ErrorEvent, int &ErrorCode);
        void __fastcall ClientSocketDisconnect(TObject *Sender, TCustomWinSocket *Socket);
        void __fastcall ClientClose(TObject *Sender, TCloseAction &Action);
        void __fastcall BTSendClick(TObject *Sender);
        void __fastcall BTDisconnectClick(TObject *Sender);
private:
        AnsiString msgR;
        AnsiString msgS;
        AnsiString log;
public:		// User declarations
        __fastcall TClient(TComponent* Owner);
};
//---------------------------------------------------------------------------
extern PACKAGE TClient *Client;
//---------------------------------------------------------------------------
#endif
