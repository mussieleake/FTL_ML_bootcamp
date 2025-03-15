import sqlite3


def create_database():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT NOT NULL,
            first_name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def insert_students():
    students = [
        ("Smith", "John", 15),
        ("Doe", "Jane", 16),
        ("Lee", "Alex", 14)
    ]

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO students (last_name, first_name, age) VALUES (?, ?, ?)", students)

    conn.commit()
    conn.close()


def add_student():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    age = int(input("Enter age: "))

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (last_name, first_name, age) VALUES (?, ?, ?)", (last_name, first_name, age))

    conn.commit()
    conn.close()

    print("Student added successfully!")


def update_student():
    student_id = int(input("Enter student ID to update: "))
    new_age = int(input("Enter new age: "))

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET age = ? WHERE id = ?", (new_age, student_id))

    conn.commit()
    conn.close()

    print("Student record updated successfully!")


def query_students():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    for student in students:
        print(f"ID: {student[0]}, Name: {student[2]} {student[1]}, Age: {student[3]}")

    conn.close()


def delete_student():
    student_id = int(input("Enter student ID to delete: "))

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))

    conn.commit()
    conn.close()

    print(f"Student with ID {student_id} deleted successfully!")


def main():
    create_database()  
    insert_students()  

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Query Students")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":


            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            query_students()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")


main()
