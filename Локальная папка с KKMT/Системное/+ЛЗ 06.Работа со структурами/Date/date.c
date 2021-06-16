/* ��������� "����". ���� ����. ��������� �.�., 05.05.2020 */
#include <stdio.h>
#include <stdlib.h>
#include "date.h"

int ge(Date d1, Date d2)  {
    /* ����� ��, ��� this �� ������ (greater or equal), ��� other */
    return
        d1.year > d2.year ||
        (d1.year == d2.year && (d1.month > d2.month || (d1.month == d2.month && d1.day >= d2.day)));
}

int le(Date d1, Date d2) {
    /* ����� ��, ��� d1 �� ������ (less or equal), ��� d2 */
    return ge(d2, d1);
}

int between(Date d1, Date d2, Date d3) {
    /* ������ �� ���� � �������� */
    return ge(d3, d1) && le(d3, d2);
}

Date date_diff(Date d1, Date d2) {
    /* �������� ��� */
    Date diff;
    diff.day = d1.day - d2.day;
    diff.month = d1.month - d2.month;
    if (diff.day < 0) {
        diff.day += 30;
        diff.month--;
    }
    diff.year = d1.year - d2.year;
    if (diff.month < 0) {
        diff.month += 12;
        diff.year--;
    }

    return diff;
};


Date intsToDate(int year, int month, int day) {
    /* �������� ���� �� 3� ����� */
    Date date = {year, month, day};
    return date;
};

Date strToDate(const char *s) {
    /* �������� ���� �� ������. �������������� */
    /* */
    Date date = {0, 0, 0};
    return date;
};
