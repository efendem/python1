# from uuid import uuid4
# class Avto:
#     """Avtomobil klassi"""
#     def __init__(self,make,model,rang,yil,narh,km=0):
#         """Avtomobilning xususiyatlari"""
#         self.make = make
#         self.model = model
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()
    
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")
            class Avto:
                """Avtomobil klassi"""
num_avto = 0
def __init__(self,make,model,rang,yil,narh,km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.num_avto += 1