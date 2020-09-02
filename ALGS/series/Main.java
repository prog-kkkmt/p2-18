//Даны десять вещественных чисел. Найти их сумму.



public class Main {

    public static void main(String[] args) {
       float a[] = new float[] {1.1f, 1.2f, 1.3f, 1.4f, 1.5f, 1.6f, 1.7f, 1.8f, 1.9f, 2,0f}; // исходные данные
       float answer = 0.0f; // ответ
       for(int i = 0; i < a.length; ++i){
           answer+= a[i];//сложение и присвоениие ответа
       }
       System.out.println("answer = " + answer);// вывод
    }
}
