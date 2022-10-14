import pytest

from school_schedule.student import Student
from compare import get_student_with_more_classes


def test_class_with_currect_attributes():
        # Arrange
        name = "Claire"
        grade = "freshmen"
        classes = [
        "Algebra", 
        "Writing", 
        "Contemporary Issues", 
        "Gym", 
        "Earth Science", 
        "Painting"
        ]
        # Act

        student = Student(name, grade, classes)

        # Assert
        assert student.name == "Claire"
        assert student.grade == "freshmen"
        assert student.classes == [
        "Algebra", 
        "Writing", 
        "Contemporary Issues", 
        "Gym", 
        "Earth Science", 
        "Painting"
        ]


def test_adding_one_class_increases_class_length():
        # Arrange
        name = "Ellis"
        grade = "junior"
        classes = ["Painting"]

        ellis = Student(name, grade, classes)

        # Act
        ellis.add_class("Geography")
        
        # Assert
        assert len(ellis.classes) == 2

def test_get_num_classes_returns_int_len_of_classes():
        # Arrange
        name = "Quinn",
        grade = "junior"
        classes = [
        "Pre-Calc", 
        "English III", 
        "World History", 
        "Gym", 
        "Chemistry", 
        "Music Composition"
        ]
        quinn = Student(name, grade, classes)
        # Act
        num_of_classes = quinn.get_num_classes()

        #Assert
        assert type(num_of_classes) == int
        assert num_of_classes == 6
        

def test_add_class_adds_correct_class_to_list():
        # Arrange
        name = "Ellis"
        grade = "junior"
        classes = ["Painting"]

        ellis = Student(name, grade, classes)

        # Act
        ellis.add_class("Geography")
        
        # Assert
        assert len(ellis.classes) == 2

def test_empty_list_creates_student_with_empty_class_list():
        # Arrange
        name = "Ellis"
        grade = "junior"
        classes = []

        # Act
        ellis = Student(name, grade, classes)

        # Assert
        assert len(ellis.classes) == 0

def test_compare_returns_student_with_more_classes():
        name = "Ellis"
        grade = "junior"
        classes = ["Painting"]

        name = "Ellis Jr"
        grade = "junior"
        classes = ["Drawing", "Sketching"]

        ellis = Student(name, grade, classes)
        ellis_jr = Student(name, grade, classes)

        student_with_more_classes = get_student_with_more_classes(ellis, ellis_jr)
