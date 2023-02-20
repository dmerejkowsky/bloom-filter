from collections import Counter
import pytest
from faker import Faker
from bloom import hash_input, Algorithms, get_index


def test_sha1():
    input = "abc"
    output = "a9993e36 4706816a ba3e2571 7850c26c 9cd0d89d"
    actual = hash_input(input, Algorithms.SHA1)
    assert actual.hex() == output.replace(" ", "")


def test_sha256():
    input = "abc"
    output = "ba7816bf 8f01cfea 414140de 5dae2223 b00361a3 96177a9c b410ff61 f20015ad"
    actual = hash_input(input, Algorithms.SHA256)
    assert actual.hex() == output.replace(" ", "")


def test_sha512():
    input = "abc"
    output = "ddaf35a193617aba cc417349ae204131 12e6fa4e89a97ea2 0a9eeee64b55d39a 2192992a274fc1a8 36ba3c23a3feebbd 454d4423643ce80e 2a9ac94fa54ca49f"
    actual = hash_input(input, Algorithms.SHA512)
    assert actual.hex() == output.replace(" ", "")


def test_get_index_for_abc_and_max_size_16():
    input = "abc"
    max_index = 16
    index = get_index(input, algorithm=Algorithms.SHA1, max_index=max_index)
    assert 0 <= index < max_index


def test_get_index_is_uniform():
    """
    This calls the get_index() method and displays a histogram of the results

    You can call it repeatedly and see if histograms make sense

    I *think* you could write a proper test by computing Chi Square, but this
    is more fragile than simply *looking* at the histogram with human eyes :)
    """
    fake = Faker()
    counter = Counter()
    max_index = 16
    for i in range(0, 100):
        input = fake.pystr()
        index = get_index(input, algorithm=Algorithms.SHA1, max_index=max_index)
        counter.update([index])
    keys = sorted(counter.keys())
    print()
    for k in keys:
        print(k, "*" * counter[k])
