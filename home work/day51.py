frontend_students = {"joseph", "Ashik", "Vishnu", "Anu"}
backend_students = {"joseph", "vishnu", "salman", "Nithin"}
backend_students.add("ashok")

frontend_students.discard("Anu")

both_courses = frontend_students & backend_students
print("Students in both courses:", both_courses)

only_backend = backend_students - frontend_students
print("Students only in Backend:", only_backend)

unique_students = frontend_students | backend_students
print("Total unique students:", len(unique_students))

course_enrollments = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}

for course, count in course_enrollments.items():
    print(f"{course}: {count} students")
   
    fullstack_enrollments = {
    **course_enrollments,
    "Fullstack": len(frontend_students & backend_students)
}
print("Course enrollments including Fullstack:", fullstack_enrollments)