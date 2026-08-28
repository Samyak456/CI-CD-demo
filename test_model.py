from app import predict_result


def test_model_pass_prediction():
    assert predict_result(80) == "PASS"


def test_model_fail_prediction():
    assert predict_result(25) == "FAIL"


def test_model_boundary_prediction():
    assert predict_result(40) == "PASS"