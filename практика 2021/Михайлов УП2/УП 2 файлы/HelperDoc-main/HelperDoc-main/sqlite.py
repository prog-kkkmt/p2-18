import sqlite3


class Sqliter:
    def __init__(self, name_db):
        """
        Подключение к бд
        :param name_db: имя базы данных
        """
        self.connection = sqlite3.connect(name_db)
        self.cursor = self.connection.cursor()
        self.table = str()
        self.table_profession = "profession"
        self.table_qualification = "qualification"
        self.table_education_program = "education_program"
        self.table_student = "student"
        self.table_document = "document"

    @staticmethod
    def is_valid(table):
        """
        Валидна ли таблица
        :param table: название таблицы
        :return: True - если название таблицы подходит; False - если нет
        """
        is_valid = False

        if len(table) != 0 or type(table) == str:
            new_table = "".join(table.split('_'))
            is_valid = new_table.isalnum()
        return is_valid

    def connect_table(self, table):
        """
        Функция create_table создаёт таблицу в БД
        :param table: имя таблицы
        :return: True - если подключились к таблице, False - если нет
        """

        if table is None:
            table = self.table

        with self.connection:
            is_valid = self.is_valid(table)
            if is_valid:
                self.table = table
        return is_valid

    def get_qualification_id(self, title):
        """
        Вернет id записи от таблицы qualification.
        :return:
        """

        try:
            with self.connection:
                data = self.cursor.execute(
                    f'SELECT `id` FROM {self.table_qualification} WHERE `title` = \'{title}\'').fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def add_qualification(self, title: str):
        """
        Функция add добавляет данные в таблицу qualification
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_qualification}` (title) VALUES (?)", (title,))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_qualification: Такой пользователь уже существует")

        return is_valid

    def del_qualification(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_qualification} WHERE `id` = {pk}')
            self.save()

    def get_education_program_id(self, title):
        """
        Вернет id записи от таблицы student.
        :return:
        """

        try:
            with self.connection:
                data = self.cursor.execute(
                    f'SELECT `id` FROM {self.table_education_program} WHERE `title` = \'{title}\'').fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def add_education_program(self, title: str):
        """
        Функция add добавляет данные в таблицу education_program
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_education_program}` (title) VALUES (?)", (title,))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_education_program: Такой пользователь уже существует")

        return is_valid

    def del_education_program(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_education_program} WHERE `id` = {pk}')
            self.save()

    def get_profession_id(self, title):
        """
        Вернет id записи из таблицы profession
        :return:
        """

        try:
            with self.connection:
                data = self.cursor.execute(
                    f'SELECT `code` FROM {self.table_profession} WHERE `title` = \'{title}\'').fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def add_profession(self, code: str, title: str):
        """
        Функция add добавляет данные в таблицу profession
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_profession}` (code, title) VALUES (?,?)", (code, title))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_profession: Такой пользователь уже существует")

        return is_valid

    def del_profession(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_profession} WHERE `code` = \'{pk}\'')
            self.save()

    def get_student_id(self, name, last_name, middle_name, birth_date, gender,
                       snills, country_code, education_form, education_receipt_form,
                       financing_source, admission_year, graduation_year, study_period,
                       profession_code, qualification_id, education_program_id
                       ):
        """
        Вернет id студента от таблицы student
        :return:
        """

        try:
            with self.connection:
                command = f'SELECT `id` FROM {self.table_student} WHERE `name` = ? AND \
                    `last_name` = ? AND `middle_name` = ? AND \
                    `birth_date` = ? AND `gender` = ? AND \
                    `snills` = ? AND `country_code` = ? AND \
                    `education_form` = ? AND \
                    `education_receipt_form` = ? AND \
                    `financing_source` = ? AND \
                    `admission_year` = ? AND \
                    `graduation_year` = ? AND \
                    `study_period` = ? AND \
                    `profession_code` = ? AND \
                    `qualification_id` = ? AND \
                    `education_program_id` = ?'
                args = (
                    name, last_name, middle_name, birth_date, gender,
                    snills, country_code, education_form, education_receipt_form,
                    financing_source, admission_year, graduation_year, study_period,
                    profession_code, qualification_id, education_program_id
                )
                data = self.cursor.execute(command, args).fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def add_student(self, name, last_name, middle_name, birth_date, gender,
                    snills, country_code, education_form, education_receipt_form,
                    financing_source, admission_year, graduation_year, study_period,
                    profession_code, qualification_id, education_program_id
                    ):
        """
        Функция add добавляет данные в таблицу student
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_student}` (name, last_name, middle_name, birth_date, \
                gender, snills, country_code, education_form, education_receipt_form, financing_source, \
                admission_year, graduation_year, study_period, profession_code, qualification_id, \
                education_program_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                    (name, last_name, middle_name, birth_date, gender,
                                     snills, country_code, education_form, education_receipt_form,
                                     financing_source, admission_year, graduation_year, study_period,
                                     profession_code, qualification_id, education_program_id))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_student: Такой пользователь уже существует")

        return is_valid

    def del_student(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_student} WHERE `id` = {pk}')
            self.save()

    def get_document_id(self, title, type, series, number, loss_confirmation, exchange_confirmation,
                        destruction_confirmation, education_level, issue_date, registration_number,
                        status, student_id):
        """
        Вернет id студента от таблицы student
        :return:
        """

        try:
            with self.connection:
                data = self.cursor.execute(
                    f'SELECT `id` FROM {self.table_document} WHERE `title` = \'{title}\' AND \
                    `type` = \'{type}\' AND `series` = \'{series}\' AND \
                    `number` = \'{number}\' AND `loss_confirmation` = \'{loss_confirmation}\' AND \
                    `exchange_confirmation` = \'{exchange_confirmation}\' AND \
                    `destruction_confirmation` = \'{destruction_confirmation}\' AND \
                    `education_level` = \'{education_level}\' AND  `issue_date` = \'{issue_date}\' AND \
                    `registration_number` = \'{registration_number}\' AND `status` = \'{status}\' AND \
                    `student_id` = \'{student_id}\'').fetchall()
                if len(data) != 0:
                    return data[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def add_document(self, title, type, series, number, loss_confirmation, exchange_confirmation,
                     destruction_confirmation, education_level, issue_date, registration_number,
                     status, student_id):
        """
        Функция add добавляет данные в таблицу profession
        :return:
        """

        is_valid = False
        try:
            with self.connection:
                self.cursor.execute(f"INSERT INTO `{self.table_document}` (title, type, series, number, \
                loss_confirmation, exchange_confirmation, destruction_confirmation, education_level, issue_date, \
                registration_number,status, student_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (title, type, series, number,
                                                                                            loss_confirmation,
                                                                                            exchange_confirmation,
                                                                                            destruction_confirmation,
                                                                                            education_level,
                                                                                            issue_date,
                                                                                            registration_number,
                                                                                            status, student_id))
                self.save()
                is_valid = True
        except sqlite3.IntegrityError:
            print("add_document: Такой пользователь уже существует")

        return is_valid

    def del_document(self, pk):
        with self.connection:
            self.cursor.execute(f'DELETE FROM {self.table_document} WHERE `id` = {pk}')
            self.save()

    def get_id(self, table: str, name_pk: str, data: dict):
        """
        Вернет id студента от таблицы student
        :return:
        """

        try:
            with self.connection:
                command = f"SELECT `{name_pk}` FROM `{table}`"
                count = len(data)
                if count == 0:
                    return -1
                command += " WHERE "
                column_values = list()
                for key, value in data.items():
                    count -= 1
                    if value is not None:
                        command += f"`{key}` = ?"
                        column_values.append(value)
                        if count:
                            command += " AND "
                need_id = self.cursor.execute(command, tuple(column_values)).fetchall()
                if len(need_id) != 0:
                    return need_id[0][0]
                return -1
        except sqlite3.IntegrityError:
            return -1

    def get_last_id(self, table, name_pk):
        """
        Вернет последнее id записи из таблицы которую вы передадите
        :return:
        """

        try:
            with self.connection:
                return self.cursor.execute(f"SELECT MAX({name_pk}) FROM {table}").fetchall()[0][0]
        except sqlite3.IntegrityError:
            return -1

    def select(self, table: str, need: str, data: dict):
        """
        Вернет выбранные данные (need) из выбранной таблицы (table).
        Выборка происходит благодаря переданным данным (data)
        :return:
        """

        try:
            with self.connection:
                command = f"SELECT {need} FROM `{table}`"
                if len(data) == 0:
                    return self.cursor.execute(command).fetchall()
                command += " WHERE "
                column_values = list()
                count = len(data)
                for key, value in data.items():
                    command += f"`{key}` = ?"
                    column_values.append(value)
                    count -= 1
                    if count:
                        command += " AND "
                return self.cursor.execute(command, tuple(column_values)).fetchall()
        except sqlite3.IntegrityError:
            return -1

    # def get

    def update(self, table: str, pk: dict, data: dict):
        """
        Обновит выбранные данные (data) из выбранной таблицы (table).
        Выборка происходит благодаря id таблицы (pk)
        :param: все словари имеют следующий вид => {'имя_колоны': значение_колоны}
        :return:
        """

        try:
            with self.connection:
                column_values = list()
                command = f"UPDATE `{table}`"

                key_pk = list(pk.keys())[0]
                command += f" SET `{key_pk}` WHERE "
                column_values.append(pk[key_pk])
                count = len(data)
                for key, value in data.items():
                    column_values.append(value)
                    command += f"`{key}` = ?"
                    count -= 1
                    if count:
                        command += ", "
                return self.cursor.execute(command, tuple(column_values)).fetchall()
        except sqlite3.IntegrityError:
            return -1

    # Функция save сохраняет изменения в БД
    def save(self):
        self.connection.commit()
        # print(f"{self.cursor.rowcount} отредактированно строк")

    # Функция close закрывает БД
    def close(self):
        self.connection.close()
