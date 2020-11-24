/* Структура "дата". Гусятинер Л.Б., 17.09.2020 */
#ifndef DATE_H
#define DATE_H

typedef struct Date{ /* дата */
    int year; /* год */
    int month; /* месяц */
    int day; /* день */
} Date;

/* Верно ли, что d1 не меньше (greater or equal), чем d2 */
int ge(Date d1, Date d2);

/* Верно ли, что d1 не больше (less or equal), чем d2 */
int le(Date d1, Date d2);

/* Входит ли дата в интервал */
int between(Date d1, Date d2, Date d3);

/* Разность дат */
Date date_diff(Date d1, Date d2);

/* Получить дату из 3х чисел */
Date intsToDate(int year, int month, int day);

/* Получить дату из строки. Самостоятельно */
Date strToDate(const char *s);

#endif // DATE_H
