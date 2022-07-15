x = 10
print(type(x))
matn = "salom"
print(type(matn))
def salom_ber():
    print("Assalom alaykum")

print(type(salom_ber))
matn = "salom"
print(matn.upper())
son = 20
print(son.lower())

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil