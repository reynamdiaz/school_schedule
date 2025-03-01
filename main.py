from school_schedule.student import Student
from compare import get_student_with_more_classes

#first instance
quinn = Student(
        "Quinn", 
        "junior", 
        [
        "Pre-Calc", 
        "English III", 
        "World History", 
        "Gym", 
        "Chemistry", 
        "Music Composition"
        ]
    )

quinn.add_class("Painting")
quinn.get_num_classes()
quinn.summary()

# second instance
claire = Student(
        "Claire", 
        "freshmen", 
        [
        "Algebra", 
        "Writing", 
        "Contemporary Issues", 
        "Gym", 
        "Earth Science", 
        "Painting"
        ]
    )

claire.get_num_classes()
claire.summary()

# Extra:
# - create a function that will return the student with more classes
print(get_student_with_more_classes(quinn, claire))
# - create a test for that function