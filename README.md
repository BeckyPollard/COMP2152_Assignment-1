# COMP2152 - Assignment 1

## About

This repository contains my work for **Assignment 1** of the COMP2152 course. The assignment focuses on core Python fundamentals — working with variables, data types, dictionaries, lists, loops, conditionals, and user input — all within the context of a workout tracking program.

## Et voila
<img width="451" height="554" alt="Screenshot 2026-02-15 175851" src="https://github.com/user-attachments/assets/0ae1c936-d1f9-4823-86fe-866f5974a8e2" />


## The Assignment

The program tracks workout minutes (yoga, running, and weightlifting) for a group of friends. It covers the following tasks:

1. Define variables of different data types (`str`, `float`, `int`, `bool`) with inline comments identifying each type.
2. Build a dictionary (`workout_stats`) where each key is a friend's name and each value is a tuple of three workout durations.
3. Loop through the dictionary to calculate and store each friend's total workout minutes as new key-value pairs (e.g., `"Alex_Total": 95`).
4. Extract the workout data into a 2D nested list (`workout_list`) where rows represent friends and columns represent activities.
5. Use list slicing to pull out specific subsets of the data — yoga/running for everyone, and weightlifting for the last two friends.
6. Use an if-statement inside a loop to identify friends whose total is 120 minutes or more, and print a congratulatory message.
7. Accept user input to look up a specific friend's workout breakdown, or print a "not found" message if the name doesn't exist.
8. Determine and print which friend has the highest and lowest total workout minutes.

The full assignment instructions can be found in `Instructions1.md`.

## Repository Structure

```
.
├── assignment1_studentID.py       # Starter Python script (skeleton with step comments)
├── assignment1_studentID.ipynb    # Starter Jupyter Notebook (one cell per step)
├── Instructions1.md               # Full assignment instructions in Markdown
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## Starter Files

Both `assignment1_studentID.py` and `assignment1_studentID.ipynb` are provided as starter templates. They contain the multi-line author comment block at the top and a comment for each step (b through i) — no solution code. The notebook version has each step in its own cell so it runs cleanly in Jupyter.

Before working on the assignment, rename both files by replacing `studentID` with your actual student ID.

## .gitignore

The `.gitignore` is configured to keep the repo clean across different development environments. It covers:

- **Python** — bytecode, virtual environments, cache directories, coverage reports
- **Jupyter** — `.ipynb_checkpoints`
- **macOS / Windows / Linux** — OS-generated files like `.DS_Store`, `Thumbs.db`, etc.
- **Editors** — VS Code, PyCharm/JetBrains, Neovim/Vim, Sublime Text, Emacs
- **Secrets** — `.env`, `.pem`, `.key`, and credential files
- **Archives** — `.zip`, `.tar.gz`, `.rar`
