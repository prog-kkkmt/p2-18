//------------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "CChat.h"
//------------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TClient *Client;
//------------------------------------------------------------------------------
                        /*Основная функция окна*/
//------------------------------------------------------------------------------
__fastcall TClient::TClient(TComponent* Owner)
        : TForm(Owner)
{
}
//------------------------------------------------------------------------------
                  /*Функция Авторизации и Регистрации*/
//------------------------------------------------------------------------------
void __fastcall TClient::BTlogInClick(TObject *Sender)                          //Функция нажатия на кнопку CONNECT
{
    if(RBTLogIn->Checked){                                                      //Проверка активности радиокнопки авторизация
        ClientSocket->Port = Port->Text.ToInt();                                //Заполнение данных о Порте
        ClientSocket->Host = Host->Text;                                        //Заполнение данных о адрессе
        ClientSocket->Active = true;                                            //Активация клиента и открытие порта

        Host->Enabled = false;                                                  //Блокировка использования и редоктирование поля Host
        Port->Enabled = false;                                                  //Блокировка использования и редоктирование поля Port
        Login->Enabled = false;                                                 //Блокировка использования и редоктирование поля Логина
        Password->Enabled = false;                                              //Блокировка использования и редоктирование поля Пароля
        BTlogIn->Enabled = false;                                               //Блокировка использования и редоктирование кнопки Connect
        RBTRegister->Enabled = false;                                           //Блокировка использования и редоктирование радиокнопки Регистрации

        Application->Title="INFO";                                              //Задает название появившегося окна ShowMessage
        ShowMessage("Authorization...");                                        //Окно сообщения Авторизации
        ClientSocket->Socket->SendText("/login " + Login->Text + " " + Password->Text + "\n");//Функия передачи данныз серверу
    }

    if (RBTRegister->Checked){                                                  //Проверка активности радиокнопки регестрации
        ClientSocket->Port = Port->Text.ToInt();                                //Заполнение данных о Порте
        ClientSocket->Host = Host->Text;                                        //Заполнение данных о адрессе
        ClientSocket->Active = true;                                            //Активация клиента и открытие порта

        Host->Enabled = false;                                                  //Блокировка использования и редоктирование поля Host
        Port->Enabled = false;                                                  //Блокировка использования и редоктирование поля Port
        Login->Enabled = false;                                                 //Блокировка использования и редоктирование поля Логина
        Password->Enabled = false;                                              //Блокировка использования и редоктирование поля Пароля
        BTlogIn->Enabled = true;                                                //Блокировка использования и редоктирование кнопки Connect
        RBTRegister->Enabled = false;                                           //Блокировка использования и редоктирование радиокнопки Регистрации

        Application->Title="INFO";                                              //Задает название появишегося окна ShowMessage
        ShowMessage("Registration...");                                         //Окно сообщения Регистрации
        ClientSocket->Socket->SendText("/reg " + Login->Text + " " + Password->Text + "\n");//Функция передачи данных серверу
    }
}
//------------------------------------------------------------------------------
           /*Функция чтения данных отпревленные с сервера->клиенту*/
//------------------------------------------------------------------------------
void __fastcall TClient::ClientSocketRead(TObject *Sender, TCustomWinSocket *Socket)
{
    AnsiString Time = Now().FormatString("[hh:nn] ");                           //Создание нового объекта для хранения даты

    log = Login->Text;                                                          //log - хранит данные введённые с поля Login
    msgR = Socket->ReceiveText();                                               //msgR - Хранит всю строку которую принял от сервера
    int word = msgR.AnsiPos(log);                                               //word - хранит данные о позиции слов хранящиеся в log

    if (ClientSocket->Active == true && word != 0){                             //Проверка активности клиента и имени введенного сообщения для замены цвета текста!
        if (Socket->Connected == true){                                         //Проверка соеденения клиента с сокетами
            for(int i = 1; i <= msgR.Length(); i++){                            //Проверка текста и разбитие его по строчно
                if(msgR[i] == '\n'){                                            //Проверяет введенный принятый текст на \n\t\b и уберает лишние \n\t\b
                    msgR.Delete(i--, 1);                                        //Удаляет лишние \n\t\b, если таковые имеются
                   // MText->Lines->Add(Time + msgR);                           //Вывод информации с Временем и текстом в Memo
                    REText->SelAttributes->Color=clAqua;                        //Задает цвет текста в RichEdit
                    REText->Lines->Add(Time + msgR);                            //Выводит сообщение с Временем и текстом в RichEdit
                }
            }
        }
    }
    else {                                                                      //Финальная проверка принятого текста с сервера
        for(int i = 1; i <= msgR.Length(); i++){                                //Проверка текста и разбитие его по строчно
            if(msgR[i] == '\n'){                                                //Удаляет лишние \n\t\b, если таковые имеются
                msgR.Delete(i--, 1);                                            //Вывод информации с Временем и текстом в Memo
              //MText->Lines->Add(Time + msgR);                                 //Задает цвет текста в RichEdit
                REText->SelAttributes->Color=clLime;                            //Выводит сообщение с Временем и текстом в RichEdit
                REText->Lines->Add(Time + msgR);
            }
        }
     }

}
//------------------------------------------------------------------------------
                 /*Функция отправки сообщение на сервер*/
