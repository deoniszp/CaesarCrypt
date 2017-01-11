from django.test import TestCase
from appCrypt.views import Crypt
# Create your tests here.

class ShiftTest(TestCase):
    def SetUp(self):
        pass

    def test_shift(self):
        self.assertEquals(Crypt.encrypt_msg('abcd', 2), 'cdef')
        self.assertEquals(Crypt.decrypt_msg('zzz  fff', 5), 'uuu aaa')
        self.assertEquals(Crypt.encrypt_msg('The early english text society', 11),
                          'esp plcwj pyrwtds epie dzntpej')

        self.assertEquals(Crypt.decrypt_msg('esp plcwj pyrwtds epie dzntpej', 11),
                          'the early english text society')