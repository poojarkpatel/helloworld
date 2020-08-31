import unittest
from helloworld import hello_world


class Test(unittest.TestCase):
    def hello_world(self):
        self.assertEqual(hello_world(), "Hello World!")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
