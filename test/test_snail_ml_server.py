'Testing routes of the server'
import path_helper_test_main
from snail_ml_server import app

# MAIN INTERFACE TESTS
def test_index_page_has_x_SPURIOUS_AT_PRESENT():
    'test_index_page_has_x_SPURIOUS_AT_PRESENT'
    tester = app.test_client()
    response = tester.get('/', content_type='html/text')
    assert (response.status_code) == 200

# API TESTS
def test_uploading_an_image_returns_forwards_pivot_left_or_pivot_right():
    'test_uploading_an_image_returns_forwards_pivot_left_or_pivot_right'
    #nb test image has to be in root for this test to work, some problem
    # with the way the filepath is handled...
    tester = app.test_client()
    response = tester.post('/upload', data={'image': open('test_image_forwards.jpg', 'rb')})
    response_set = [b'forward', b'pivot_left', b'pivot_right']
    assert (response.status_code) == 200
    assert response.data in response_set

def test_image_classifier_allows_multiple_requests():
    'test_image_classifier_allows_multiple_requests'
    tester = app.test_client()
    response1 = tester.post('/upload', data={'image': open('test_image_forwards.jpg', 'rb')})
    response2 = tester.post('/upload', data={'image': open('test_image_forwards.jpg', 'rb')})
    response_set = [b'forward', b'pivot_left', b'pivot_right']
    assert (response1.status_code) == 200
    assert response1.data in response_set
    assert (response2.status_code) == 200
    assert response2.data in response_set
