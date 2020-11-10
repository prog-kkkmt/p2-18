//---------------------------------------------------------------------------

#include <vcl.h>
#pragma hdrstop

#include "Unit1.h"
//---------------------------------------------------------------------------
#pragma package(smart_init)
#pragma resource "*.dfm"
TForm1 *Form1;
//---------------------------------------------------------------------------
__fastcall TForm1::TForm1(TComponent* Owner)
        : TForm(Owner)
{
}
  struct Library{
char name[30];
char book[30];
int year;
};

void __fastcall TForm1::Button1Click(TObject *Sender){
        Edit1->Clear();
        Memo1->Clear();

        String File;
        File = "C:\\Users\\Иван\\Desktop\\Library menu\\1.txt";
        Memo1->Lines->LoadFromFile(File);
}
//---------------------------------------------------------------------------
void __fastcall TForm1::Button2Click(TObject *Sender){
        exit(1);
}
//---------------------------------------------------------------------------

void __fastcall TForm1::Button3Click(TObject *Sender){
        Edit1->Text.Length();
                AnsiString file = "C:\\Users\\Иван\\Desktop\\Library menu\\1.txt";
                AnsiString temp = Edit1->Text;
                TStringList *list1 = new TStringList;

        if (FileExists(file))
                list1->LoadFromFile(file);
                list1->Add(temp);
                list1->SaveToFile(file);

        delete list1;

        Edit1->Clear();
        Memo1->Clear();
        
        String File = "C:\\Users\\Иван\\Desktop\\Library menu\\1.txt";
        Memo1->Lines->LoadFromFile(File);

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
}
//---------------------------------------------------------------------------
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
void __fastcall TForm1::Button4Click(TObject *Sender){

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

                //удаление по полному вводу строки или все похожие компоненты!!!
         TStringList *s0 = new TStringList;
  TStringList *s1 = new TStringList;
  s0->LoadFromFile("C:\\Users\\Иван\\Desktop\\Library menu\\1.txt");
  for(int i = 0; i < s0->Count; i++)
   {
     if(s0->Strings[i].Pos(Edit1->Text)) continue;
     s1->Add(s0->Strings[i]);
   }
  s1->SaveToFile("C:\\Users\\Иван\\Desktop\\Library menu\\1.txt");
  delete s0;
  delete s1;
  Edit1->Clear();
        Memo1->Clear();
        String File = "C:\\Users\\Иван\\Desktop\\Library menu\\1.txt";
        Memo1->Lines->LoadFromFile(File); 
}
//---------------------------------------------------------------------------



