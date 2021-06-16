/* ��������� "����". ��������� �.�., 17.09.2020 */
#include <stdio.h>
#include "date.h"

int main() {
    Date d1, d2;
	scanf("%d%d%d", &d1.year, &d1.month, &d1.day);
	scanf("%d%d%d", &d2.year, &d2.month, &d2.day);

    printf("���� 1 = %d.%d.%d\n", d1.day, d1.month, d1.year);
    printf("���� 2 = %d.%d.%d\n", d2.day, d2.month, d2.year);

    Date d3 = date_diff(d1, d2);
    printf("�������� = %d.%d.%d\n", d3.day, d3.month, d3.year);

    /* �������� ���� �� 3� ����� */
    int day, month, year;
	scanf("%d%d%d", &year, &month, &day);
    Date d4 = intsToDate(year, month, day);
    printf("���� 4 = %d.%d.%d\n", d4.day, d4.month, d4.year);

    /* ������� ���� �������� */
    char *months[] =
        {"", "������","�������","�����","������","���","����","����",
        "�������","��������","�������","������","�������"};
    printf("����: %d %s %d\n", d1.day, months[d1.month], d1.year);

    return 0;
}
