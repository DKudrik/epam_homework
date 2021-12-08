import sqlite3


class TableData:
    def __init__(self, db_name, tb_name):
        self.__db_name = db_name
        self.__tb_name = tb_name
        with sqlite3.connect(self.__db_name) as conn:
            self.__cursor = conn.cursor()

    def __len__(self):
        query = f"SELECT * FROM {self.__tb_name}"
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        return len(rows)

    def __iter__(self):
        query = f"SELECT * FROM {self.__tb_name}"
        self.__cursor.execute(query)
        data = self.__cursor.fetchall()
        names = list(map(lambda x: x[0], self.__cursor.description))
        output = [dict(zip(names, data[index]))
                  for index, name in enumerate(names)]
        return iter(output)

    def __getitem__(self, key):
        query = f"SELECT * FROM {self.__tb_name} WHERE name = '{key}'"
        self.__cursor.execute(query)
        data = self.__cursor.fetchone()
        return data

    def __contains__(self, item):
        query = f"SELECT * FROM {self.__tb_name}  WHERE name = '{item}'"
        return self.__cursor.execute(query).fetchone()
