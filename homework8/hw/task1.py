class KeyValueStorage:
    """
    Allows to open .txt file with key:value data, store it and gran access
    with dict methods.
    """

    def __init__(self, path: str):
        self.__path = path
        self.__dict = {}
        with open(self.__path, "r") as data:
            lines = data.readlines()
            for line in lines:
                key, value = line.strip().split("=")
                self.__dict[key] = value

    def __getitem__(self, key):
        return self.__dict[key]

    def __getattr__(self, key):
        """
        In case value can be cast to int - it would be returned as int.
        """
        value = self.__dict[key]
        try:
            int(value)
        except ValueError:
            return value
        else:
            return int(value)
