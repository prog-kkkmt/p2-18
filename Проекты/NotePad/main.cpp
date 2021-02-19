/*------------------------------------------------------------------------------
        Выполнил: Студент ККМТ
        Группа: П2-18
        ФИО: Короленко Иван Романович
//------------------------------------------------------------------------------
        О Программе:
Данная программа создана в C++ Builder 6, скомпилирована и собрана там же.
Программа представляет собой относительно полную копию исходного блокнота Windows,
от компании Microsoft, и имеет полный не отличительный функционал от исходного!

        Комментарии:
// - Описание действия или функции
//** - ранее описывалось значение действия или функции
//*** - ранее объявленно значение действия или функции

        Версия: 15 (Сборка OC 11.12.200a)

//----------------------------------------------------------------------------*/
#include <vcl.h>
#pragma hdrstop

#include "main.h"
#include "About.h"
//------------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TNP *NP;
//--------------------Основная main функция-------------------------------------
__fastcall TNP::TNP(TComponent* Owner)
		: TForm(Owner)
{
        to_Enlarge->ShortCut = TextToShortCut("Ctrl+NUM +");
        Reduce->ShortCut = TextToShortCut("Ctrl+NUM -");
	N = 100;                                                                //N - размер шрифта в %
	SaveF = false;                                                          //Переменная false для сохранения файла
}
//-------------------Функция изменения размера формы----------------------------
void __fastcall TNP::FormResize(TObject *Sender){
	NP->DoubleBuffered = true;                                              //Не знаю почему так, но перестало маргать
	
	MText->Height=NP->Height/2;                                             //Не знаю почему так, но работает
	MText->Width=NP->Width/2;                                               //Не знаю почему так, но работает
}
//--------------------Функция копирования---------------------------------------
void __fastcall TNP::CopyClick(TObject *Sender){
	MText->CopyToClipboard();                                               //Копирует выделенный текст
	if(Clipboard()->HasFormat(CF_TEXT)){ Paste->Enabled = true; }           //Проверяет есть ли скопированный текст
	   else{ Paste->Enabled = false; }                                      //если нет, то запрещает вставить
}
//-------------------Функция вставить-------------------------------------------
void __fastcall TNP::PasteClick(TObject *Sender){
	MText->PasteFromClipboard();                                            //Вставляет ранее скопированный текст
}
//-------------------Функция очистить-------------------------------------------
void __fastcall TNP::ClearClick(TObject *Sender){
	MText->CutToClipboard();                                                //очищает MText(Memo1)
}
//-------------------Функция выделения------------------------------------------
void __fastcall TNP::SelectAllClick(TObject *Sender){
	MText->SelectAll();                                                     //Выделяет всё
}
//-------------------Функция отмены(UNDO)---------------------------------------
void __fastcall TNP::BackClick(TObject *Sender){
	MText->Undo();                                                          //UNDO
}
//------------------Кнопка открытия файла---------------------------------------
void __fastcall TNP::OpenClick(TObject *Sender){

        Paste->Enabled = false;                                                 //Закрывает кнопку вставить
        Find_Next->Enabled = false;                                             //Закрывает кнопку поиск далее

        //Проверяет Пустто ли в название при открытии и пустая ли строка
	if(FName == "\0" && MText->Lines->Count > 0 && MessageDlg("Вы хотите сохранить данные?",
		mtConfirmation  , TMsgDlgButtons() << mbNo << mbYes, 0) == mrYes && SaveFile->Execute()){
		
		MText->Lines->SaveToFile(SaveFile->FileName);
	}

	if (OpenFile->Execute()){                                               //Вызывает меню открытия файла
		FWay = ExtractFileDir(OpenFile->FileName);                      //Хранит путь файла
		FName = ExtractFileName(OpenFile->FileName);                    //Хранит Название файла
		FPath = ExtractFilePath(OpenFile->FileName);                    //Хранит путь файла с /

		Caption = FName + " - Блокнот";                                 //Меняет название формы
		
		MText->Lines->LoadFromFile(OpenFile->FileName);                 //Выводит содержимое с файла в MText(Memo1)

		StatusBar->Panels->Items[0]->Text = FWay;
		//Way->Caption = FWay;                                            //Выводит в статут бар путь
		Save->Enabled = true;                                           //Разрешает сохранения
		SaveF = false;                                                  //Сохранение не было
	}
}
//-----------------Кнопка удаления/Вырезания------------------------------------
void __fastcall TNP::DelClick(TObject *Sender){
	MText->ClearSelection();                                                //Вырезает выделенный текст
}
//------------------Функция позиции каретки-------------------------------------
void __fastcall TNP::MTextChange(TObject *Sender){
	Xstr = "Строка ";                                                      //X
	Ystr = ", столбец ";                                                    //Y
	X = MText->Perform(EM_LINEFROMCHAR, MText->SelStart, 0);                //Присвоение X
	Y = MText->SelStart - MText->Perform(EM_LINEINDEX, X, 0);               //Присвоение Y
		X += 1;                                                         //Не знаю почему так, но оно работает
		Y += 1;                                                         //Не знаю почему так, но оно работает
	//PosXY->Caption = Xstr + X + Ystr + Y;                                   //Вывод в статус бар информацию об X и Y
        StatusBar->Panels->Items[1]->Text = Xstr + X + Ystr + Y;
}
//------------------Функция вызова фонта----------------------------------------
void __fastcall TNP::font1Click(TObject *Sender){
	if(Font->Execute()){MText->Font = Font->Font;}                          //Открывает и выводит меню фонта, меняя ее если нужно
}
//------------------Функция Сохранения------------------------------------------
void __fastcall TNP::SaveClick(TObject *Sender){
	MText->Lines->SaveToFile(FPath+FName);                                  //Берёт путь и Имя файла с ранее записанных данных при открытие файла
	SaveF = true;                                                           //Ставит положение сохранения в true
}
//-----------------Функция сохранить как==--------------------------------------
void __fastcall TNP::SaveAsClick(TObject *Sender){
	if(SaveF == false && MText->Lines->Count > 0 && SaveFile->Execute()){   //Проверка на сохранение, на не пустую строку и октрывает диалоговое окно сохранения
	   MText->Lines->SaveToFile(SaveFile->FileName);                        //Сохраняет весь текст в файл

	   FWay = ExtractFileDir(SaveFile->FileName);                           //**
	   FName = ExtractFileName(SaveFile->FileName);                         //**
	   FPath = ExtractFilePath(SaveFile->FileName);                         //**
	   Caption = FName + " - Блокнот";                                      //**

           StatusBar->Panels->Items[0]->Text = FWay;
	  // Way->Caption = FWay;                                                 //**
	   Save->Enabled = true;                                                //**
	   SaveF = true;                                                        //**
	}
}
//-------------------Кнопка переноса слов---------------------------------------
void __fastcall TNP::WordWrapClick(TObject *Sender){
	NP->DoubleBuffered = true;                                              //**
	if(WordWrap->Checked == true){                                          //Проверяет состояние кнопки
		MText->WordWrap = false;                                        //Отключает перенос строки
		WordWrap->Checked = false;                                      //Делает неактивной кнопку
		MText->ScrollBars = ssBoth;                                     //Меняет Scroll Bar у MText(Memo1)
	}else{                                                                  //если if не выполнилось, то включает перенос и убирает Scroll Bar
		MText->WordWrap = true;
		WordWrap->Checked = true;
		MText->ScrollBars = ssVertical;
	 }
}
//-----------------Кнопка увеличения шрифа--------------------------------------
void __fastcall TNP::to_EnlargeClick(TObject *Sender){
	if (N < 500){                                                           //Проверяет значения, чтоб то не было более 500
		MText->Font->Size += 1;                                         //Прибавляет 1 еденицу к исходному
		//Size_Font->Caption ="|" + IntToStr(N+=10) + "%";                //Выводит Ифно о состоянии в %
                StatusBar->Panels->Items[2]->Text = IntToStr(N+=10) + "%";
	}
}
//-----------------Кнопка уменьшение шрифта-------------------------------------
void __fastcall TNP::ReduceClick(TObject *Sender){
	if (N > 10){                                                            //Проверка значения
		MText->Font->Size -= 1;                                         //Убавляет исходный шрифт на -1
		//Size_Font->Caption ="|" + IntToStr(N-=10) + "%";                //Выводит Ифно о состоянии в %
                StatusBar->Panels->Items[2]->Text = IntToStr(N-=10) + "%";
	}
}
//-----------------Кнопка восстановления размера шрифта-------------------------
void __fastcall TNP::Restore_default_scaleClick(TObject *Sender){
        N = 100;
        MText->Font->Size = 12;                                                      //Восстанавливает размер шрифта
        StatusBar->Panels->Items[2]->Text = "100%";
}
//-----------------Кнопка отображения статуст бара------------------------------
void __fastcall TNP::Status_barClick(TObject *Sender){
	if(Status_bar->Checked == true){                                        //Проверяет активна ли кнопка
		//PosXY->Visible = false;                                         //***Выключает Статутс бар
		//Size_Font->Visible = false;                                     //***
                //Way->Visible = false;                                           //***
                StatusBar->Visible = false;
		Status_bar->Checked = false;                                    //Делает кнопку не активной
		MText->Height = NP->Height - 60;                                //Смешает MText(Memo1) вниз
	}else{
		//PosXY->Visible = true;                                          //***Включает статус бар
		//Size_Font->Visible = true;                                      //***
                //Way->Visible = true;                                            //***
                StatusBar->Visible = true;
		Status_bar->Checked = true;                                     //Делает кнопку активной
		MText->Height = NP->Height - 75;                                //Поднимает MText(Memo1) вверх
	 }
}
//----------------Кнопка выхода-------------------------------------------------
void __fastcall TNP::ExitClick(TObject *Sender){
	if(SaveF == true){                                                      //Проверяет сохранен ли файл
		Close();                                                        //Закрывает программу
	}else if(MText->Lines->Count > 0 && MessageDlg("Вы хотите сохранить изменения в файле " + FPath + FName,
			mtConfirmation  , TMsgDlgButtons() << mbNo << mbYes, 0) == mrYes){
		MText->Lines->SaveToFile(FPath+FName);                          //Сохраняет с вопросом о сохранение
		Application->Title = "Блокнот";                                 //Название формы
	 }


}
//--------------------Функция при нажатие на кнопку закрытия--------------------
void __fastcall TNP::TTEClose(TObject *Sender, TCloseAction &Action){
	if(SaveF == false && FName == "\0" && MText->Lines->Count > 0 && MessageDlg("Вы хотите сохранить данные?",
		mtConfirmation  , TMsgDlgButtons() << mbNo << mbYes, 0) == mrYes && SaveFile->Execute()){
		MText->Lines->SaveToFile(SaveFile->FileName);                   //***
	}else if(SaveF != true && FName != "\0" && MText->Lines->Count > 0 && MessageDlg("Вы хотите сохранить изменения в файле " + FWay + "\\" + FName,
				mtConfirmation  , TMsgDlgButtons() << mbNo << mbYes, 0) == mrYes){
				MText->Lines->SaveToFile(FPath+FName);          //***
	 }
	SaveF = false;                                                          //***
}
//--------------------Кнопка поиска---------------------------------------------
void __fastcall TNP::FindClick(TObject *Sender){
	FindD->FindText = MText->SelText;                                       //Выделяет весь текст
	FindD->Execute();                                                       //Передает в функцию FindDFind
}
//-------------------Функция поиска---------------------------------------------
void __fastcall TNP::FindDFind(TObject *Sender){
	StartPos = MText->SelStart;                                             //Позиция старта поиска (Положение каретки)
        Find_Next->Enabled = true;                                              //Делает активную кнопку искать далее

	if(MText->SelLength)                                                    //Проверяте где каретка
		StartPos += MText->SelLength;                                   //Даёт значение каретке
		ToEnd = MText->Text.Length() - StartPos;                        //Ищет конец текста

	if(FindD->Options.Contains(frMatchCase))                                //Условия и кнопки в поиске
		FoundAt = StartPos + MText->Text.SubString(StartPos+1, ToEnd).Pos(FindD->FindText);

        //***
	else FoundAt = StartPos + MText->Text.SubString(StartPos+1, ToEnd).LowerCase().Pos(FindD->FindTextA.LowerCase());

	if(FoundAt != StartPos){                                                //***
		MText->SetFocus();                                              //Ставит фокус на активное окно MText(Memo1)
		MText->SelStart = FoundAt-1;                                    //Каретка в исходной позиции
		MText->SelLength = FindD->FindText.Length();                    //***
	}else ShowMessage("Не удалось найти \""  + FindD->FindText + "\"");     //***
		Application->Title = "Блокнот";                                 //***
}
//-----------------Функция замены слов------------------------------------------
void __fastcall TNP::ReplaceDFind(TObject *Sender){
	FoundAt = 0;                                                            //Позиция каретки в начало
	StartPos = MText->SelStart;                                             //***

	if(MText->SelStart)                                                     //***
			StartPos += MText->SelLength;                           //***
			ToEnd = MText->Text.Length() - StartPos;                //***

	if(FindD->Options.Contains(frMatchCase))                                //***
		FoundAt = StartPos + MText->Text.SubString(StartPos+1, ToEnd).Pos(ReplaceD->FindText);//***
	else FoundAt = StartPos + MText->Text.SubString(StartPos+1, ToEnd).LowerCase().Pos(ReplaceD->FindTextA.LowerCase());
		
	if(FoundAt != StartPos){                                                //***
		MText->SetFocus();                                              //***
		MText->SelStart = FoundAt-1;                                    //***
		MText->SelLength = ReplaceD->FindText.Length();                 //***
	}else{
		ShowMessage("Не удалось найти \""  + ReplaceD->FindText + "\"");//***
		Application->Title = "Блокнот";                                 //***
		MText->SetFocus();                                              //***
		MText->CaretPos = Point(0, 0);                                  //Позиция каретки на 0 0
		return;
	 }
	 
	if(ReplaceD->Options.Contains(frReplaceAll))                            //В случае нажатие кнопки Заменить всё
		ReplaceDReplace(Sender);                                        //Вызывает функцию ReplaceDReplace
}
//--------------------Функция замены ALL----------------------------------------
void __fastcall TNP::ReplaceDReplace(TObject *Sender){
	if (MText->SelText != "")                                               //проверяет есть ли выделенный текст
			MText->SelText = ReplaceD->ReplaceTextA;                //***
	
	else if(ReplaceD->Options.Contains(frReplace)){                         //***
		ShowMessage("Не удалось найти\"" + ReplaceD->FindTextA +  "\"");//***
		Application->Title = "Блокнот";                                 //***
		return;
	}

	if(ReplaceD->Options.Contains(frReplaceAll))                            //Возвращается в исходную функцию
			ReplaceDFind(Sender);                                   //***
}
//------------------Кнопка замены-----------------------------------------------
void __fastcall TNP::ReplaceClick(TObject *Sender){
	ReplaceD->FindTextA = MText->SelText;
	ReplaceD->Execute();
}
//------------------Кнопка поиска далее-----------------------------------------
void __fastcall TNP::Find_NextClick(TObject *Sender){
        StartPos = MText->SelStart;                                             //***

	if(MText->SelLength)                                                    //***
		StartPos += MText->SelLength;                                   //***
		ToEnd = MText->Text.Length() - StartPos;                        //***

	if(FindD->Options.Contains(frMatchCase))
		FoundAt = StartPos + MText->Text.SubString(StartPos+1, ToEnd).Pos(FindD->FindText);//***

        //***
	else FoundAt = StartPos + MText->Text.SubString(StartPos+1, ToEnd).LowerCase().Pos(FindD->FindTextA.LowerCase());

	if(FoundAt != StartPos){                                                //***
		MText->SetFocus();                                              //***
		MText->SelStart = FoundAt-1;                                    //***
		MText->SelLength = FindD->FindText.Length();                    //***
	}else ShowMessage("Не удалось найти \""  + FindD->FindText + "\"");     //***
		Application->Title = "Блокнот";                                 //***
}
//------------------Кнопка о программе------------------------------------------
void __fastcall TNP::AboutClick(TObject *Sender){
        About_the_program->ShowModal();                                         //Вызывает форму About_The_program
}
//------------------------------------------------------------------------------
void __fastcall TNP::MTextKeyDown(TObject *Sender, WORD &Key,
      TShiftState Shift){
        	Xstr = "Строка ";                                               //X
	        Ystr = ", столбец ";                                            //Y
	X = MText->Perform(EM_LINEFROMCHAR, MText->SelStart, 0);                //Присвоение X
	Y = MText->SelStart - MText->Perform(EM_LINEINDEX, X, 0);               //Присвоение Y
		X += 1;                                                         //Не знаю почему так, но оно работает
		Y += 1;                                                         //Не знаю почему так, но оно работает
	//PosXY->Caption = Xstr + X + Ystr + Y;                                   //Вывод в статус бар информацию об X и Y
        StatusBar->Panels->Items[1]->Text = Xstr + X + Ystr + Y;
}
//---------------------------------------------------------------------------
void __fastcall TNP::MTextKeyUp(TObject *Sender, WORD &Key,
      TShiftState Shift){
        	Xstr = "Строка ";                                               //X
	        Ystr = ", столбец ";                                            //Y
	X = MText->Perform(EM_LINEFROMCHAR, MText->SelStart, 0);                //Присвоение X
	Y = MText->SelStart - MText->Perform(EM_LINEINDEX, X, 0);               //Присвоение Y
		X += 1;                                                         //Не знаю почему так, но оно работает
		Y += 1;                                                         //Не знаю почему так, но оно работает
	//PosXY->Caption = Xstr + X + Ystr + Y;
        StatusBar->Panels->Items[1]->Text = Xstr + X + Ystr + Y;
}
//---------------------------------------------------------------------------

void __fastcall TNP::StatusBarResize(TObject *Sender)
{
    StatusBar->Panels->Items[0]->Width = NP->Width/2;
}
//---------------------------------------------------------------------------

