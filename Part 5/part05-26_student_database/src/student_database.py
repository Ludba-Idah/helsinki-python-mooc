def add_student(database: dict, name: str):
    if name not in database:
        database[name] = {}

def add_course(database: dict, name: str, course: tuple):
    course_name, grade = course
    if grade == 0:
        return
    if name in database:
        if course_name not in database[name] or grade > database[name][course_name]:
            database[name][course_name] = grade

def print_student(database: dict, name: str):
    if name not in database:
        print(f"{name}: no such person in the database")
        return
    
    courses = database[name]
    print(f"{name}:")
    if not courses:
        print(" no completed courses")
    else:
        print(f" {len(courses)} completed courses:")
        total_grade = 0
        for c_name, c_grade in courses.items():
            print(f"  {c_name} {c_grade}")
            total_grade += c_grade
        avg = total_grade / len(courses)
        print(f" average grade {avg}")

def summary(database: dict):
    print(f"students {len(database)}")
    
    most_courses = -1
    best_student_courses = ""
    
    best_avg = -1.0
    best_student_avg = ""
    
    for name, courses in database.items():
        count = len(courses)
        if count > most_courses:
            most_courses = count
            best_student_courses = name
            
        if count > 0:
            avg = sum(courses.values()) / count
            if avg > best_avg:
                best_avg = avg
                best_student_avg = name
                
    print(f"most courses completed {most_courses} {best_student_courses}")
    print(f"best average grade {best_avg} {best_student_avg}")
