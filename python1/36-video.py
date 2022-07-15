# def get_full_name(ism, familiya):
#     return f"{ism} {familiya}".title()
#     import unittest
# from name import get_full_name

# class NameTest(unittest.TestCase):
#     def test_toliq_ism(self):
#         formatted_name = get_full_name('alijon','valiyev')        
#         self.assertEqual(formatted_name, 'Alijon Valiyev')

#         unittest.main()
# def get_full_name(ism, familiya, otasi=''):
#     if otasi:
#         return f"{ism} {otasi} {familiya}"   
#     else:
#         return f"{ism} {familiya}".title()
import unittest
from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        formatted_name = get_full_name('alijon','valiyev')        
        self.assertEqual(formatted_name, 'Alijon Valiyev')
    def test_toliq_ism_otasi(self):
        name = get_full_name('hasan','husanov','olimovich')
        self.assertEqual(name,'Hasan Olimovich Husanov')

unittest.main()