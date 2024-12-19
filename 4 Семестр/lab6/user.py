from datetime import datetime


class User:

    def __init__(self, name, height):
        self._id = None
        self._name = name
        self._height = height
        self._created_at = datetime.now()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.isidentifier():
            raise ValueError("Некоректрое значение имени.")

        self._name = value

    @name.deleter
    def name(self):
        self._name = None

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def created_at(self):
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        self._created_at = value

    def dict(self):
        return {
            "id": self._id,
            "name": self._name,
            "height": self._height,
            "created": str(self._created_at)
        }


if __name__ == '__main__':
    u1 = User(1, 1.78, 'Max')
    print(u1)
