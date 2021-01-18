// определите только функцию power, где
//    x - число, которое нужно возвести в степень
//    p - степень, в которую нужно возвести x
//

int power(int x, unsigned p) {
    int answer = 1, a = x;
    for(int i=0; i<p; i++){
        answer = x;
        x = x * a;
    }
    return answer;
}
