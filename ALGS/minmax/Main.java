//Дано целое число N и набор из N чисел. Найти минимальный и максимальный из элементов данного набора и вывести их в указанном порядке.


public class Main {

    public static void main(String[] args) {
      int arr[] = new int[] {-5,-3, -3, -11, 1, 5, 10};// исходные данные
        int min = arr[0], max = arr[0];// даем им изначальные данные(первые в списке)
      for(int i = 0; i < arr.length; ++i){
          if(min > arr[i]){ //находим минимальное
              min = arr[i];
          }
          if(max < arr[i]){// находим максимальное
              max = arr[i];
          }
      }
      System.out.println("max = " + max +" min = " + min); // вывод
    }
}
