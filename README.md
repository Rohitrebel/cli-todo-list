# CLI TodoList Application

This is a simple command-line based Todo List application built using Python. It allows users to **add**, **delete**, **view**, and **persist** tasks using a plain text file (`todo.txt`).

## Features

- Add new tasks (with duplicate prevention)
- Delete existing tasks (case-insensitive match)
- View all current tasks
- Save tasks for persistence
- Run multiple operations until user chooses to exit

## How it Works

- The program checks if todo.txt exists. If it does, it loads the tasks from it, otherwise creates it.
- When adding a task, it ensures no duplicate task is added (case-insensitive check).
- While deleting, it matches the task regardless of letter casing.
- You can save your tasks anytime by selecting the Save option.
- The application will continue to run until you select Stop.

## Getting Started

### Prerequisites

- Python 3.x installed on your system

### How to Run

1. Clone this repository or download the Python file.
2. Open your terminal or command prompt.
3. Run the script using:

```bash
python todo.py
```

## Output

![alt text](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1754383455/Screenshot_2403_edd6fk.png)
