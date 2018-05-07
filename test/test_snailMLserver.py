import path_helper_test_main
from snailMLserver import app

def test_index_page_has_upload_form():
    tester = app.test_client()
    response = tester.get('/', content_type='html/text')
    assert (response.status_code) == 200
    assert (b'form action="/upload" method="post"' in response.data)

def test_uploading_an_image_returns_forwards_pivot_left_or_pivot_right():
    #nb test image has to be in root for this test to work, some problem
    # with the way the filepath is handled...
    tester = app.test_client()
    response = tester.post('/upload', data={'image': open('test_image_forwards.jpg', 'rb')})
    assert (response.status_code) == 200
    forward_response = b'forward' in response.data
    pivot_left_response = b'pivot_left' in response.data
    pivot_right_response = b'pivot_right' in response.data
    assert (forward_response or pivot_left_response or pivot_right_response)
