print("----Initializing Dropbox For Students----")


class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, submission_date, is_submitted, grade, submitted_files):
        self.student_name = student_name
        self.student_id = student_id
        self.assignment_title = assignment_title
        self.submission_date = submission_date
        self.is_submitted = is_submitted
        self.grade = grade
        self.submitted_files = submitted_files

    def add_file(self, file_name):
        if self.is_submitted:
            print(f"---> [Error] {self.student_name} Cannot add file '{file_name}' after the assignment has been graded.")
            return

        if file_name in self.submitted_files:
            print(f"---> [Warning] {self.student_name} '{file_name}' already exists in the submission.")
        else:
            self.submitted_files.append(file_name)
            print(f"---> [Success] {self.student_name} File '{file_name}' added to the submission.")

    def remove_file(self, file_name):
        if self.is_submitted:
            print(f"---> [Error] {self.student_name} Cannot remove file '{file_name}' after the assignment has been graded.")
            return

        if file_name in self.submitted_files:
            self.submitted_files.remove(file_name)
            print(f"---> [Success] {self.student_name} '{file_name}' removed from the submission.")
        else:
            print(f"---> [Error] {self.student_name} '{file_name}' not found in the submission.")

    def assign_grade(self, grade):
        self.grade = grade
        self.is_submitted = True
        if self.is_submitted and grade < 100:
            print(f"---> [Success] {self.student_name} Grade {grade} assigned to {self.student_name}'s submission.")
        else:
            print(f"---> [Error] {self.student_name} Cannot grade. No files submitted for Jose Reyes.")
        

    def view_files(self):
        if not self.submitted_files:
            return "No files submitted."
        return self.submitted_files

    def display_submission_details(self):
        print(f"Student Name: {self.student_name}")
        print(f"Student ID: {self.student_id}")
        print(f"Assignment Title: {self.assignment_title}")
        print(f"Submission Date: {self.submission_date}")

    def is_submitted_on_time(self, due_date):
        return self.submission_date <= due_date

    def get_status_report(self):
        return (
            f"Student Name: {self.student_name}\n", f"|"
            f"Student ID: {self.student_id}\n", f"|"
            f"Assignment Title: {self.assignment_title}\n", f"|"
            f"Submission Date: {self.submission_date}", f"|"
        )



student1 = AssignmentSubmission(
    "Alex Gonzaga", "pshs-1090", "CS 101","2026-10-01", False, None, []
)

student2 = AssignmentSubmission(
    "Adelle", "pshs-1920-x", "CS 103","2026-10-01", False, None, []
)

student3 = AssignmentSubmission(
    "Juan dela", "pshs-1033-x", "CS-101", "2026-10-01", False, None, []
)

student4 = AssignmentSubmission(
    "Maria Santos", "pshs-1044-x", "CS-101","2026-10-01", False, None, []
)

student5 = AssignmentSubmission(
    "Jose Reyes", "pshs-1055-x", "CS-101","2026-10-01", False, None, []
)


print("---- TEST SCENARIO 1: Multiple Files via List ----")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")


print("---- TEST SCENARIO 2: Removing Files from List ----")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.docx")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")


print("---- TEST SCENARIO 3: Preventing Duplicate Files ----")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Juan's Files: {student3.view_files()}\n")


print("---- TEST SCENARIO 4: Removing file after being graded ----")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()


print("---- TEST SCENARIO 5: Empty List Handling ----")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()


print("--- Final System Report ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())