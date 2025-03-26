## 🛠 **Workshop Instructions: Breaking Down Problems & Incremental Implementation**

### 🎯 **Workshop Objectives**
By the end of this workshop, learners will:
- Understand the importance of breaking down even small but complex problems into manageable tasks.
- Learn how to identify implementation steps required to solve a problem.
- Practice implementing and testing step by step to reach a working final solution.

---

### 👩‍🏫 **Step 1: Coach Demonstration (Live Example)**

#### 1️⃣ Introduce the Problem
> "Let’s solve a coding challenge together. Here's our test suite that describes the desired behavior of a function called `battle_of_chars`."

```python
from lib.battle_of_chars import battle_of_chars

def test_battle_of_chars():
    assert battle_of_chars("AAA", "Z") == "Z"
    assert battle_of_chars("ONE", "TWO") == "TWO"
    assert battle_of_chars("ONE", "NEO") == "Tie!"
    assert battle_of_chars("FOUR", "FIVE") == "FOUR"
    print("✅", end=" ")
```

#### 2️⃣ Read and Understand the Problem Together
- Ask the group: “What do we think this function is supposed to do?”
- Discuss what each test case is telling us about the expected output.
- Clarify expectations:
  - The goal of the `battle_of_chars` function is to determine which of the two input strings has the higher total character score.
  - Each letter has a score based on its position in the alphabet (e.g., A=1, B=2, ..., Z=26).
  - Calculate the total score of each string.
  - The string with the higher score wins.
  - If the scores are equal, return "Tie!".
- Encourage learners to verbalize the *goal* of the function and observe patterns in the test cases.

#### 3️⃣ Break Down the Problem into Tasks (Group Discussion)
Ask students:
- "What are the *small steps* we need to take to build this function?"
- "How can we compare two strings?"
- "What’s a good strategy to determine which string wins?"
- Write down the tasks suggested by learners on a whiteboard or shared doc. E.g.:
```python
def battle_of_chars():
  # Convert each letter to a score.
  # Calculate total score of each string.
  # Compare both totals.
  # Return the string with higher score or "Tie!" if equal.

  # code below
```

#### 4️⃣ Start Implementing Step by Step
- Write the first few lines of `battle_of_chars` together.
- After each small implementation:
  - Run the test.
  - Celebrate partial success.
  - Adjust or extend the code.
- Let learners observe how the solution *evolves* through small, validated steps.

---

### 🚀 **Step 2: Student Challenge**

#### 1️⃣ Present the New Challenge
> "Now it’s your turn. Here’s a new function called `name_initials`, and a test suite that defines what it should do."

```python
# Setting up
## create a virtual environment for this project
$ python3 -m venv venv

## Enter the virtual environment
$ source venv/bin/activate

## Install pytest
$ pip install pytest

## Run the tests
$ pytest tests/test_name_initials.py -v

## Edit the lib/name_initials.py file until test passes
```



```python
from lib.name_initials import name_initials

def test_name_initials():
    assert name_initials("Nguyen Tado") == "N.T"
    assert name_initials("Anamaria Lopez") == "A.L"
    print("✅", end=" ")
```

#### 2️⃣ Instructions for Students
- Read and understand what the tests are asking.
- Discuss in pairs:
  - What steps will be needed to solve this?
- Start coding:
  - Implement small tasks one by one.
  - Run the test after each meaningful change.
- Encourage students to follow the same workflow:
  - Break it down → Implement → Test → Refine.

---

### ✅ **Wrap Up**
- Ask students what they learned about the process of problem-solving and testing.
- Reinforce the habit of:
  - **Reading the tests carefully**
  - **Breaking down problems into tasks**
  - **Testing often and early**

