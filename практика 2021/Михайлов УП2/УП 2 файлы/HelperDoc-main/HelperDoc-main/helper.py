from excel import Excel
from sqlite import Sqliter


class Helper:

    def __init__(self, bd):
        self.bd = Sqliter(bd)
        self.table_profession = "profession"
        self.table_qualification = "qualification"
        self.table_education_program = "education_program"
        self.table_student = "student"
        self.table_document = "document"

    @staticmethod
    def get_profession(row, is_form_list=False):
        """
        return: Вернет список или словарь с необходимыми данными
        """
        if is_form_list:
            return [row[11], row[12]]

        return {
            'code': row[11],
            'title': row[12]
        }

    def add_profession_bd(self, row):
        """
        Добавление данных в бд
        """
        if row == -1:
            return False

        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_profession(row)
        if type(row) is dict:
            data = row

        is_added = False
        # pk = self.bd.get_profession_id(data['title'])
        pk = self.bd.get_id(self.table_profession, 'code', {'title': data['title']})
        if pk == -1:
            is_added = True
            self.bd.add_profession(data['code'], data['title'])
        return is_added

    def del_profession_bd(self, row):
        """
        Удаление данных из бд
        """
        is_del_success = False

        data = self.get_profession(row)
        if data == -1:
            return is_del_success
        # pk = self.bd.get_profession_id(data['title'])
        pk = self.bd.get_id(self.table_profession, 'code', {'title': data['title']})
        num_id = len(self.bd.select(self.table_student, '`id`', {'profession_code': pk}))
        if num_id == 0:
            self.bd.del_profession(pk)
            is_del_success = True
        return is_del_success

    @staticmethod
    def get_qualification(row, is_form_list=False):
        """
        return: Вернет список или словарь с необходимыми данными
        """
        if is_form_list:
            return [row[13]]
        return {
            'title': row[13]
        }

    def add_qualification_bd(self, row):
        """
        Добавление данных в бд
        """
        if row == -1:
            return False

        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_qualification(row)
        if type(row) is dict:
            data = row

        is_added = False
        # data_id = self.bd.get_qualification_id(data['title'])
        pk = self.bd.get_id(self.table_qualification, 'id', data)
        if pk == -1:
            is_added = True
            self.bd.add_qualification(data['title'])
        return is_added

    def del_qualification_bd(self, row):
        """
        Удаление данных из бд
        """
        is_del_success = False

        data = self.get_qualification(row)
        if data == -1:
            return is_del_success
        # pk = self.bd.get_qualification_id(*data)
        pk = self.bd.get_id(self.table_qualification, 'id', data)
        # кол-во используемых id
        num_id = len(self.bd.select(self.table_student, '`id`', {'qualification_id': pk}))
        if num_id == 0:
            self.bd.del_qualification(pk)
            is_del_success = True
        return is_del_success

    @staticmethod
    def get_education_program(row, is_form_list=False):
        """
        return: Вернет список или словарь с необходимыми данными
        """

        if is_form_list:
            return [row[14]]

        return {
            'title': row[14]
        }

    def add_education_program_bd(self, row):
        """
        Добавление данных в бд
        """
        if row == -1:
            return False

        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_education_program(row)
        if type(row) is dict:
            data = row

        is_added = False
        # data_id = self.bd.get_education_program_id(data['title'])
        pk = self.bd.get_id(self.table_education_program, 'id', data)
        if pk == -1:
            is_added = True
            self.bd.add_education_program(data['title'])
        return is_added

    def del_education_program_bd(self, row):
        """
        Удаление данных из бд
        """
        is_del_success = False

        data = self.get_education_program(row)
        if data == -1:
            return is_del_success

        # pk = self.bd.get_education_program_id(*data)
        pk = self.bd.get_id(self.table_education_program, 'id', data)
        # кол-во используемых id
        num_id = len(self.bd.select(self.table_student, '`id`', {'education_program_id': pk}))
        if num_id == 0:
            self.bd.del_education_program(pk)
            is_del_success = True
        return is_del_success

    def get_student(self, row, is_form_list=False):
        """
        return: Вернет список или словарь с необходимыми данными
        """
        # qualification_id = self.bd.get_qualification_id(row[13])
        qualification_id = self.bd.get_id(self.table_qualification, 'id', {'title': row[13]})
        # education_program_id = self.bd.get_education_program_id(row[14])
        education_program_id = self.bd.get_id(self.table_education_program, 'id', {'title': row[14]})
        if (qualification_id == -1) or (education_program_id == -1):
            return -1

        try:
            birth_date = row[21].strftime("%d.%m.%Y")
        except Exception:
            birth_date = row[21]
        if is_form_list:
            return [
                row[19], row[18], row[20], birth_date,
                row[22], row[23], row[24], row[25], row[26], row[27], row[15],
                row[16], row[17], row[11], qualification_id, education_program_id,
            ]

        return {
            'name': row[19],
            'last_name': row[18],
            'middle_name': row[20],
            'birth_date': birth_date,
            'gender': row[22],
            'snills': row[23],
            'country_code': row[24],
            'education_form': row[25],
            'education_receipt_form': row[26],
            'financing_source': row[27],
            'admission_year': row[15],
            'graduation_year': row[16],
            'study_period': row[17],
            'profession_code': row[11],
            'qualification_id': qualification_id,
            'education_program_id': education_program_id,
        }

    def add_student_bd(self, row):
        """
        Добавление данных в бд
        """
        if row == -1:
            return False

        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_student(row)
        if type(row) is dict:
            data = row

        is_added = False

        data_of_list = [
            data['name'],
            data['last_name'],
            data['middle_name'],
            data['birth_date'],
            data['gender'],
            data['snills'],
            data['country_code'],
            data['education_form'],
            data['education_receipt_form'],
            data['financing_source'],
            data['admission_year'],
            data['graduation_year'],
            data['study_period'],
            data['profession_code'],
            data['qualification_id'],
            data['education_program_id'],
        ]

        # data_id = self.bd.get_student_id(*data_of_list)
        pk = self.bd.get_id(self.table_student, 'id', data)
        if pk == -1:
            is_added = True
            self.bd.add_student(*data_of_list)
        return is_added

    def del_student_bd(self, row):
        """
        Удаление данных из бд
        """
        data = self.get_student(row)
        if data == -1:
            return False
        # pk = self.bd.get_student_id(*data)
        pk = self.bd.get_id(self.table_student, 'id', data)
        self.bd.del_student(pk)
        return True

    def get_document(self, row, is_form_list=False):
        """
        return: Вернет список или словарь с необходимыми данными
        """
        student = self.get_student(row)
        if student == -1:
            return -1
        # student_id = self.bd.get_student_id(*student)
        student_id = self.bd.get_id(self.table_student, 'id', student)
        if student_id == -1:
            return -1

        try:
            issue_date = row[9].strftime("%d.%m.%Y")
        except Exception:
            issue_date = row[9]

        if is_form_list:
            return [
                row[0], row[1], row[7], row[8], row[3],
                row[4], row[5], row[6], issue_date, row[10],
                row[2], student_id,
            ]

        return {
            'title': row[0],
            'type': row[1],
            'series': row[7],
            'number': row[8],
            'loss_confirmation': row[3],
            'exchange_confirmation': row[4],
            'destruction_confirmation': row[5],
            'education_level': row[6],
            'issue_date': issue_date,
            'registration_number': row[10],
            'status': row[2],
            'student_id': student_id,
        }

    def add_document_bd(self, row):
        """
        Добавление данных в бд
        """
        if row == -1:
            return False

        data = dict()
        if (type(row) is list) or (type(row) is tuple):
            data = self.get_document(row)
        if type(row) is dict:
            data = row

        is_added = False
        data_of_list = [
            data['title'],
            data['type'],
            data['series'],
            data['number'],
            data['loss_confirmation'],
            data['exchange_confirmation'],
            data['destruction_confirmation'],
            data['education_level'],
            data['issue_date'],
            data['registration_number'],
            data['status'],
            data['student_id']
        ]

        # data_id = self.bd.get_document_id(*data_of_list)
        pk = self.bd.get_id(self.table_document, 'id', data)
        if pk == -1:
            is_added = True
            self.bd.add_document(*data_of_list)
        return is_added

    def del_document_bd(self, row):
        """
        Удаление данных из бд
        """
        data = self.get_document(row)
        if data == -1:
            return False
        # pk = self.bd.get_document_id(*data)
        pk = self.bd.get_id(self.table_document, 'id', data)

        self.bd.del_document(pk)
        return True

    def add_all_bd(self, row):
        """
        Добавление всех данных в бд
        """
        result_add = {
            'profession': self.add_profession_bd(self.get_profession(row)),
            'qualification': self.add_qualification_bd(self.get_qualification(row)),
            'education_program': self.add_education_program_bd(self.get_education_program(row)),
            'student': self.add_student_bd(self.get_student(row)),
            'document': self.add_document_bd(self.get_document(row))
        }
        # print(result_add)
        return bool(sum(result_add.values()))

    def del_all_bd(self, row):
        """
        Удаление полной строки из бд
        """
        result_del = {
            'document': self.del_document_bd(row),
            'student': self.del_student_bd(row),
            'education_program': self.del_education_program_bd(row),
            'qualification': self.del_qualification_bd(row),
            'profession': self.del_profession_bd(row),
        }
        return result_del['document']

    def create_row(self, pk_document):
        """
        Создание строки для удобного форматирования
        """
        try:
            document = self.bd.select(self.table_document, '*', {'id': pk_document})[0]
            student = self.bd.select(self.table_student, '*', {'id': document[12]})[0]
            profession = self.bd.select(self.table_profession, '*', {'code': student[14]})[0]
            education_program = self.bd.select(self.table_education_program, '*', {'id': student[15]})[0]
            qualification = self.bd.select(self.table_qualification, '*', {'id': student[16]})[0]
            data = (
                document[1], document[2], document[11],
                document[5], document[6], document[7],
                document[8], document[3], document[4],
                document[9], document[10], profession[0], 
                profession[1], qualification[1],
                education_program[1], student[11], student[12],
                student[13], student[2], student[1],
                student[3], student[4], student[5],
                student[6], student[7], student[8],
                student[9], student[10]
            )
            # print(data)
            return data
        except Exception:
            return -1

    def close(self):
        """
        Закрытие соединения с бд
        """
        self.bd.close()


if __name__ == '__main__':
    doc = Excel("ККМТ2020 Очно.xlsx")
    doc.max_col = 28
    # doc.max_row = 11

    # rows = doc.get_rows(False)

    # first_row = rows[0]
    # title = doc.get_title_row()
    # for i in range(len(title)):
    #     print(f"{i}| {title[i]}: {first_row[i]}")
    # print(first_row)

    helper = Helper('db.db')
    # helper.create_row(1)
    # line = doc.get_row(2)
    # is_add = helper.del_all_bd(line)
    # print(is_add)
    # list_false = list()
    # for i in range(2, 362):
    #     line = doc.get_row(i)
    #     is_add = helper.add_all_bd(line)
    #     if not is_add:
    #         list_false.append(i)
    #     else:
    #         print(f"{i}| {is_add}")
        # is_del = helper.del_all_bd(line)
        # print(f"{i}| {is_del}")

    # data = helper.bd.select(helper.table_document, '*', {})
    # for line in data:
    #     print(line)

    # print(dict_false)
    helper.close()
