import unittest
import ddt
@ddt.ddt
class a(unittest.TestCase):

    @ddt.data({'first': 1, 'second': 3, 'third': 2},
          {'first': 4, 'second': 6, 'third': 5})
    @ddt.unpack
    def test_dicts_extracted_into_kwargs(self, first, second, third):
        self.assertTrue(first < third < second)

if __name__=="__main__":
    unittest.main()