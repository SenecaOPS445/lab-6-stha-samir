#!/usr/bin/env python3

class Student:
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)
        self.courses = {}

    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        if len(self.courses) == 0:
            return 'GPA of student ' + self.name + ' is 0.0'
        gpa = 0.0
        for course in self.courses:
            gpa += self.courses[course]
        return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))

    def displayCourses(self):
        passed_courses = []
        for course, grade in self.courses.items():
            if grade != 0.0:
                passed_courses.append(course)
        return passed_courses

if __name__ == '__main__':
    samir = Student('Samir', 789012345)
    samir.addGrade('math101', 4.0)
    samir.addGrade('ops445', 3.0)
    samir.addGrade('ipc144', 0.0)

    print(samir.displayStudent())
    print(samir.displayGPA())
    print(samir.displayCourses())

