from lib.battle_of_chars import battle_of_chars

def xtest_battle_of_chars():
    assert battle_of_chars("AAA", "Z") == "Z"
    assert battle_of_chars("ONE", "TWO") == "TWO"
    assert battle_of_chars("ONE", "NEO") == "Tie!"
    assert battle_of_chars("FOUR", "FIVE") == "FOUR"
    print("✅", end=" ")
