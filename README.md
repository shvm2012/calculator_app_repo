# 🧮 Calculator App Blueprint

**Manager:** Shivam  
**Project:** Beginner-friendly Python calculator for learning Git and GitHub collaboration

A simple command-line calculator built with Python. This project is intentionally small so learners can focus on how a team collaborates using **repositories, commits, branches, pushes, pulls, merges, and pull requests**.

---

## 📌 Project Overview

The calculator accepts two integer inputs and displays the results of five operations:

| Operation | Function | Description |
|---|---|---|
| Addition | `add(a, b)` | Returns the sum of two numbers |
| Subtraction | `sub(a, b)` | Returns the difference `a - b` |
| Multiplication | `mul(a, b)` | Returns the product of two numbers |
| Division | `div(a, b)` | Returns `a / b`, unless the divisor is zero |
| Sum of squares | `sqr_and_sum(a, b)` | Returns `a² + b²` |

The application uses Python's built-in `input()` function to collect values and `print()` to display results. It does not require third-party Python packages.

## ✨ Features

- Simple, beginner-friendly Python functions.
- Separate functions for each calculator operation.
- Division-by-zero handling.
- An `if __name__ == "__main__":` guard to control when the interactive program runs.
- Comments that document the intended feature-branch collaboration exercise.

## 🗂️ Project Structure

```text
calculator-app/
├── calculator.py   # Calculator functions and command-line interface
└── README.md       # Project overview, instructions, and learning guide
```

## 🚀 Getting Started

### Requirements

- Python 3 installed on your computer.
- A terminal or command prompt.
- Git and GitHub (recommended for the collaboration exercises).

### Run the application

1. Save the calculator code in a file named `calculator.py`.
2. Open a terminal in the directory containing the file.
3. Run:

   ```bash
   python calculator.py
   ```

   Depending on your system, you may need to use:

   ```bash
   python3 calculator.py
   ```

4. Enter two integers when prompted.

### Example

For inputs `10` and `5`, the output will look like this:

```text
Enter 1st Number: 10
Enter 1st Number: 5
Sum : 15
Diff : 5
Mul : 50
Sq_Sum : 125
Div : 2.0
```

> **Note:** The current program uses the same prompt text, `Enter 1st Number:`, for both inputs. You may wish to change the second prompt to `Enter 2nd Number:` as a small improvement exercise.

If the second number is `0`, division returns the message `operation not defined`. The other operations still run.

## 🧠 How the Code Works

### 1. Addition

```python
def add(a, b):
    return a + b
```

Takes two values and returns their sum. For example, `add(10, 5)` returns `15`.

### 2. Subtraction

```python
def sub(a, b):
    return a - b
```

Returns the first number minus the second. For example, `sub(10, 5)` returns `5`.

### 3. Multiplication

```python
def mul(a, b):
    return a * b
```

Returns the product of the two numbers. For example, `mul(10, 5)` returns `50`.

### 4. Division

```python
def div(a, b):
    if b == 0:
        return "operation not defined"
    else:
        return a / b
```

Checks whether the divisor is zero before dividing. If `b == 0`, it returns a message instead of attempting an invalid division. Otherwise, it returns the quotient.

### 5. Sum of squares

```python
def sqr_and_sum(a, b):
    return a**2 + b**2
```

Squares each number and adds the results:

`a² + b²`

For example, with `a = 10` and `b = 5`, the result is `10² + 5² = 125`.

## 🔍 Understanding the Main Guard

At the bottom of the file:

```python
if __name__ == "__main__":
```

Python sets `__name__` to `"__main__"` when the file is run directly. The code inside this block therefore runs when you execute `python calculator.py`.

If another Python file imports `calculator.py` to use its functions, the interactive input-and-print section will not run automatically. This makes the functions easier to reuse in other scripts and tests.

## 🌿 Git and GitHub Collaboration Exercise

This calculator is designed to demonstrate how multiple contributors can work on separate features.

### Contributors and feature branches

The comments in the supplied code document the following contributions:

| Feature | Function / output | Contributor | Branch recorded in the code |
|---|---|---|---|
| Addition | `add()` and sum output | Shivam | `main` |
| Subtraction | `sub()` and difference output | Shivam | `main` |
| Multiplication | `mul()` and multiplication output | Shivam | `feature_3_mul_shivam` |
| Division | `div()` and division output | Pavan | `feature_4_division_pavan` |
| Sum of squares | `sqr_and_sum()` and squared-sum output | Chaya | `feature_5_squared_sum_chaya` |

These comments describe the intended teaching scenario; they are not proof of Git history. To verify actual authorship, branch history, or merge status, inspect the commits and pull requests in the repository.

### Suggested classroom workflow

1. **Create a repository:** Add `calculator.py` and this `README.md`.
2. **Commit the baseline:** Commit the initial project to `main`.
3. **Create feature branches:** Each learner creates a branch for one assigned function.
4. **Implement the feature:** Add or update the function and its corresponding output line.
5. **Commit the change:** Use a descriptive commit message, such as `Add multiplication feature`.
6. **Push the branch:** Publish the branch to GitHub.
7. **Open a pull request:** Explain what the feature changes and request a review.
8. **Review and merge:** Merge the feature into `main` after review.
9. **Update local `main`:** Pull the latest merged changes before starting another feature.
10. **Clean up:** Delete a merged feature branch if it is no longer needed.

### Example Git commands

```bash
# Check the current branch and working tree
git status

# Create and switch to a feature branch
git switch -c feature_3_mul_shivam

# Stage and commit the changes
git add calculator.py
git commit -m "Add multiplication feature"

# Push the branch to GitHub
git push -u origin feature_3_mul_shivam
```

After the branch is merged through GitHub, update the local `main` branch before starting the next feature:

```bash
git switch main
git pull origin main
```

If the branch already exists locally, switch to it with `git switch <branch-name>` rather than creating it again. GitHub Desktop can be used for the same workflow through its graphical interface.

## 🧪 Practice Tasks

Try these small improvements as separate Git branches:

- [ ] Change the second input prompt to `Enter 2nd Number:`.
- [ ] Improve the division-by-zero message.
- [ ] Add a function that calculates the average of the two numbers.
- [ ] Add a function that returns the larger number.
- [ ] Add basic tests for all five operations.
- [ ] Update the README when a new feature is merged.

For a merge-conflict demonstration, ask two learners to edit the same line on separate branches, then resolve the conflict together. For normal feature work, assigning separate functions helps reduce conflicts.

## ⚠️ Current Limitations

- Inputs are converted to integers, so decimal values are not supported by the current interface.
- The input prompts use the same wording for both numbers.
- Division by zero returns a string, while successful division returns a numeric result.
- There is no input validation for non-integer entries.
- The project does not currently include automated tests.

These are intentional opportunities for future feature branches and code-review exercises.

---

## 🎯 Learning Goals

By completing this project, learners can practice:

- Understanding the difference between Git and GitHub.
- Creating and managing repositories.
- Committing, pushing, and pulling changes.
- Creating branches for independent features.
- Collaborating through pull requests and merges.
- Understanding and resolving merge conflicts.
- Reviewing file history and reverting changes safely.

**Keep the app simple; use Git to teach the collaboration workflow.**