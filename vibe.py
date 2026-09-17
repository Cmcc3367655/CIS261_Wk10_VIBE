#Chris McCoy
#CIS261
#VIBE Coding


def calculate_average(scores):
	"""Return the average of a student's test scores."""
	return sum(scores) / len(scores) if scores else 0.0


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


def read_score():
	"""Read a valid test score from the user."""
	while True:
		try:
			score = float(input("Enter a test score (0-100): "))
			if 0 <= score <= 100:
				return score
		except ValueError:
			pass
		print("Please enter a number from 0 to 100.")


def read_student_id():
	"""Read a non-empty student ID."""
	while True:
		student_id = input("Enter student ID: ").strip()
		if student_id:
			return student_id
		print("Student ID cannot be blank.")


def add_student(students):
	student_id = read_student_id()
	if student_id in students:
		print("That student already exists.")
		return

	name = input("Enter student name: ").strip()
	while not name:
		print("Student name cannot be blank.")
		name = input("Enter student name: ").strip()

	scores = []
	while True:
		scores.append(read_score())
		if input("Add another score? (y/n): ").strip().lower() != "y":
			break

	students[student_id] = {"name": name, "scores": scores}
	print("Student record added.")


def display_student(student_id, student):
	average = calculate_average(student["scores"])
	grade = calculate_letter_grade(average)
	scores = ", ".join(f"{score:.1f}" for score in student["scores"])
	print(f"\nID: {student_id}")
	print(f"Name: {student['name']}")
	print(f"Scores: {scores}")
	print(f"Average: {average:.2f}")
	print(f"Grade: {grade}")


def view_students(students):
	if not students:
		print("No student records found.")
		return
	for student_id, student in sorted(students.items()):
		display_student(student_id, student)


def update_scores(students):
	student_id = read_student_id()
	if student_id not in students:
		print("Student not found.")
		return

	students[student_id]["scores"].append(read_score())
	print("Score added.")
	display_student(student_id, students[student_id])


def remove_student(students):
	student_id = read_student_id()
	if students.pop(student_id, None) is None:
		print("Student not found.")
	else:
		print("Student record removed.")


def main():
	students = {}
	menu = (
		"\nStudent Record Manager\n"
		"1. Add student\n"
		"2. View all students\n"
		"3. Add a test score\n"
		"4. Remove student\n"
		"5. Exit"
	)

	while True:
		print(menu)
		choice = input("Choose an option: ").strip()
		if choice == "1":
			add_student(students)
		elif choice == "2":
			view_students(students)
		elif choice == "3":
			update_scores(students)
		elif choice == "4":
			remove_student(students)
		elif choice == "5":
			print("Goodbye.")
			break
		else:
			print("Please choose an option from 1 to 5.")


if __name__ == "__main__":
	main()
