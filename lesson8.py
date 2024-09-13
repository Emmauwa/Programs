# Define student records using tuples
student1 = ("Emmanuel Ong", 18, "Grade 14")
student2 = ("Hannah Mary", 17, "Grade 14")
student3 = ("Ned Flanders", 24, "Grade 20")

# Create a tuple of student records
students = (student1, student2, student3)

# Use tuple methods
print(f"Number of students: {len(students)}")
print(f"Index of Hannah Mary: {students.index(student2)}")

# Create sets to store unique student IDs and courses.
studentIDs = {1,2,3,4,5}
courses = {"English","Math","Science","History","Geography"}

# Perform set operations
print(f"Student IDs: {studentIDs}")
print(f"Courses: {courses}")

newStudents = {6,7}
studentIDs.update(newStudents)
print(f"Updated student IDs: {studentIDs}")

completedCourses = {"Math", "History"}
remainingCourses = courses - completedCourses
print(f"Remaining courses: {remainingCourses}")

# Use frozen sets
frozenCourses = frozenset(["Math", "Science", "English", "History"])
print(f"Frozen Courses: {frozenCourses}")

# Attempt to modify a frozen set (will raise an error)
# frozen_courses.add("Art")  # Uncommenting this line will raise an AttributeError

# Create a frozen set of student data
frozenStudentsData = frozenset(students)
print(f"Frozen Students Data: {frozenStudentsData}")
