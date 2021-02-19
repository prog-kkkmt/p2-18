//---------------------------------------------------------------------------

#ifndef mainH
#define mainH
//---------------------------------------------------------------------------
#include <Classes.hpp>
#include <Clipbrd.hpp>
#include <Controls.hpp>
#include <StdCtrls.hpp>
#include <Forms.hpp>
#include <ComCtrls.hpp>
#include <Dialogs.hpp>
#include <Menus.hpp>
#include <locale>

//---------------------------------------------------------------------------
class TNP : public TForm
{
__published:	// IDE-managed Components                                       //* - функции и кнопки меню
        TOpenDialog *OpenFile;                                                  //Панель открытия файлов
        TSaveDialog *SaveFile;                                                  //Панель Сохранения файлов
        TFontDialog *Font;                                                      //Панель фонта
        TMainMenu *Trey;                                                        //Трей программы
        TMenuItem *File1;                                                       //*
        TMenuItem *Open;                                                        //*
        TMenuItem *Save;                                                        //*
        TMenuItem *Edit2;                                                       //*
        TMenuItem *Back;                                                        //*
        TMenuItem *Format;                                                      //*
        TMenuItem *WordWrap;                                                    //*
        TMenuItem *SaveAs;                                                      //*
        TMenuItem *see;                                                         //*
        TMenuItem *Scale;                                                       //*
        TMenuItem *Clear;                                                       //*
        TMenuItem *Copy;                                                        //*
        TMenuItem *Paste;                                                       //*
        TMenuItem *Del;                                                         //*
        TMenuItem *help;                                                        //*
        TMenuItem *About;                                                       //*
        TLabel *PosXY;                                                          //*
        TMenuItem *font1;                                                       //*
        TMenuItem *to_Enlarge;                                                  //*
        TMenuItem *Reduce;                                                      //*
        TMenuItem *Restore_default_scale;                                       //*
        TMenuItem *Status_bar;                                                  //*
        TLabel *Size_Font;                                                      //Размер шрифта в %
        TMemo *MText;                                                           //Основная текстовая панель
        TLabel *Way;                                                            //Отображает путь файла
        TMenuItem *Exit;                                                        //*
        TMenuItem *Find;                                                        //*
        TMenuItem *SelectAll;                                                   //*
        TFindDialog *FindD;                                                     //Функция поиска в файле
        TReplaceDialog *ReplaceD;                                               //Функция замены в файле
        TMenuItem *Replace;                                                     //*
        TMenuItem *Find_Next;
        TStatusBar *StatusBar;                                                   //*
        void __fastcall OpenClick(TObject *Sender);                             //Вызывает операцию открытия окна
        void __fastcall DelClick(TObject *Sender);                              //Функция удаления
        void __fastcall MTextChange(TObject *Sender);                           //Функция активности на основном тексте
        void __fastcall font1Click(TObject *Sender);                            //Функция фонта
        void __fastcall SaveClick(TObject *Sender);                             //Функция Сохранить
        void __fastcall SaveAsClick(TObject *Sender);                           //Функция Сохранить как
        void __fastcall WordWrapClick(TObject *Sender);                         //Функция переноса слов
        void __fastcall TTEClose(TObject *Sender, TCloseAction &Action);        //Функция закрытия окна
        void __fastcall to_EnlargeClick(TObject *Sender);                       //Функция увеличения шрифта
        void __fastcall ReduceClick(TObject *Sender);                           //Функция уменьшения шрифта
        void __fastcall Restore_default_scaleClick(TObject *Sender);            //Функция восстановления размера шрифа
        void __fastcall Status_barClick(TObject *Sender);                       //Отображение статус бара
        void __fastcall ExitClick(TObject *Sender);                             //Кнопка выхода
        void __fastcall CopyClick(TObject *Sender);                             //Кнопка копирования
        void __fastcall PasteClick(TObject *Sender);                            //Кнопка Вставить
        void __fastcall ClearClick(TObject *Sender);                            //Кнопка очистки
        void __fastcall BackClick(TObject *Sender);                             //Кнопка UNDO
        void __fastcall FormResize(TObject *Sender);                            //Функция изменения формы
        void __fastcall SelectAllClick(TObject *Sender);                        //Функция выделения всего
        void __fastcall FindClick(TObject *Sender);                             //Кнопка поиска
        void __fastcall FindDFind(TObject *Sender);                             //Функция поиска
        void __fastcall ReplaceDFind(TObject *Sender);                          //Функция замены
        void __fastcall ReplaceDReplace(TObject *Sender);                       //Функция замены всего
        void __fastcall ReplaceClick(TObject *Sender);                          //Кнопка заменить
        void __fastcall Find_NextClick(TObject *Sender);                        //Кнопка поиска далее
        void __fastcall AboutClick(TObject *Sender);                            //Кнопка о программе
        void __fastcall MTextKeyDown(TObject *Sender, WORD &Key,
          TShiftState Shift);
        void __fastcall MTextKeyUp(TObject *Sender, WORD &Key,
          TShiftState Shift);
        void __fastcall StatusBarResize(TObject *Sender);
private:// User declarations
public:// User declarations
        __fastcall TNP(TComponent* Owner);
        int N, X, Y, FoundAt, StartPos, ToEnd;                                  //Переменные
        AnsiString FWay, FName, FileName, FPath, Xstr, Ystr;                    //
        String Str;                                                             //
        Boolean SaveF;                                                          //Переменная сохранения

};
//---------------------------------------------------------------------------
extern PACKAGE TNP *NP;
//---------------------------------------------------------------------------
#endif
