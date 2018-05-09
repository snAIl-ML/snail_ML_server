import path_helper_test_ml
from classifier import get_model_name

def test_get_model_name_gets_model_name_from_model_folder():
    assert get_model_name("test/test_model") == 'test_model'
