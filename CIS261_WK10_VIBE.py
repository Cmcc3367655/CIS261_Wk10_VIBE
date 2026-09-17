# Chris McCoy
# CIS261
# VIBE Coding

FILE_NAME = "student_grades.txt"


def calculate_average(scores):
	"""Return the average of a student's three test scores."""
	return sum(scores) / len(scores)


def calculate_letter_grade(average):
	"""Convert a percentage average to a letter grade."""
	if average >= 90:
		return "A"
	if average >= 80:
		return "B"
	if average >= 70:
		return "C"
	if average >= 60:
		return "D"
	return "F"


def read_text(prompt):
	"""Read a non-empty text value from the user."""
	while True:
		value = input(prompt).strip()
		if value:
			return value
		print("This value cannot be blank.")


def read_score(test_number):
	"""Read a valid test score from the user."""
	while True:
		try:
			score = float(input(f"Enter Test {test_number} score (0-100): "))
			if 0 <= score <= 100:
				return score
		except ValueError:
			pass
		print("Please enter a number from 0 to 100.")


def create_student(name, student_id, scores):
	"""Create an Option A student dictionary with calculated values."""
	average = calculate_average(scores)
	return {
		"name": name,
		"id": student_id,
		"test1": scores[0],
		"test2": scores[1],
		"test3": scores[2],
		"average": average,
		"grade": calculate_letter_grade(average),
	}


def add_student(students):
	name = read_text("Enter student name: ")
	student_id = read_text("Enter student ID: ")
	if any(student["id"].lower() == student_id.lower() for student in students):
		print("That student ID already exists.")
		return

	scores = [read_score(number) for number in range(1, 4)]
	students.append(create_student(name, student_id, scores))
	print("Student record added.")


def display_students(students):
	if not students:
		print("No student records found.")
		return

	print("\nStudent Grade Records")
	print("Name                 ID          Test 1   Test 2   Test 3   Average  Grade")
	print("-" * 78)
	for student in sorted(students, key=lambda record: record["name"].lower()):
		print(
			f"{student['name'][:20]:20} {student['id'][:10]:10} "
			f"{student['test1']:7.2f}  {student['test2']:7.2f}  "
			f"{student['test3']:7.2f}  {student['average']:7.2f}  {student['grade']:>5}"
		)


def display_statistics(students):
	if not students:
		print("No student records found.")
		return

	averages = [student["average"] for student in students]
	highest = max(students, key=lambda student: student["average"])
	lowest = min(students, key=lambda student: student["average"])
	print("\nClass Statistics")
	print(f"Highest average: {highest['average']:.2f} ({highest['name']})")
	print(f"Lowest average: {lowest['average']:.2f} ({lowest['name']})")
	print(f"Class average: {sum(averages) / len(averages):.2f}")


def search_students(students):
	search_text = read_text("Enter a student name to search: ").lower()
	matches = [student for student in students if search_text in student["name"].lower()]
	if matches:
		display_students(matches)
	else:
		print("No students matched that name.")


def save_students(students):
	try:
		with open(FILE_NAME, "w", encoding="utf-8") as file:
			for student in students:
				file.write(
					f"{student['name']}|{student['id']}|{student['test1']:.2f}|"
					f"{student['test2']:.2f}|{student['test3']:.2f}|"
					f"{student['average']:.2f}|"
					f"{student['grade']}\n"
				)
		print(f"Saved {len(students)} student record(s) to {FILE_NAME}.")
	except OSError as error:
		print(f"Could not save student records: {error}")


def load_students():
	students = []
	try:
		with open(FILE_NAME, "r", encoding="utf-8") as file:
			for line_number, line in enumerate(file, start=1):
				if not line.strip():
					continue
				parts = line.rstrip("\n").split("|")
				if len(parts) != 7:
					print(f"Skipped invalid record on line {line_number}.")
					continue
				try:
					students.append(
						{
							"name": parts[0],
							"id": parts[1],
							"test1": float(parts[2]),
							"test2": float(parts[3]),
							"test3": float(parts[4]),
							"average": float(parts[5]),
							"grade": parts[6],
						}
					)
				except ValueError:
					print(f"Skipped invalid record on line {line_number}.")
	except FileNotFoundError:
		print("No saved student records found. Starting with an empty list.")
		return students
	except OSError as error:
		print(f"Could not load student records: {error}")
	return students


def main():
	students = load_students()
	menu = (
		"\nStudent Grade Calculator (Option A: list of dictionaries)\n"
		"1. Add student\n"
		"2. View all students\n"
		"3. View class statistics\n"
		"4. Search by student name\n"
		"5. Save records\n"
		"Press ESC to save and exit"
	)

	while True:
		print(menu)
		choice = input("Choose an option: ").strip()
		if choice in ("\x1b", "esc", "ESC"):
			save_students(students)
			print("Goodbye.")
			break
		if choice == "1":
			add_student(students)
		elif choice == "2":
			display_students(students)
		elif choice == "3":
			display_statistics(students)
		elif choice == "4":
			search_students(students)
		elif choice == "5":
			save_students(students)
		else:
			print("Please choose an option from 1 to 5, or press ESC to exit.")


if __name__ == "__main__":
	main()
