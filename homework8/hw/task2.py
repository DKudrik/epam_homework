import sqlite3


class TableData:
    def __init__(self, db_name, tb_name):
        self.__db_name = db_name
        self.__tb_name = tb_name
        with sqlite3.connect(self.__db_name) as conn:
            self.__cursor = conn.cursor()

    def __len__(self):
        self.__cursor.execute(f"SELECT * FROM {self.__tb_name}")
        data = []
        while row := self.__cursor.fetchone():
            data.append(row)
        return len(data)

    def __iter__(self):
        self.__cursor.execute(f"SELECT * FROM {self.__tb_name}")
        data = []
        while row := self.__cursor.fetchone():
            data.append(row)
        names = list(map(lambda x: x[0], self.__cursor.description))
        output = [dict(zip(names, data[index])) for index, name in enumerate(names)]
        return iter(output)

    def __getitem__(self, key):
        self.__cursor.execute(
            f"SELECT * FROM {self.__tb_name} WHERE name=:name", {"name": key}
        )
        data = self.__cursor.fetchone()
        return data

    def __contains__(self, item):
        return self.__cursor.execute(
            f"SELECT * FROM {self.__tb_name}  WHERE name=:name", {"name": item}
        ).fetchone()
