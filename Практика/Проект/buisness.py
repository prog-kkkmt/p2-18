from Cashier import Deal, Report
from datetime import datetime
from sqlighter import SQLigter

class Program:

    def menu(self):
        print("==={ Меню }===")
        print("0. Выход")
        print("1. Принять документ и деньги")
        print("2. Получить отчет кассира")

    def inputData(self, deal):
        print("Введите имя документа: ", end='')
        doc = input()
        print("Оплата клиента: ", end='')
        money = float(input())
        print("нал/безнал: ", end='')
        payment = input()
        if (payment == '1') or (payment.lower()[0] == 'н'):
            payment = 'нал'
        else:
            payment = 'безнал'
        return {
            "doc": doc,
            "money": money,
            "payment": payment
        }

    def menuPaymentDoc(self):
        print("==={ Меню для работы с квитанцией }===")
        print("0. Завершить работу с заказом")
        print("1. Создать квитанцию об оплате")
        print("2. Вывести на экран квитанцию об оплате")
        print("3. Вернуть квитанцию об оплате")
        print("4. Получить отчет кассира")

    def workWithDocuments(self, deal, cashier):
        answer = -1
        while (answer):
            self.menuPaymentDoc()
            print('>> ', end='')
            answer = int(input())
            print()
                
            # 1. Создать квитанцию об оплате
            if answer == 1:
                deal.setPaymentDoc()
                print("Квитанция создана")
                print()
            
            # 2. Вывести на экран квитанцию об оплате
            elif answer == 2:
                print("Квитанция об оплате:")
                deal.printPaymentDoc()
                print()
            
            # 3. Вернуть квитанцию об оплате
            elif answer == 3:
                print("Квитанция об оплате в файле: ", deal.printFilePaymentDoc())
                print()
            
            # 4. Получить отчет кассира
            elif answer == 4:
                cashier.printReport()
                print()

            # Что-то непонятное
            elif answer != 0:
                print("Такой функции не существует")
            
        print('----------------')

    def menuPrintReport(self):
        print("0. Назад")
        print("1. Записать отчет документа на экран")
        print("2. Записать отчет документа в файл")

    def workingPrintReport(self, cashier):
        answer = -1
        while (answer):
            self.menuPaymentDoc()
            print('>> ', end='')
            answer = int(input())
            print()

            # 1. Записать отчет документа на экран
            if answer == 1:
                cashier.printReport()
                answer = 0
            
            # 2. Записать отчет документа в файл
            elif answer == 2:
                print("Отчет кассира в файле:", cashier.printReport(cashier.createNameFile()) )
                answer = 0

            # Что-то не понятное
            elif answer != 0:
                print("Такой функции не существует")
            
        print('----------------')

def main():
    print(datetime.today())
    print()

    cashier = Report(0, 0)
    user = Program()
    db = SQLigter("bd")
    answer = -1

    while answer:
        user.menu()
        print(">> ", end='')
        answer = int(input())
        print()

        # 1. Принять документ и деньги
        if answer == 1:
            # data = user.inputData(deal)
            # deal = Deal(data['doc'], data['money'], data['payment'])
            doc = 'doc.txt'
            money = 6000.0
            payment_method = 'нал'
            deal = Deal(doc, money, payment_method)

            # Если не хватило денег
            if deal.enoughMoney() == False:
                print()
                print("Недостаточно")      
            # Денег хватает
            else:
                print()
                print("Докумет принят")
                cashier.add(money, payment_method) # Добавляем деньги в отчет

                d_fio = deal.getFIO()   # Получаем ФИО клиента
                # Если его нет в бд с клиентами, добавляем
                if db.clientExists(d_fio) == False:
                    db.addClient(d_fio, deal.getPhoneNumber())
                    s = ''
                    for key in d_fio:
                        s += d_fio[key] + ' '
                    print("Добавлен новый клиент: ", s)
                
                client_id = db.getIdClient(d_fio)
                db.addMoneyToTheClient(client_id, money) # Добавляем деньги в общий список покупок клиента

                # Добавляем в реестр заказов новый заказ
                d = deal.getDataProduct()
                date, time = str(datetime.today()).split()
                db.addOrderToRegister(d['product'], d['number'], d['total_price'],\
                    deal.getPaymentMethod(), client_id, date, time)
                data = [d['product'], d['number'], d['total_price'], deal.getPaymentMethod(), client_id, date, time]
                s = str(db.getLastId('registry')) + ' | '
                for x in data:
                    s += str(x) + ' | '

                print("Добавлен в реестр: ", s)
                print()
                # Работа с поступившем документом
                user.workWithDocuments(deal, cashier)            
        
        # 2. Получить отчет кассира
        elif answer == 2:
            cashier.printReport()
            
        # Что-то не понятное
        elif answer != 0:
            print("Такой функции не существует")
        
        print()
    print('----------------')
    # Отчет кассира
    cashier.printReport()
    print("Отчет кассира в файле:", cashier.printReport(cashier.createNameFile()) )
    print('----------------')
    print()
    print("Stop programm")


if __name__ == "__main__":
    main()
