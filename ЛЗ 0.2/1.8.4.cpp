// ���������� ������ ������� power, ���
//    x - �����, ������� ����� �������� � �������
//    p - �������, � ������� ����� �������� x
//

int power(int x, unsigned p) {
    int answer = 1, a = x;
    for(int i=0; i<p; i++){
        answer = x;
        x = x * a;
    }
    return answer;
}