//------------------------------------------------------------------------------
void __fastcall TClient::BTSendClick(TObject *Sender)
{
    msgS = Enter->Text;                                                         //msgS- введенная строка в поля Enter(Edit)
    if (msgS != ""){                                                            //Проверяет строку на наличие слов, цифр, любого текста
        ClientSocket->Socket->SendText("/msgToAll " + msgS + "\n");             //Если текст не пустой то отправляет его на сервер
        Enter->Clear();                                                         //Чистит поле Enter для дальнейшего ввода
    }
    else ShowMessage("Empty line / input error!");                              //В случае неудачной попытки ввода или сткрока ввода была пустой!

}
//------------------------------------------------------------------------------
                 /*Функция соеденения с клиента к серверу*/
//------------------------------------------------------------------------------
void __fastcall TClient::ClientSocketConnect(TObject *Sender, TCustomWinSocket *Socket)
{
    REText->SelAttributes->Color=clRed;                                         //Задает цвет текста
    REText->Lines->Add("Connecting to server.");                                //Выводит текст о успешном connect!
}
//------------------------------------------------------------------------------
                  /*Функция ошибок сокета и соеденения!*/
//------------------------------------------------------------------------------
void __fastcall TClient::ClientSocketError(TObject *Sender, TCustomWinSocket *Socket, TErrorEvent ErrorEvent, int &ErrorCode)
{
    ShowMessage("Network error №" + IntToStr(ErrorCode));                       //Появляется окно в котором будет написан код ошибки или его номер
    ClientSocket->Active = false;                                               //Деактивирует клиента, освобождая порт
	ErrorCode=0;                                                            //Делает код ошибки 0
}
//------------------------------------------------------------------------------
                   /*Функция закрытия закрытия клиента*/
//------------------------------------------------------------------------------
void __fastcall TClient::ClientClose(TObject *Sender, TCloseAction &Action)     //Функция закрытия закрытия клиента
{
    ClientSocket->Active = false;                                               //Деактивирует клиента
}
//------------------------------------------------------------------------------
                    /*Функция Disconnect клиента*/
//---------------------------------------------------------------------------
void __fastcall TClient::ClientSocketDisconnect(TObject *Sender, TCustomWinSocket *Socket)//Функция Disconnect клиента
{
    ClientSocket->Active = false;                                               //Деактивирует клиента
}
//------------------------------------------------------------------------------
     /*Функция кнопки о Disconnect, для выхода или авторизации/регистрации*/
//------------------------------------------------------------------------------
void __fastcall TClient::BTDisconnectClick(TObject *Sender)
{
    if (MessageDlg("Закрыть приложение?", mtConfirmation, TMsgDlgButtons() << mbYes << mbNo,0) == mrYes)//Диалоговое оно которое спрашивает чего хочет пользователь
    {
        AnsiString DSC = "/exit";                                               //DSC - хранит строку /exit
        Application->Title="INFO";                                              //Задает название ShowMessage
        ClientSocket->Socket->SendText(DSC + "\n");                             //Отправляет на сервер /exit
        ShowMessage("GoodBye...");                                              //Выводит окно GoodBye
        ClientSocket->Active = false;                                           //Деактивирует Клиента
        Close();                                                                //закрывает осно
    }
                                                                                //DSC - хранит строку /exit
    AnsiString DSC = "/exit";                                                   //Задает название ShowMessage
    Application->Title="INFO";                                                  //Отправляет на сервер /exit
    ClientSocket->Socket->SendText(DSC + "\n");                                 //Выводит окно GoodBye
    ClientSocket->Active = false;                                               //Деактивирует Клиента

    Host->Enabled = true;                                                       //Делает активным поле Host
    Port->Enabled = true;                                                       //Делает активным поле Port
    Login->Enabled = true;                                                      //Делает активным поле Login
    Password->Enabled = true;                                                   //Делает активным поле Password
    BTlogIn->Enabled = true;                                                    //Делает активным кнопку CONNECT
    RBTRegister->Enabled = true;                                                //Делает активным радиокнопку Регистрация
}
//------------------------------------------------------------------------------
