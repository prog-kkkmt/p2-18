#include <stdio.h>

int main(void)
{
    int i,n,r,b=0;
    printf("kolichestvo:");
    scanf("%i", &n); // ���� ��������� �����
    for (i=1; i<=n; ++i){ // ����
    printf("%i=",i); // ���� ����� �����
    scanf("%i", &r);
    if (r>0) b=1; // ���� ����� ������ 0, �� ������ True
    }
    printf("%s\n",b?"True":"False");
    return 0;
}
