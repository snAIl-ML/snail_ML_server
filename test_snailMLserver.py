import unittest
from snailMLserver import app

class SnailMLServerTestCase(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello!')

if __name__ == "__main__":
    unittest.main()
