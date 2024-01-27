from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message("socorro", "socorro")

    with pytest.raises(TypeError):
        encrypt_message(123, 123)

    assert encrypt_message("Cachorro", 20) == "orrohcaC"

    assert encrypt_message("Cachorro", 6) == "or_rohcaC"

    assert encrypt_message("Cachorro", 7) == "rrohcaC_o"

    assert encrypt_message("Cachorro", 1) == "C_orrohca"
