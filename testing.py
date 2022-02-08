import unittest
import h_unittest
class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = h_unittest.do_stuff(test_param)
        self.assertEqual(result,15)


unittest.g_unittest()


