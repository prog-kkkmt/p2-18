// ��������� �.�., ����� ����, 17.09.2020
// ������ ������������� ����������. ��������� ��������
// � �������� ������ (��� ���������� �����) ���������� ������
// ���������

#include <stdio.h>
#include <stdlib.h>

typedef struct Date { // ����
    // �� ��������� ��� ���� ��������� - public
    int year; // ���
    int month; // �����
    int day; // ����
} Date;

typedef struct Saler { // ��������
    int salerId; // ���������� �����, ������������� (��) ��������
    char name[30]; // ���
    char city[20]; // �����
    double comm; // ������������ �� 0 �� 1

} Saler;

typedef struct Customer { // ��������
    // �� ��������� ��� ���� ������ private,
    // �� ���� ��� ���� ������ �� �����
    int customerId; // �� ���������
    char name[30]; // ���
    char city[20]; // �����
    int rating; // ������� (�������� ����� �� 0 �� 200)
    int salerId; // �� �������������� ��������
} Customer;

typedef struct Order { // �����
    int orderId; // �� ������
    int salerId; // �� ��������
    int customerId; // �� ���������
    Date date; // ���� ������
    double cost; // ����� ������
} Order;

int main() {
    Order order;
    // ������� ��������� ���������
    //
    order.orderId = 1;
    order.salerId = 1;
    order.customerId = 1;
    order.date.year = 2019;
    order.date.month = 12;
    order.date.day = 31;
    order.cost = 125.78;

    // ���������� ��������
    printf("%d %d %d %d.%d.%d %f\n",
           order.orderId,
           order.salerId,
           order.customerId,
           order.date.year,
           order.date.month,
           order.date.day,
           order.cost);
    return 0;
}
