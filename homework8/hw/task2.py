import sqlite3


class TableData:
    def __init__(self, db_name, tb_name):
        self.__db_name = db_name
        self.__tb_name = tb_name
        self.__connection = sqlite3.connect(self.__db_name)

    def __len__(self):
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute(f"SELECT COUNT(*) FROM {self.__tb_name}")
        rows = self.__cursor.fetchone()
        return rows[0]

    def __iter__(self):
        """
        Recombines data from tuples so that getting data with a key during
        iteration could be done.
        For example:
        for president in presidents:
            print(president['name'])
        """
        self.__cursor = self.__connection.cursor()
        self.__cursor.execute(f"SELECT * FROM {self.__tb_name}")
        data = []
        while row := self.__cursor.fetchone():
            data.append(row)
        names = list(map(lambda x: x[0], self.__cursor.description))
        output = [dict(zip(names, data[index])) for index, name in enumerate(names)]
        return iter(output)

    def __getitem__(self, key):
        self.__cursor = self.__connection.cursor()
        return self.__cursor.execute(
            f"SELECT * FROM {self.__tb_name}  WHERE name=:name", {"name": key}
        ).fetchone()

    def __contains__(self, item):
        self.__cursor = self.__connection.cursor()
        if self.__cursor.execute(
            f"SELECT * FROM {self.__tb_name}  WHERE name=:name", {"name": item}
        ).fetchone():
            return True
        return False

    def __del__(self):
        self.__connection.close()
