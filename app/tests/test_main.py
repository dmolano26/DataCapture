import unittest

from utils.data_capture import DataCapture


class TestMain(unittest.TestCase):
    def setUp(self):
        self.data_capture = DataCapture()
        self.data_capture.add_number(3)
        self.data_capture.add_number(9)
        self.data_capture.add_number(3)
        self.data_capture.add_number(4)
        self.data_capture.add_number(6)

        self.stats = self.data_capture.build_stats()

    def test_less(self):
        self.assertEqual(self.stats.less(4), 2)

    def test_greater(self):
        self.assertEqual(self.stats.greater(4), 2)

    def test_between(self):
        self.assertEqual(self.stats.between(3, 6), 4)


if __name__ == "__main__":
    unittest.main()
