# 🎓 Student Management System

A command-line application to manage student records using Python.

Developed as part of the **Synent Technologies Python Development Internship**.

---

## ✨ Features

- ➕ Add new student records with auto-assigned ID
- 👁️ View all students in a formatted table
- 🔍 Search students by name or ID
- ✏️ Update any field of an existing student record
- 🗑️ Delete student records with confirmation prompt
- 📊 Summary report:
  - Total students
  - Average age
  - Grade breakdown
- 💾 All data saved automatically to `students.csv`
- 🔄 Data reloads automatically every time the program starts

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed

Uses only Python built-in modules:

- `os`
- `csv`

---

## 🚀 How to Run

```bash
python student_management.py
```

---

## 🖥️ Sample Output

```text
=======================================================
       STUDENT MANAGEMENT SYSTEM
  Synent Technologies - Python Internship
=======================================================

  0 record(s) loaded from students.csv

  MENU
  1. View all students
  2. Add student
  3. Search student
  4. Update student
  5. Delete student
  6. Summary
  7. Exit

  Enter choice (1-7): 2

  --- Add New Student ---
  Enter name    : Ruman Tanveer
  Enter age     : 21
  Enter grade   : A+
  Enter email   : ruman@email.com

  Student added! ID assigned: 1
```

---

## 📋 Student Record Fields

| Field | Description |
|-------|-------------|
| ID | Auto-assigned unique number |
| Name | Full name of the student |
| Age | Age of the student |
| Grade | Academic grade (A, B+, etc.) |
| Email | Student email address |

---

## 💾 Data Storage

All records are stored in `students.csv` in the same folder as the script.

The file is:

- Automatically created on first use
- Reloaded every time the program starts

So your data is never lost.

---

## 📁 Project Structure

```text
student-management/
│
├── student_management.py
├── students.csv
└── README.md
```

---

## 📚 Concepts Used

- Python Functions
- File Handling
- CSV Operations
- Lists and Dictionaries
- Loops and Conditional Statements
- Exception Handling
- User Input Validation

---

## 👤 Author

**Ruman Tanveer**  
Synent Technologies — Python Development Internship

---

## 📌 Tags

`#python` `#studentmanagement` `#internship` `#programming` `#technology`