from lib.name_initials import name_initials

def test_name_initials():
    assert name_initials("Nguyen Tado") == "N.T"
    assert name_initials("Anamaria Lopez") == "A.L"
    print("✅", end=" ")