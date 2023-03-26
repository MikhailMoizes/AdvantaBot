from pymysql import connect, OperationalError
from DB.sql_provider import SQLProvider
from config import db_config
provider = SQLProvider("D:\\advantaGetData\DB\queries")

class DBConnection:

    def __init__(self, config):
        self.config = config

    def __enter__(self):
        errors = {
            1049: 'Неверное имя базы данны',
            1045: 'Неверный логин или пароль',
            2003: 'Неверный адрес'
        }
        try:
            self.conn = connect(**self.config)
            self.cursor = self.conn.cursor()
            return self.cursor
        except OperationalError as err:
            print(errors.get(err.args[0]))
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        errors = {
            'Курсор None': 'Курсор не создан',
            1064: 'Синтаксическая ошибка в запросе',
            1146: 'Ошибка в запросе. Таблицы не существует',
            1054: 'Ошибка в запросе. Поля не существует'
        }
        if exc_val is None:
            self.conn.commit()
            self.conn.close()
            self.cursor.close()
        else:
            print('Errors:', errors.get(exc_val.args[0]))
        return True


def work_with_db(sql):
    result = []
    with DBConnection(db_config) as cursor:
        cursor.execute(sql)
        schema = [column[0] for column in cursor.description]
        for item in cursor.fetchall():
            result.append(dict(zip(schema, item)))
        return result


def db_update_table(sql):
    with DBConnection(db_config) as cursor:
        if cursor is None:
            raise ValueError('Курсор None')
        elif cursor:
            cursor.execute(sql)
