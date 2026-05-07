class Xisob:
    def __init__(self, son):
        self._son = son

    @property
    def son(self):
        return self._son

    @son.setter
    def son(self, value):
        if isinstance(value, (int, float)):
            self._son = value
        else:
            raise TypeError("Sonlar faqat butun yoki o'nlik son bo'lishi mumkin")

    @son.deleter
    def son(self):
        del self._son

class Test:
    def __init__(self):
        self.xisob = Xisob(10)

    def test_property(self):
        print(self.xisob.son)  # 10
        self.xisob.son = 20
        print(self.xisob.son)  # 20
        del self.xisob.son
        try:
            print(self.xisob.son)
        except AttributeError:
            print("Son o'chirilgan")

test = Test()
test.test_property()
```

@property dekoratori getter metodni yaratadi. U getter metodni obyektning xususiyati sifatida ishlatishga imkon beradi. Shuningdek, u setter metodni yaratadi, agar getter metod yaratilgan bo'lsa. Setter metod obyektning xususiyati uchun setter metodni yaratadi. @son.deleter dekoratori esa deleter metodni yaratadi, agar getter metod yaratilgan bo'lsa. Deleter metod obyektning xususiyati uchun deleter metodni yaratadi.
