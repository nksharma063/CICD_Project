import pytest, sys
from sqrt import *
def test_hello():
    a = hello()
    assert a == "hi breakout 4"

if __name__ == "__main__":
    exit_code = sys.exit(pytest.main(["-x", "test_sqrt.py"]))
    # result = (exit_code == 0)
    # print(result)