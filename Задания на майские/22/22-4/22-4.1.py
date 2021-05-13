# Выполнил Кузнецов М. С. П2-18.

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form, Window = uic.loadUiType("tracker.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


def on_click():
    print(form.plainTextEdit.toPlainText())
    print(form.dateEdit.dateTime().toString('dd-MM-yyyy'))
    print("Clicked!!!")

def on_click_calendar():
    global start_date, calc_date
    form.dateEdit.setDate(form.calendarWidget.selectedDate())
    calc_date = form.calendarWidget.selectedDate()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    form.label_3.setText("До наступления события осталось: %s дней )))" % delta_days)

def on_dateedit_change():
    global start_date, calc_date
    form.calendarWidget.setSelectedDate(form.dateEdit.date())
    calc_date = form.dateEdit.date()
    delta_days = start_date.daysTo(calc_date)
    print(delta_days)
    form.label_3.setText("До наступления события осталось: %s дней )))" % delta_days)

form.pushButton.clicked.connect(on_click)
form.calendarWidget.clicked.connect(on_click_calendar)
form.dateEdit.dateChanged.connect(on_dateedit_change)

start_date = form.calendarWidget.selectedDate()
calc_date = form.calendarWidget.selectedDate()
form.label.setText("Трекер события от %s" % start_date.toString('dd-MM-yyyy'))
on_click_calendar()

app.exec_()
