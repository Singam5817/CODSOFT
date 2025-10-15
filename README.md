# 💻 CODSOFT Python Programming Internship Tasks

This repository documents and hosts my solutions for the tasks completed during the CodSoft Python Programming Internship. The projects focus on fundamental Python concepts, demonstrating proficiency in user input handling, control flow, modular programming, and utilizing essential Python libraries (`random`, `string`).

## 🛠️ Prerequisites

To run these projects locally, you need:

1.  **Python 3** (3.6 or newer recommended)
2.  **Git** (for cloning the repository)

## 🚀 Getting Started

Follow these steps to get a local copy of the projects up and running on your machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Singam5817/CODSOFT.git](https://github.com/Singam5817/CODSOFT.git)
    cd CODSOFT
    ```

2.  **Run any task** using the Python interpreter:
    ```bash
    # Example: Run the To-Do List Application
    python3 to_do_list.py
    ```

---

## 🎯 Task Breakdown and Features

### 1. Task 1: To-Do List Application (`to_do_list.py`)

This is a command-line application designed to help users manage their daily tasks.

| Feature | Description |
| :--- | :--- |
| **Add Task** | Allows the user to input and append a new task to the list. |
| **View List** | Displays all tasks with a clear status indicator (e.g., `[ ]` or `[✓]`). |
| **Mark Done** | Allows the user to select a task by number and update its status to "completed" (tracking). |
| **Persistence** | *Future enhancement: Add file I/O to save the list between sessions.* |

### 2. Task 2: Simple Calculator (`calculator.py`)

A basic command-line tool that handles fundamental arithmetic.

| Feature | Description |
| :--- | :--- |
| **Operations** | Supports **Addition (`+`), Subtraction (`-`), Multiplication (`*`), and Division (`/`)**. |
| **Input Validation** | Uses `try...except` blocks to handle non-numeric inputs gracefully. |
| **Error Handling** | Includes specific logic to prevent and notify the user about **division by zero** errors. |

### 3. Task 3: Password Generator (`password_generator.py`)

A utility for generating strong, high-entropy passwords based on user specifications.

| Feature | Description |
| :--- | :--- |
| **User Input** | Prompts the user to specify the exact **desired length** of the password. |
| **Complexity** | The password character pool includes: **Lowercase letters, Uppercase letters, Digits (0-9), and Symbols (punctuation)** using the `string` module. |
| **Randomness** | Employs the `random.choices` function to ensure an unpredictable selection of characters. |

### 4. Task 4: Rock-Paper-Scissors Game (`rock_paper_scissors.py`)

An interactive game played against a computer opponent.

| Feature | Description |
| :--- | :--- |
| **User Input** | Accepts and validates input for "rock," "paper," or "scissors." |
| **Computer AI** | Uses the `random.choice` function to simulate a random, unbiased computer opponent. |
| **Core Logic** | Implements the full RPS win/lose ruleset. |
| **Score Tracking** | **(Optional Requirement fulfilled)** Keeps a running score for the user and the computer across multiple rounds. |
| **Play Again** | **(Optional Requirement fulfilled)** Asks the user if they want to play another round before exiting. |

---

## 👤 Author : Singam Somesh Kumar

* **GitHub:** Singam5817

**Thank you, CodSoft, for the learning opportunity!**
