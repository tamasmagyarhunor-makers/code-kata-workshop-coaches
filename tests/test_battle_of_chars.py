from lib.battle_of_chars import battle_of_chars

def test_battle_of_chars():
    assert battle_of_chars("AAA", "Z") == "Z", "Unfair fight"
    assert battle_of_chars("ONE", "TWO") == "TWO", "Unfair fight!"
    assert battle_of_chars("ONE", "NEO") == "Tie!", "Unfair fight!"
    assert battle_of_chars("FOUR", "FIVE") == "FOUR", "Unfair fight!"
    print("✅", end=" ")
