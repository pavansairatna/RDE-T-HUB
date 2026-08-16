"""
Student Grade Tracker
----------------------
Demonstrates lists + tuples working together in Python.

- Each student record is a TUPLE: (name, subject, score)
  -> immutable, because a single record's shape shouldn't change.
- The roster of all students is a LIST of those tuples.
  -> mutable, because we constantly add/remove/reorder students.

Run this file directly to try the interactive menu, or import the
functions into your own script / notebook.
"""

# ---------------------------------------------------------
# Starting data: a list of tuples
# ---------------------------------------------------------
students = [
    ("Ana", "Math", 92),
    ("Sam", "Science", 78),
    ("Leo", "Math", 65),
    ("Mia", "English", 88),
    ("Ben", "Science", 91),
]


# ---------------------------------------------------------
# Core operations
# ---------------------------------------------------------

def add_student(roster, name, subject, score):
    """Append a new (name, subject, score) tuple to the roster list."""
    record = (name, subject, score)  # tuple: fixed, immutable record
    roster.append(record)
    print(f'Added: {record}')


def remove_student(roster, name):
    """Remove the first record matching `name` from the roster."""
    for record in roster:
        if record[0].lower() == name.lower():
            roster.remove(record)
            print(f'Removed: {record}')
            return
    print(f'No student named "{name}" found.')


def find_student(roster, name):
    """Return the record tuple for a student, or None if not found."""
    for record in roster:
        if record[0].lower() == name.lower():
            return record
    return None


def show_all(roster):
    """Print every record in a simple formatted table."""
    if not roster:
        print("No students in the roster.")
        return

    print(f'\n{"Name":<10}{"Subject":<12}{"Score":>6}')
    print("-" * 28)
    for name, subject, score in roster:  # tuple unpacking
        print(f'{name:<10}{subject:<12}{score:>6}')
    print()


def sort_by(roster, key_index, descending=False):
    """
    Return a NEW sorted list (doesn't mutate the original).
    key_index: 0 = name, 1 = subject, 2 = score
    """
    return sorted(roster, key=lambda record: record[key_index], reverse=descending)


def class_stats(roster):
    """Return (average, highest_record, lowest_record) for the whole roster."""
    if not roster:
        return 0, None, None

    scores = [record[2] for record in roster]
    average = sum(scores) / len(scores)
    highest = max(roster, key=lambda r: r[2])
    lowest = min(roster, key=lambda r: r[2])
    return average, highest, lowest


def group_by_subject(roster):
    """Build a dict: {subject: [record, record, ...]} from the flat list."""
    groups = {}
    for record in roster:
        subject = record[1]
        groups.setdefault(subject, []).append(record)
    return groups


def demonstrate_immutability(record):
    """Try to modify a tuple directly to show why it raises a TypeError."""
    try:
        record[2] = 100  # this will fail -- tuples can't be changed in place
    except TypeError as e:
        print(f'Tried to edit {record} directly -> TypeError: {e}')
        print("That's the whole point of a tuple: once created, it's locked.")


# ---------------------------------------------------------
# Interactive menu
# ---------------------------------------------------------

def print_menu():
    print("""
--- Student Grade Tracker ---
1. Show all students
2. Add a student
3. Remove a student
4. Search for a student
5. Sort by score (high to low)
6. Sort by name (A-Z)
7. Show class stats (average / highest / lowest)
8. Group students by subject
9. Demonstrate tuple immutability
0. Quit
""")


def main():
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_all(students)

        elif choice == "2":
            name = input("Name: ").strip()
            subject = input("Subject: ").strip()
            try:
                score = int(input("Score: ").strip())
            except ValueError:
                print("Score must be a number.")
                continue
            add_student(students, name, subject, score)

        elif choice == "3":
            name = input("Name to remove: ").strip()
            remove_student(students, name)

        elif choice == "4":
            name = input("Name to search: ").strip()
            result = find_student(students, name)
            if result:
                n, subj, sc = result  # unpack the tuple
                print(f'Found: {n} — {subj} — {sc}')
            else:
                print("Not found.")

        elif choice == "5":
            show_all(sort_by(students, key_index=2, descending=True))

        elif choice == "6":
            show_all(sort_by(students, key_index=0))

        elif choice == "7":
            avg, high, low = class_stats(students)
            print(f'\nAverage score: {avg:.1f}')
            print(f'Highest: {high}')
            print(f'Lowest: {low}\n')

        elif choice == "8":
            groups = group_by_subject(students)
            for subject, records in groups.items():
                print(f'\n{subject}:')
                for r in records:
                    print(f'   {r}')
            print()

        elif choice == "9":
            if students:
                demonstrate_immutability(students[0])
            else:
                print("Add a student first.")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
