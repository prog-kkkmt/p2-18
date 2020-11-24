/*****************************************************************************
* The program was assembled -> Korolenko Ivan Romanich                       *
*                                        Program version -> 2.9              *
*                                               Student -> KKKMT -> P2-18    *
******************************************************************************/
//---------------------------------------------------------------------------
#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
//---------------------------------------------------------------------------
//структура Library
struct Library{
	char name[30];
	char book[30];
	int year;
};

__fastcall TForm1::TForm1(TComponent* Owner)
        : TForm(Owner){
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BTExitClick(TObject *Sender){
        if (-1 == remove ("DBbuff.txt"))                         //удаление файла Buff
        exit(1);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BTShowListClick(TObject *Sender){
        String File = "DataBase.txt";;                           //Откртие файла "DataBase.txt"
        Memo1->Lines->LoadFromFile(File);                        //Вывод данных с файла на Memo1(Экран)
}
//---------------------------------------------------------------------------

void __fastcall TForm1::BTAddAuthorClick(TObject *Sender){
  Edit1->Text.Length();                                          //Обработка данных с поля Edit1, переобразование в ТЕХТ
  AnsiString file = "DataBase.txt";                              //Откртие файла "DataBase.txt"
  AnsiString temp = Edit1->Text;                                 //Занесение данных с с поля Edit1 во веменную переменную temp
  TStringList *List = new TStringList;                           //объявляем объект

        if (FileExists(file)){                                   //Проверка файла
                List->LoadFromFile(file);                        //Запись во временную переменную данных с файла "DataBase.txt"
                List->Add(temp);                                 //Запись данных с Edit1 (С поля для ввода) в временную переменную temp
                List->SaveToFile(file);                          //Сохранение в конец файла новых данных
        }

  delete List;                                                   //удаление/освобождение памяти

//Очиска поля ввода и экрана, вывод на экран!
  Edit1->Clear();
  Memo1->Clear();
  String File = "DataBase.txt";
  Memo1->Lines->LoadFromFile(File);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BTdelauthorClick(TObject *Sender){
//удаление по полному вводу строки или все похожие компоненты!!!
  TStringList *words0 = new TStringList;                         //объявляем объект words0
  TStringList *words1 = new TStringList;                         //объявляем объект words1

  words0->LoadFromFile("DataBase.txt");                          //Занесение данных с файла "DataBase.txt"
//Проверка введенных данных в поле для ввода Edit1 и сравнивание с сушествующим
  for(int i = 0; i < words0->Count; i++){
        if(words0->Strings[i].Pos(Edit1->Text)) continue;
        words1->Add(words0->Strings[i]);
  }
  words1->SaveToFile("DataBase.txt");                            //Сохранение в файл исходных данных с удаленной строкой

  delete words0;
  delete words1;
//Очиска поля ввода и экрана, вывод на экран!
        Edit1->Clear();
        Memo1->Clear();
        String File = "DataBase.txt";
        Memo1->Lines->LoadFromFile(File);
}
//----------------------------------------------------------------------------

void __fastcall TForm1::BTsortAuthorClick(TObject *Sender){
  auto_ptr<TStringList> L (new TStringList);                     //объявляем объект
  L->LoadFromFile("DataBase.txt");                               //загружаем файл
  int n = L->Count;                                              //количество строк

  int i,j;
  struct Library *lib,temp;                                      //Обяления структуры
  FILE *library1 = fopen("DataBase.txt","r");                    //Открытие файла для чтения

        lib = (struct Library*)malloc(n*sizeof(struct Library)); //выделяет память
//Ввод данных с файла "DataBase.txt" и запись в структуру
        for(i=0;i<n;i++){
                fscanf(library1,"%s",&(lib+i)->name);
                fscanf(library1,"%s",&(lib+i)->book);
                fscanf(library1,"%d",&(lib+i)->year);
        } fclose(library1);                                      //закрытие файла

  FILE *library = fopen("DBbuff.txt","w");                       //открытие файла для записи
//Вывод данных в файла "DBbuff.txt"
        for(i=0;i<n;i++){
                for(j=0;j<n;j++)
                        if(strcmp((lib+i)->name,lib[j].name)<0){
                                temp=lib[i];
                                lib[i]=lib[j];
                                lib[j]=temp;
                }
        }
  for (i=0;i<n;i++){
        fprintf(library,"%s %s %d\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
  }fclose(library);                                              //закрытие файла
  free(lib);                                                     //освобождение памяти
//Очиска поля ввода и экрана, вывод на экран!
        Edit1->Clear();
        Memo1->Clear();
        String File = "DBbuff.txt";
        Memo1->Lines->LoadFromFile(File);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BTsortBookClick(TObject *Sender){
  auto_ptr<TStringList> L (new TStringList);                     //объявляем объект
  L->LoadFromFile("DataBase.txt");                               //загружаем файл
  int n = L->Count;                                              //количество строк

  int i,j;
  struct Library *lib,temp;                                      //Обяления структуры
  FILE *library1 = fopen("DataBase.txt","r");                    //Открытие файла для чтения

        lib = (struct Library*)malloc(n*sizeof(struct Library)); //выделяет память
//Ввод данных с файла "DataBase.txt" и запись в структуру
        for(i=0;i<n;i++){
                fscanf(library1,"%s",&(lib+i)->name);
                fscanf(library1,"%s",&(lib+i)->book);
                fscanf(library1,"%d",&(lib+i)->year);
        } fclose(library1);                                      //закрытие файла

  FILE *library = fopen("DBbuff.txt","w");                       //открытие файла для записи
//Вывод данных в файла "DBbuff.txt"
        for(i=0;i<n;i++){
                for(j=0;j<n;j++)
                        if(strcmp((lib+i)->book,lib[j].book)<0){
                                temp=lib[i];
                                lib[i]=lib[j];
                                lib[j]=temp;
                }
        }
  for (i=0;i<n;i++){
        fprintf(library,"%s %s %d\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
  }fclose(library);                                              //закрытие файла
  free(lib);                                                     //освобождение памяти
//Очиска поля ввода и экрана, вывод на экран!
        Edit1->Clear();
        Memo1->Clear();
        String File = "DBbuff.txt";
        Memo1->Lines->LoadFromFile(File);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BTsortYearClick(TObject *Sender){
  auto_ptr<TStringList> L (new TStringList);                     //объявляем объект
  L->LoadFromFile("DataBase.txt");                               //загружаем файл
  int n = L->Count;                                              //количество строк

  int i,j;
  struct Library *lib,temp;                                      //Обяления структуры
  FILE *library1 = fopen("DataBase.txt","r");                    //Открытие файла для чтения

        lib = (struct Library*)malloc(n*sizeof(struct Library)); //выделяет память
//Ввод данных с файла "DataBase.txt" и запись в структуру
        for(i=0;i<n;i++){
                fscanf(library1,"%s",&(lib+i)->name);
                fscanf(library1,"%s",&(lib+i)->book);
                fscanf(library1,"%d",&(lib+i)->year);
        } fclose(library1);                                      //закрытие файла

  FILE *library = fopen("DBbuff.txt","w");                       //открытие файла для записи
//Вывод данных в файла "DBbuff.txt"
        for (i=0; i<n-1;i++)
    		for (j=i+1;j<n;j++)
                        if((lib+i)->year>lib[j].year){
                                temp=lib[i];
                                lib[i]=lib[j];
                                lib[j]=temp;
                        }
  for (i=0;i<n;i++){
        fprintf(library,"%s %s %d\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
  }fclose(library);                                              //закрытие файла
  free(lib);                                                     //освобождение памяти
//Очиска поля ввода и экрана, вывод на экран!
        Edit1->Clear();
        Memo1->Clear();
        String File = "DBbuff.txt";
        Memo1->Lines->LoadFromFile(File);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::BTFindAuthorClick(TObject *Sender){
  auto_ptr<TStringList> L (new TStringList);                     //объявляем объект
  L->LoadFromFile("DataBase.txt");                               //загружаем файл
  int n = L->Count;                                              //количество строк

  int i,j;
  struct Library *lib,temp;                                      //Обяления структуры
  FILE *library1 = fopen("DataBase.txt","r");                    //Открытие файла для чтения

        lib = (struct Library*)malloc(n*sizeof(struct Library)); //выделяет память
//Ввод данных с файла "DataBase.txt" и запись в структуру
        for(i=0;i<n;i++){
                fscanf(library1,"%s",&(lib+i)->name);
                fscanf(library1,"%s",&(lib+i)->book);
                fscanf(library1,"%d",&(lib+i)->year);
        } fclose(library1);                                      //закрытие файла

  FILE *library = fopen("DBbuff.txt","w");                       //открытие файла для записи

  char *NameW = new char[Edit1->Text.Length()+1];                //Создание объекта
  strcpy(NameW, Edit1->Text.c_str());                            //Приесвоение объекту введенный текста
    for (i=0; i<n;i++){
        if (strcmp((lib+i)->name,NameW)==0){
                fprintf(library,"%s %s %d\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
        }
    }fclose(library);                                             //Закрытие файла
   free(lib);                                                     //освобождение памяти

//Очиска поля ввода и экрана, вывод на экран!
        Edit1->Clear();
        Memo1->Clear();
        String File = "DBbuff.txt";
        Memo1->Lines->LoadFromFile(File);
}
//--------------------------------------------------------------------------
void __fastcall TForm1::BTFindBookClick(TObject *Sender){
  auto_ptr<TStringList> L (new TStringList);                     //объявляем объект
  L->LoadFromFile("DataBase.txt");                               //загружаем файл
  int n = L->Count;                                              //количество строк

  int i,j;
  struct Library *lib,temp;                                      //Обяления структуры
  FILE *library1 = fopen("DataBase.txt","r");                    //Открытие файла для чтения

        lib = (struct Library*)malloc(n*sizeof(struct Library)); //выделяет память
//Ввод данных с файла "DataBase.txt" и запись в структуру
        for(i=0;i<n;i++){
                fscanf(library1,"%s",&(lib+i)->name);
                fscanf(library1,"%s",&(lib+i)->book);
                fscanf(library1,"%d",&(lib+i)->year);
        } fclose(library1);                                      //закрытие файла

  FILE *library = fopen("DBbuff.txt","w");                       //открытие файла для записи

  char *BookW = new char[Edit1->Text.Length()+1];                //Создание объекта
  strcpy(BookW, Edit1->Text.c_str());                            //Приесвоение объекту введенный текст
    for (i=0; i<n;i++){
        if (strcmp((lib+i)->book,BookW)==0){
                fprintf(library,"%s %s %d\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
        }
    }fclose(library);                                             //Закрытие файла
   free(lib);                                                     //освобождение памяти

//Очиска поля ввода и экрана, вывод на экран!
        Edit1->Clear();
        Memo1->Clear();
        String File = "DBbuff.txt";
        Memo1->Lines->LoadFromFile(File);
}
//---------------------------------------------------------------------------

 /*void __fastcall TForm1::BTFindYearClick(TObject *Sender){
  auto_ptr<TStringList> L (new TStringList);                     //объявляем объект
  L->LoadFromFile("DataBase.txt");                               //загружаем файл
  int n = L->Count;                                              //количество строк

  int i,j;
  struct Library *lib,temp;                                      //Обяления структуры
  FILE *library1 = fopen("DataBase.txt","r");                    //Открытие файла для чтения

        lib = (struct Library*)malloc(n*sizeof(struct Library)); //выделяет память
//Ввод данных с файла "DataBase.txt" и запись в структуру
        for(i=0;i<n;i++){
                fscanf(library1,"%s",&(lib+i)->name);
                fscanf(library1,"%s",&(lib+i)->book);
                fscanf(library1,"%d",&(lib+i)->year);
        } fclose(library1);                                      //закрытие файла

  FILE *library = fopen("DBbuff.txt","w");                       //открытие файла для записи

    /*int YearW;
    TryStrToInt(Edit1->Text, YearW);  */

  /*String *YearW = new String[Edit1->Text.Length()+1];                //Создание объекта
  strcpy(YearW, Edit1->Text.c_str());*/
  /*  for (i=0; i<n;i++){
        if (strcmp((lib+i)->year,YearW)==0){
                fprintf(library,"%s %s %d\n",(lib+i)->name,(lib+i)->book,(lib+i)->year);
        }
    }fclose(library);                                           //Закрытие файла
   free(lib);                                                     //освобождение памяти

//Очиска поля ввода и экрана, вывод на экран!
        Edit1->Clear();
        Memo1->Clear();
        String File = "DBbuff.txt";
        Memo1->Lines->LoadFromFile(File);
}    */
          /*  AnsiString file = "C:\\Users\\Иван\\Desktop\\Library menu\\1.txt";
        AnsiString temp ="|             " +  Edit1->Text + "|               " + Edit2->Text + "|               " +  Edit3->Text + "|"; // ???????????? ??????
        TStringList *list1 = new TStringList;
        list1->Add(temp); //  Edit1->Text + "|" + Edit2->Text
        if (FileExists(file) == false)
        {
            list1->SaveToFile(file);
        }
        else
        {
            TStringList *list2 = new TStringList; // 2 TStringLis
            list2->LoadFromFile(file);
            list2->Text = list2->Text + list1->Text;
            list2->SaveToFile(file);
            delete list2;
        }
        delete list1;   */

   /*bool remove_line(const char *filename, size_t index){
  vector<string> vec;
    ifstream file(filename);
    if (file.is_open())
    {
        string str;
        while (getline(file, str))
            vec.push_back(str);
        file.close();
        if (vec.size() < index)
            return false;
        vec.erase(vec.begin() + index);
        ofstream outfile(filename);
        if (outfile.is_open())
        {
            copy(vec.begin(), vec.end(),
                ostream_iterator<string>(outfile, "\n"));
            outfile.close();
            return true;
        }
        return false;
    }
    return false;
}

void __fastcall TForm1::Button4Click(TObject *Sender)
{
  cout << boolalpha << remove_line("1.txt", 2);
    return 0;
}    */


        /*TStringList *List=new TStringList;
        List->LoadFromFile("1.txt");*/

        /*for(int j = 0; j < List->Count-1; j++)
        for(int i = j; i < List->Count; i++)
        if (*((int *)List->Items[j]) > * ((int *)List->Items[i]))
        List->Exchange(j, i);
        List->SaveToFile("1.txt");  */
        

       /* String str="",buf="";
        for (int j=0;j<List->Items->Count-1;j++){
        for (int i=0;i<List->Items->Count-1;i++){
        str=List->Items->Strings[i];
        buf=List->Items->Strings[i+1];
        if (str<buf);} } delete List;
        Edit1->Clear();
        Memo1->Clear();
        String File = "1.txt";
        Memo1->Lines->LoadFromFile(File);  */


        /*TStringList *List=new TStringList;
        List->LoadFromFile("1.txt");
        StringGrid1->Enabled=true;
        KolWorker = trToInt(Edit1->Text);
        StringGrid1->RowCount=KolWorker + 1; */


        /*TStringList *lst  = new TStringList;
        TStringList *lst1 = new TStringList;

        int col_sort =0;  //номер колонки для сортиовки
 
        for(int i=1;i<StringGrid1->RowCount;++i)    //загоняем все в лист и через разделительный знак запоминаем номер строки, что бы после все передвинуть
                lst->Add(StringGrid1->Cells[col_sort][i]+"~"+IntToStr(i));
 
                lst->Sort();   //Сортируем
 
        for(int i=0;i<StringGrid1->RowCount;++i)   //Делаем дупликат таблицы,что бы по ней после пересобрать основную
                lst1->Add(StringGrid1->Rows[i]->Text);
 
        for(int i=0;i<lst->Count;++i)     //Строим отсортированую таблицу
                StringGrid1->Rows[i+1]->DelimitedText =lst1->Strings[lst->Strings[i].SubString(lst->Strings[i].Pos("~") + 1,lst->Strings[i].Length()).ToInt()]  ;
 
        delete lst,lst1;    */

          /* AnsiString file_in = "C:\\Users\\Иван\\Desktop\\Library menu\\1.txt";

   Edit1->Text.Length();
         AnsiString idelete = Edit1->Text;
  int i_number_line_now = 0;
  string line;
  string line_file_text;

 while(getline(file_in, line))
 {
   i_number_line_now++;

   if(!(i_number_line_now == idelete))
   {
       line_file_text.insert(line_file_text.size(),line);
       line_file_text.insert(line_file_text.size(),"\r\n");

   }
 }

 ofstream file_out;
 file_out.open ("C:\\Users\\Иван\\Desktop\\Library menu\\1.txt",ios::trunc | ios::binary);
 file_out.write(line_file_text.c_str(), line_file_text.size());
 file_out.clear();  */

//---------------------------------------------------------------------------
//удаление по номеру
/*  int number = 0;
  number = StrToInt(Edit1->Text);

        TStringList *List=new TStringList;
        List->LoadFromFile("C:\\Users\\Иван\\Desktop\\Library menu\\1.txt");
        List->Delete(number-1);

        List->SaveToFile("C:\\Users\\Иван\\Desktop\\Library menu\\1.txt");
        delete List;

        Edit1->Clear();
        Memo1->Clear();
        String File = "C:\\Users\\Иван\\Desktop\\Library menu\\1.txt";
        Memo1->Lines->LoadFromFile(File);     */
//--------------------------------------------------------------------------

