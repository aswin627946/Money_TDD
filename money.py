class Money:
    def __init__(self, x=0):
        parts = str(x).split('.')
        self.rupee = int(parts[0])
        if len(parts) > 1:
            self.paise = int(parts[1][:2]) if len(parts[1]) >= 2 else 0
        else:
            self.paise = 0

    def __add__(self, obj2):
        obj3 = Money()
        obj3.rupee = self.rupee + obj2.rupee
        obj3.paise = self.paise + obj2.paise
        while obj3.paise >= 100:
            remainder = obj3.paise % 100
            obj3.rupee += (obj3.paise - remainder) // 100
            obj3.paise %= 100
        return obj3
    
    def __mul__(self, x):
        obj3 = Money()
        obj3.rupee = self.rupee * x
        obj3.paise = self.paise * x
        if obj3.paise >= 100:
            remainder = obj3.paise % 100
            obj3.rupee += (obj3.paise - remainder) // 100
            obj3.paise %= 100
        return obj3

    def __sub__(self, obj2):
        obj3 = Money()
        obj3.rupee = self.rupee - obj2.rupee
        obj3.paise = self.paise - obj2.paise
        return obj3

    def __str__(self):
        if self.rupee < 0 and self.paise <= 0 or self.rupee < 0:
            return "UnderFlow\n\n"
        return f"{self.rupee} rupees, {self.paise} paise.\n"

