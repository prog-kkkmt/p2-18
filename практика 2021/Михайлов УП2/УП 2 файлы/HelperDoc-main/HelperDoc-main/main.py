import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox
from docxtpl import DocxTemplate
# import subprocess

from design import Ui_HelperDoc
from excel import Excel
from helper import Helper


class HelperDoc(QtWidgets.QMainWindow):

    def __init__(self):
        """
        Главный класс. Объединяет GUI и функциональную часть
        """
        super().__init__()

        self.excel = Excel("KKMT2020.xlsx")
        self.helper = Helper('db.db')
        self.word = DocxTemplate("template.docx")
        self.excel.max_col = 28
        self.excel.max_row = 11

        self.ui = Ui_HelperDoc()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        """
        Добавляет функционал всем кнопкам
        :return:
        """
        self.setWindowTitle('HelperDoc')
        self.setWindowIcon(QIcon('favicon.ico'))

        self.ui.suggest_input.setPlaceholderText('Поиск...')
        self.load_data()
        self.ui.clear.clicked.connect(lambda: self.clear_data())
        self.ui.add_row.clicked.connect(lambda: self.add_row())
        self.ui.suggest_input_button.clicked.connect(lambda: self.find_rows())
        self.ui.table.setEditTriggers(QtWidgets.QTableWidget.EditTrigger.NoEditTriggers)
        self.ui.remove_row.clicked.connect(lambda: self.remove_row())
        self.ui.create_doc.clicked.connect(lambda: self.create_doc())

    def get_all_id(self):
        """
        :return: список всех id из таблицы 'table_document'
        """
        # [(1,), (2,), (3,)]
        all_id = self.helper.bd.select(self.helper.table_document, 'id', {})
        # [1, 2, 3]
        return [pk[0] for pk in all_id]

    def load_data(self):
        """
        Загружает все данные из бд в GUI
        """
        all_id = self.get_all_id()
        table_row = 0
        self.ui.table.setRowCount(len(all_id))
        for pk in all_id:
            data = self.helper.create_row(pk)
            for i in range(self.ui.table.columnCount()):
                self.ui.table.setItem(table_row, i, QtWidgets.QTableWidgetItem(str(data[i])))
            table_row += 1

    def get_row_by_position(self, position, type_dict=False):
        """
        :param position: позиция нужной строки в бд
        :param type_dict: тип возвращаемых данных (true - dict; false - list)
        :return: Строка типа dict или list
        """
        if not type_dict:
            row = list()
            for col in range(self.ui.table.columnCount()):
                row.append(self.ui.table.item(position, col).text())
        else:
            row = {
                'title_doc': self.ui.table.item(position, 0).text(),
                'type_doc': self.ui.table.item(position, 1).text(),
                'status_doc': self.ui.table.item(position, 2).text(),
                'loss_confirmation': self.ui.table.item(position, 3).text(),
                'confirmation_exchange': self.ui.table.item(position, 4).text(),
                'destruction_confirmation': self.ui.table.item(position, 5).text(),
                'education_level': self.ui.table.item(position, 6).text(),
                'series_doc': self.ui.table.item(position, 7).text(),
                'number_doc': self.ui.table.item(position, 8).text(),
                'issue_date': self.ui.table.item(position, 9).text(),
                'registration_number': self.ui.table.item(position, 10).text(),
                'code_profession': self.ui.table.item(position, 11).text(),
                'title_profession': self.ui.table.item(position, 12).text(),
                'title_qualification': self.ui.table.item(position, 13).text(),
                'education_program': self.ui.table.item(position, 14).text(),
                'admission_year': self.ui.table.item(position, 15).text(),
                'graduation_year': self.ui.table.item(position, 16).text(),
                'study_period': self.ui.table.item(position, 17).text(),
                'last_name': self.ui.table.item(position, 18).text(),
                'name': self.ui.table.item(position, 19).text(),
                'middle_name': self.ui.table.item(position, 20).text(),
                'birth_date': self.ui.table.item(position, 21).text(),
                'gender': self.ui.table.item(position, 22).text(),
                'snills': self.ui.table.item(position, 23).text(),
                'country_code': self.ui.table.item(position, 24).text(),
                'education_form': self.ui.table.item(position, 25).text(),
                'education_receipt_form': self.ui.table.item(position, 26).text(),
                'financing_source': self.ui.table.item(position, 27).text(),
            }
        return row

    def add_row_excel(self):
        """
        Запись строки из excel в бд и на экран
        :return:
        """
        current_row_position = self.ui.table.currentRow()
        # current_row_position = 0
        # # row = self.get_row_by_position(current_row_position)
        # row = self.excel.get_row(20)
        # result = list()
        # result.append(self.helper.add_all_bd(row))
        # print(result)
        self.ui.table.insertRow(current_row_position + 1)
        # self.mbox("Пам парам")
        # self.helper.create_row(1)

    def clear_data(self):
        """
        Очистка боковой панели от введенных данных
        """
        self.ui.title_doc_line.clear()
        self.ui.type_doc_line.clear()
        self.ui.status_doc_line.clear()
        self.ui.loss_confirmation_line.clear()
        self.ui.confirmation_exchange_line.clear()
        self.ui.destruction_confirmation_line.clear()
        self.ui.education_level_line.clear()
        self.ui.series_doc_line.clear()
        self.ui.number_doc_line.clear()
        self.ui.issue_date_line.clear()
        self.ui.registration_number_line.clear()
        self.ui.code_profession_line.clear()
        self.ui.title_profession_line.clear()
        self.ui.title_qualification_line.clear()
        self.ui.education_program_line.clear()
        self.ui.admission_year_line.clear()
        self.ui.graduation_year_line.clear()
        self.ui.study_period_line.clear()
        self.ui.last_name_line.clear()
        self.ui.name_line.clear()
        self.ui.middle_name_line.clear()
        self.ui.birth_date_line.clear()
        self.ui.gender_line.clear()
        self.ui.snills_line.clear()
        self.ui.country_code_line.clear()
        self.ui.education_form_line.clear()
        self.ui.education_receipt_form_line.clear()
        self.ui.financing_source_line.clear()

    def get_inputted_data(self):
        """
        Вернет полученные данные из боковой панели
        """
        data = list()
        data.append(self.ui.title_doc_line.text())
        data.append(self.ui.type_doc_line.text())
        data.append(self.ui.status_doc_line.text())
        data.append(self.ui.loss_confirmation_line.text())
        data.append(self.ui.confirmation_exchange_line.text())
        data.append(self.ui.destruction_confirmation_line.text())
        data.append(self.ui.education_level_line.text())
        data.append(self.ui.series_doc_line.text())
        data.append(self.ui.number_doc_line.text())
        data.append(self.ui.issue_date_line.text())
        data.append(self.ui.registration_number_line.text())
        data.append(self.ui.code_profession_line.text())
        data.append(self.ui.title_profession_line.text())
        data.append(self.ui.title_qualification_line.text())
        data.append(self.ui.education_program_line.text())
        data.append(self.ui.admission_year_line.text())
        data.append(self.ui.graduation_year_line.text())
        data.append(self.ui.study_period_line.text())
        data.append(self.ui.last_name_line.text())
        data.append(self.ui.name_line.text())
        data.append(self.ui.middle_name_line.text())
        data.append(self.ui.birth_date_line.text())
        data.append(self.ui.gender_line.text())
        data.append(self.ui.snills_line.text())
        data.append(self.ui.country_code_line.text())
        data.append(self.ui.education_form_line.text())
        data.append(self.ui.education_receipt_form_line.text())
        data.append(self.ui.financing_source_line.text())

        # data = [
        #     'Диплом', 'Диплом о среднем профессиональном образовании', 'Оригинал',
        #     'Нет', 'Нет', 'Нет', 'Среднее профессиональное образование', '115033', '0101709',
        #     '02.07.2020', '298', '10.02.01', 'Организация и технология защиты информации',
        #     'техник по защите информации', 'техник по защите информации', '2016', '2020', '4',
        #     'Азаров', 'Тимофей', 'Максимович', '30.05.2000', 'Муж', '192-465-544', '95', '643',
        #     'Очная	в образовательной организации', 'Региональный бюджет'
        # ]
        return data

    def add_row(self):
        """
        Добавление строки в бд. Ввод организуется из боковой панели
        """
        if self.mbox_execute("Вы уверены, что хотите добавить данные?"):
            # new_row_position = self.ui.table.currentRow() + 1
            new_row_position = self.ui.table.rowCount()
            inputted_data = self.get_inputted_data()
            for i in range(len(inputted_data)):
                self.ui.table.setItem(new_row_position, i, QtWidgets.QTableWidgetItem(inputted_data[i].strip()))
            try:
                result = self.helper.add_all_bd(inputted_data)
                if result:
                    self.ui.table.insertRow(new_row_position)
                    for i in range(len(inputted_data)):
                        self.ui.table.setItem(new_row_position, i, QtWidgets.QTableWidgetItem(inputted_data[i].strip()))
            except Exception:
                self.mbox("Некоректный ввод данных")

    def includes_row(self, row, wanted):
        """
        Есть ли в списке row строка wanted.
        param row: список
        param wanted: строка которая ищется в списке row
        return: True, если wanted есть в row. False, если нет
        """
        for col in row:
            if wanted in str(col):
                return True
        return False

    def find_rows(self):
        """
        Загружает все подходящие строки
        """
        text = self.ui.suggest_input.text().strip()
        if text == '':
            self.load_data()
        else:
            need_rows = list()
            for pk in self.get_all_id():
                row = self.helper.create_row(pk)
                if self.includes_row(row, text):
                    need_rows.append(row)
            len_need_rows = len(need_rows)
            self.ui.table.setRowCount(len_need_rows)
            for i in range(len_need_rows):
                for j in range(self.ui.table.columnCount()):
                    self.ui.table.setItem(i, j, QtWidgets.QTableWidgetItem(need_rows[i][j]))

    def remove_row(self):
        """
        Удаление строки из бд и из GUI
        """
        if self.mbox_execute("Вы уверены, что хотите удалить данные?"):
            if self.ui.table.rowCount() > 0:
                current_row_position = self.ui.table.currentRow()
                print(current_row_position)
                row = self.get_row_by_position(current_row_position)

                result = list()
                result.append(self.helper.del_all_bd(row))
                print(result)
                self.ui.table.removeRow(current_row_position)
            else:
                self.mbox("Невозможно удалить, так как таблица пуста")

    def create_doc(self):
        """
        Создание документа по шаблону
        """
        current_row_position = self.ui.table.currentRow()
        if current_row_position != -1:
            row = self.get_row_by_position(current_row_position, True)
            context = {
                'last_name': row['last_name'],
                'name': row['name'],
                'middle_name': row['middle_name'],
                'birth_date': row['birth_date'],
                'admission_year': row['admission_year'],
                'graduation_year': row['graduation_year'],
                'education_form': row['education_form'].lower()[:-2] + "ое",
                'title_doc': row['title_doc'].lower(),
                'registration_number': row['registration_number'],
                'title_profession': row['title_profession'].lower(),
                'title_qualification': row['title_qualification'].lower(),
            }
            print(context)
            self.word.render(context)
            name_f = context['last_name'] + '_' + context['name'] + '_' + context['middle_name'] + ".docx"
            try:
                self.word.save(f"./Документы/{name_f}")
                # print(subprocess.Popen(r'explorer /select,"./Документы"'))
                # self.mbox(f"Файл \"{name_f}\" успешно создан!", "Успех")
            except Exception:
                self.mbox(f"Файл с именем \"{name_f}\" открыт. Закройте его и перевыполните действие")

    def mbox_execute(self, body, title='Предупреждение'):
        """
        Диалоговое окно с выбором действия [Yes / No]
        param body: Главный текст для сообщения
        param title: Оглавление диалогового окна
        return: True, если выбран 'Yes'. False, если 'No'
        """
        dialog = QMessageBox()
        dialog.setText(body)
        dialog.setWindowTitle(title)
        dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        result = dialog.exec()
        if result == QMessageBox.StandardButton.Yes:
            return True
        elif result == QMessageBox.StandardButton.No:
            return False

    def mbox(self, body, title='Ошибка'):
        """
        Диалоговое окно
        param body: Главный текст для сообщения
        param title: Оглавление диалогового окна
        """
        dialog = QMessageBox()
        dialog.setText(body)
        dialog.setWindowTitle(title)
        dialog.exec()


app = QtWidgets.QApplication([])
application = HelperDoc()
application.show()

sys.exit(app.exec())
