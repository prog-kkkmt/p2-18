//Дан символ C. Вывести его код (т. е. номер в кодовой таблице).


public class Main {

    public static void main(String[] args) {
      char c = 'C';//исходные данные
      int answer = (int) c;// парсируем char в int  получаем код символа
      System.out.println(answer);//выводим ответ
    }
}
