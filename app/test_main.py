from app.main import check_password
import pytest


@pytest.mark.parametrize(
    "password,result",
    [
        ("Pass@word1", True),
        ("Pas@1", False),
        ("Pass@word123456789", False),
        ("Pass@word", False),
        ("Password1", False),
        ("pass@word1", False),
        ("Pass@word1/", False),
        ("Pa1@word", True),
        ("Pass@word123456", True),
    ],
    ids=[
        "valid password",
        "too short",
        "too long",
        "without digit",
        "without special char",
        "without uppercase char",
        "invalid special char",
        "valid 8 char password",
        "valid 16 char password",
    ]
)
def test_simple_cases(password: str, result: bool) -> None:
    assert check_password(password) == result
