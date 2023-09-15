import unittest
from utils import utils

class TestUtils(unittest.TestCase):

    def reversed_with_int(self):
        self.assertEqual(utils.reversed(123), 321)

    def reversed_with_str(self):
        # should fail
        with self.assertRaises(TypeError):
            utils.reversed("hello")

    def reversed_with_flt(self):
        # should fail
        with self.assertRaises(TypeError):
            utils.reversed(3.14)

    def formatter_with_int(self):
        self.assertEqual(utils.formatter(50), ('0b110010', '0o62'))

    def formatter_with_str(self):
        # should fail
        with self.assertRaises(TypeError):
            utils.formatter("hello")

    def formatter_with_flt(self):
        # should fail
        with self.assertRaises(TypeError):
            utils.formatter(3.14)

if __name__ == '__main__':
    unittest.main()