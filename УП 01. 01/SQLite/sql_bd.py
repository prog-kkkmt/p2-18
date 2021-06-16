#Выполнил: Кузнецов Матвей
#Группа: П2-18
'''
import sqlite3


class Sqliter:

    # Функция __init__ служит инициализацией БД
    def __init__(self, name_db):
        self.connection = sqlite3.connect(name_db)
        self.cursor = self.connection.cursor()

    # Функция create_table создаёт таблицу в нашей БД
    def create_table(self, table):
        with self.connection:
            table = ''.join(chr for chr in table if chr.isalnum())
            if table != '':
                self.cursor.execute(f"CREATE TABLE IF NOT EXISTS `{table}` (\
                    id integer PRIMARY KEY,\
                    `fio` text, `group` text, `direction` text)")
                self.save()

    # Функция add_student добавляет студента в БД, если его не существует
    def add_student(self, **kwargs):
        with self.connection:
            data = kwargs
            if kwargs.get('data') != None:
                data = kwargs['data']
            self.cursor.execute("INSERT INTO `students`\
                (`fio`, `group`, `direction`) VALUES (?, ?, ?)",
                (data['fio'], data['group'], data['direction']))
            self.save()

    # Функция get_id возвращает id записи в таблице
    def get_id(self, **kwargs):
        with self.connection:
            try:
                data = kwargs
                if kwargs.get('data') != None:
                    data = kwargs.get('data')
                return self.cursor.execute("SELECT * FROM `students` WHERE \
                    `fio` = ? AND `group` = ? AND `direction` = ?",
                    (data['fio'], data['group'], data['direction'])).fetchall()[0][0]
            except:
                return -1

    # Функция save сохраняет изменения в БД
    def save(self):
        self.connection.commit()
        print(f"{self.cursor.rowcount} отредактированно строк")

    # Функция close закрывает БД
    def close(self):
        self.connection.close()

# Функция input_student возвращает данные о студенте в нужном для БД формате
def input_student(**kwargs):
    data = kwargs
    if kwargs.get('data') != None:
        data = kwargs.get('data')
    student = {
        'fio': data['fio'],
        'group': data['group'],
        'direction': data['direction']
    }
    return student

# Создание БД
bd = Sqliter("bd")
# Создание таблицы students
bd.create_table('students')


student = input_student(fio="Cipkov Il'ya Vladimirovich",\
                        group="P1-18", direction="Programmer")
# Если студента не находит в БД, то мы его добавляем в БД
if bd.get_id(data=student) == -1:
    bd.add_student(data=student)
# Если такой студент существует, то в консоль выводит "Ne mogu("
else:
    print('Ne mogu(')

# Прекращение работы с БД
bd.close()
