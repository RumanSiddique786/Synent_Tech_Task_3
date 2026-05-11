import os
import csv
 
FILE = "students.csv"
FIELDS = ["ID", "Name", "Age", "Grade", "Email"]
 
 
def load_students():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)
 
 
def save_students(students):
    with open(FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)
 
 
def get_next_id(students):
    if not students:
        return 1
    return max(int(s["ID"]) for s in students) + 1
 
 
def display_all(students):
    if not students:
        print("\n  No student records found.")
        return
    print()
    print("  " + "-" * 65)
    print("  {:<6} {:<22} {:<6} {:<8} {:<20}".format("ID", "Name", "Age", "Grade", "Email"))
    print("  " + "-" * 65)
    for s in students:
        print("  {:<6} {:<22} {:<6} {:<8} {:<20}".format(
            s["ID"], s["Name"], s["Age"], s["Grade"], s["Email"]
        ))
    print("  " + "-" * 65)
    print("  Total students: " + str(len(students)))
 
 
def add_student(students):
    print("\n  --- Add New Student ---")
    name = input("  Enter name    : ").strip()
    if not name:
        print("  Name cannot be empty.")
        return students
 
    age = input("  Enter age     : ").strip()
    if not age.isdigit():
        print("  Age must be a number.")
        return students
 
    grade = input("  Enter grade   : ").strip()
    email = input("  Enter email   : ").strip()
 
    student = {
        "ID": str(get_next_id(students)),
        "Name": name,
        "Age": age,
        "Grade": grade,
        "Email": email
    }
    students.append(student)
    save_students(students)
    print("  Student added! ID assigned: " + student["ID"])
    return students
 
 
def search_student(students):
    print("\n  --- Search Student ---")
    keyword = input("  Enter name or ID: ").strip().lower()
    results = [s for s in students if keyword in s["Name"].lower() or keyword == s["ID"]]
    if not results:
        print("  No student found.")
    else:
        display_all(results)
 
 
def update_student(students):
    print("\n  --- Update Student ---")
    sid = input("  Enter student ID to update: ").strip()
    for s in students:
        if s["ID"] == sid:
            print("  Record: " + s["Name"] + " | Age: " + s["Age"] + " | Grade: " + s["Grade"] + " | Email: " + s["Email"])
            print("  Press Enter to keep current value.")
            name  = input("  New name  [" + s["Name"]  + "]: ").strip()
            age   = input("  New age   [" + s["Age"]   + "]: ").strip()
            grade = input("  New grade [" + s["Grade"] + "]: ").strip()
            email = input("  New email [" + s["Email"] + "]: ").strip()
            if name:              s["Name"]  = name
            if age and age.isdigit(): s["Age"] = age
            if grade:             s["Grade"] = grade
            if email:             s["Email"] = email
            save_students(students)
            print("  Student updated successfully!")
            return students
    print("  ID " + sid + " not found.")
    return students
 
 
def delete_student(students):
    print("\n  --- Delete Student ---")
    sid = input("  Enter student ID to delete: ").strip()
    for s in students:
        if s["ID"] == sid:
            confirm = input("  Delete " + s["Name"] + "? (y/n): ").strip().lower()
            if confirm == "y":
                students.remove(s)
                save_students(students)
                print("  Student deleted successfully!")
            else:
                print("  Deletion cancelled.")
            return students
    print("  ID " + sid + " not found.")
    return students
 
 
def show_summary(students):
    if not students:
        print("\n  No data available.")
        return
    grades = {}
    for s in students:
        g = s["Grade"]
        grades[g] = grades.get(g, 0) + 1
    ages = [int(s["Age"]) for s in students if s["Age"].isdigit()]
    print()
    print("  --- Summary ---")
    print("  Total students : " + str(len(students)))
    if ages:
        print("  Average age    : " + str(round(sum(ages) / len(ages), 1)))
        print("  Youngest       : " + str(min(ages)))
        print("  Oldest         : " + str(max(ages)))
    print("  Grade breakdown:")
    for grade, count in sorted(grades.items()):
        print("    " + grade + " : " + str(count) + " student(s)")
 
 
def main():
    print("=" * 55)
    print("       STUDENT MANAGEMENT SYSTEM")
    print("  Synent Technologies - Python Internship")
    print("=" * 55)
 
    students = load_students()
    print("  " + str(len(students)) + " record(s) loaded from " + FILE)
 
    while True:
        print()
        print("  MENU")
        print("  1. View all students")
        print("  2. Add student")
        print("  3. Search student")
        print("  4. Update student")
        print("  5. Delete student")
        print("  6. Summary")
        print("  7. Exit")
        print()
        choice = input("  Enter choice (1-7): ").strip()
 
        if choice == "1":
            display_all(students)
        elif choice == "2":
            students = add_student(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            students = update_student(students)
        elif choice == "5":
            students = delete_student(students)
        elif choice == "6":
            show_summary(students)
        elif choice == "7":
            print("\n  Goodbye!\n")
            break
        else:
            print("  Invalid choice. Enter 1 to 7.")
 
 
if __name__ == "__main__":
    main()