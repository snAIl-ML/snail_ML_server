import path_helper_test_main
import unittest
from snailMLserver import app

class SnailMLServerTestCase(unittest.TestCase):

    def test_index_page_has_upload_form(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'form action="/upload" method="post"' in response.data)

    def spurious_post_test(self):
        tester = app.test_client(self)
        response = tester.post('/upload_test',
            content_type="text",
            data={'image': "2018-05-03 18-11-43forwards.jpg"})

    def test_uploading_an_image_returns_forwards_pivot_left_or_pivot_right(self):
        tester = app.test_client(self)
        response = tester.post('/upload',
            content_type="multipart/form-data",
            data={'image': "2018-05-03 18-11-43forwards.jpg"})
        print(response.data)
        self.assertEqual(response.status_code, 200)
        forward_response = b'forwards' in response.data
        pivot_left_response = b'pivot_left' in response.data
        pivot_right_response = b'pivot_right' in response.data
        self.assertTrue(forward_response or pivot_left_response or pivot_right_response)

if __name__ == "__main__":
    unittest.main()
