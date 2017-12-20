import unittest

def split_on_dash(string):
    return string.split('-')


class TestSplitOnDash(unittest.TestCase):

    def test(self):
        self.assertEqual(split_on_dash('hi-hi'), ['hi', 'hi'])


if __name__ == '__main__':
    unittest.main()


