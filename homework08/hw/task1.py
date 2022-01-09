import keyword


class KeyValueStorage:
    """
    Allows to open .txt file with key:value data, store it and grant access
    with dict methods.
    """

    def __init__(self, path: str):
        with open(path, "r") as data:
            lines = data.readlines()
            for line in lines:
                key, value = line.strip().split("=")
                if self.isidentifier(key):
                    try:
                        int(value)
                    except ValueError:
                        self.__dict__[key] = value
                    else:
                        self.__dict__[key] = int(value)

    def __getitem__(self, key):
        """
        In case value can be cast to int - it would be returned as int.
        """
        return self.__dict__[key]

    @staticmethod
    def isidentifier(key: str) -> bool:
        """Determines if string is valid Python identifier."""
        if not isinstance(key, str):
            raise TypeError("expected str, but got {!r}".format(type(key)))
        if not key.isidentifier():
            return False
        if keyword.iskeyword(key):
            return False
        if key in dir(object):
            return False
        return True
