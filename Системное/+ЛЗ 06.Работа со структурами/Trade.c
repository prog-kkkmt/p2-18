// Гусятинер Л.Б., МГОТУ ККМТ, 17.09.2020
// Пример использования композиции. Структура содержит
// в качестве одного (или нескольких полей) экземпляры другой
// структуры

#include <stdio.h>
#include <stdlib.h>

typedef struct Date { // дата
    // по умолчанию все поля структуры - public
    int year; // год
    int month; // месяц
    int day; // день
} Date;

typedef struct Saler { // Продавец
    int salerId; // Уникальное число, идентификатор (ИД) продавца
    char name[30]; // ФИО
    char city[20]; // Город
    double comm; // Комиссионные от 0 до 1

} Saler;

typedef struct Customer { // Заказчик
    // по умолчанию все поля класса private,
    // то есть вне кода класса не видны
    int customerId; // ИД заказчика
    char name[30]; // ФИО
    char city[20]; // Город
    int rating; // Рейтинг (некторое число от 0 до 200)
    int salerId; // ИД обслуживающего продавца
} Customer;

typedef struct Order { // Заказ
    int orderId; // ИД заказа
    int salerId; // ИД продавца
    int customerId; // ИД заказчика
    Date date; // Дата заказа
    double cost; // Сумма заказа
} Order;

int main() {
    Order order;
    // создали экземпляр структуры
    //
    order.orderId = 1;
    order.salerId = 1;
    order.customerId = 1;
    order.date.year = 2019;
    order.date.month = 12;
    order.date.day = 31;
    order.cost = 125.78;

    // Отпечатаем значения
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
