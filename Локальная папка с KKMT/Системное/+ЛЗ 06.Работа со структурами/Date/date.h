/* ��������� "����". ��������� �.�., 17.09.2020 */
#ifndef DATE_H
#define DATE_H

typedef struct Date{ /* ���� */
    int year; /* ��� */
    int month; /* ����� */
    int day; /* ���� */
} Date;

/* ����� ��, ��� d1 �� ������ (greater or equal), ��� d2 */
int ge(Date d1, Date d2);

/* ����� ��, ��� d1 �� ������ (less or equal), ��� d2 */
int le(Date d1, Date d2);

/* ������ �� ���� � �������� */
int between(Date d1, Date d2, Date d3);

/* �������� ��� */
Date date_diff(Date d1, Date d2);

/* �������� ���� �� 3� ����� */
Date intsToDate(int year, int month, int day);

/* �������� ���� �� ������. �������������� */
Date strToDate(const char *s);

#endif // DATE_H
