class Money:
    def __init__(self, x=0):
        self.rupee = int(x)
        self.paise = int((x - int(x)) * 100)

    def __add__(self, obj2):
        obj3 = Money()
        obj3.rupee = self.rupee + obj2.rupee
        obj3.paise = self.paise + obj2.paise
        while obj3.paise >= 100:
            remainder = obj3.paise % 100
            obj3.rupee += (obj3.paise - remainder) // 100
            obj3.paise %= 100
        return obj3


    def __str__(self):
        if self.rupee < 0 and self.paise <= 0:
            return "UnderFlow\n\n"
        return f"{self.rupee} rupees, {self.paise} paise.\n"

