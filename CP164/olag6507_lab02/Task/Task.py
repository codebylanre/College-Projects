"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Olagunju Abdulbasit
ID:      169076507
Email:   olag6507@mylaurier.ca
__updated__ = "2023-09-20"
-------------------------------------------------------
"""

class Student:
    def __init__(self, student_name, student_id, semester, course_enrolled, total_marks):
        self.student_name = student_name
        self.student_id = student_id
        self.semester = semester
        self.course_enrolled = course_enrolled
        self.total_marks = total_marks

    def __str__(self):
        return f"{self.student_name}, {self.student_id}"
    
    def __eq__(self, other):
        return self.student_id == other.student_id
    
    def __add__(self, other):
        return self.total_marks + other.total_marks
    
    def __lt__(self, other):
        return self.total_marks < other.total_marks
    
    def __sub__(self, other):
        return self.total_marks - other.total_marks
    