from string_ops import main2


def test_main2():
    assert main2.to_upper("exAmplE_tExt") == "EXAMPLE_TEXT"
