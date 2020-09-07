#include <cassert>
#include <iostream>

class Fibonacci final {
 public:
  static int get(int n) {
    int a[n];
      a[0] = 0;//первые числа
      a[1] = 1;
      for(int i = 2; i < n + 1; ++i){
          a[i] = a[i-1] + a[i-2];//алгоритм без рекурсии
      }
      return a[n];
  }
};

int main(void) {
  int n;
  std::cin >> n;
  std::cout << Fibonacci::get(n) << std::endl;
  return 0;
}