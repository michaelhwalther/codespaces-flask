import unittest

class test_1(unittest.TestCase):

    def test1(self):
        return True
    
    def test2(self):
        self.fail("Actually, fail!")
