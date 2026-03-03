import pytest

COUNTER_KEY = 'test_cache/counter'

def test_cache(cache):  # cache persists values between test runs
    value = cache.get(COUNTER_KEY, 0)
    print("\nCounter before:", value)
    cache.set(COUNTER_KEY, value + 1)  # cache fixture is similar to dictionary, but with .set() and .get() methods
    value = cache.get(COUNTER_KEY, 0)  # cache fixture is similar to dictionary, but with .set() and .get() methods
    print("\nCounter after:", value)
    assert True   # Make test successful

def hello():
    print("Hello, pytesting world")

def test_capsys(capsys):
    hello()  # Call function that writes text to STDOUT
    out, err = capsys.readouterr()  # Get captured output
    assert out == "Hello, pytesting world\n"

@pytest.mark.parametrize("num", range(3))
def test_temp_dir(tmpdir, num):
    print("TEMP DIR:", tmpdir, "\n")  # tmpdir fixture provides unique temporary folder name

