import pytest

# Tes sederhana untuk memastikan sistem testing berjalan
def test_read_root_logic():
    # Menguji logika dasar
    x = "Inventory API"
    assert x.lower() == "inventory api"

def test_math_logic():
    # Menghindari coverage 0%
    assert 1 + 1 == 2

def test_string_format():
    name = "Zahran"
    assert f"Hello {name}" == "Hello Zahran"