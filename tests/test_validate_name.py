import pytest

from gradebook import validate_name


@pytest.mark.parametrize("name", [
    "Ali Khan",
    "Muhammad Ali",
    "Ali-Khan",
])
def test_valid_names(name):
    assert validate_name(name) is True


@pytest.mark.parametrize("name", [
    "",
    "Ali123",
    "Ali@Khan",
])
def test_invalid_names(name):
    with pytest.raises(ValueError):
        validate_name(name)


def test_over_length_name():
    name = "A" * 51

    with pytest.raises(ValueError):
        validate_name(name)


@pytest.mark.parametrize("length,should_raise", [
    (0, True),
    (1, False),
    (49, False),
    (50, False),
    (51, True),
])
def test_name_length_boundaries(length, should_raise):
    name = "A" * length

    if should_raise:
        with pytest.raises(ValueError):
            validate_name(name)
    else:
        assert validate_name(name) is True