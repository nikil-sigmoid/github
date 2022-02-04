from string_ops.concat import main3


def test_concat():
    assert main3.concat("Nice", " Code!") == "Nice Code!"
