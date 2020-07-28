class School(object):
    def __init__(self):
        self.school = {}

    def add_student(self, name, grade):
        if grade in self.school.keys():
            self.school[grade].append(name)
        else:
            self.school[grade] = [name]
        return self.school

    def roster(self):
        return [st for grade, students in sorted(self.school.items()) for st in sorted(students)]


    def grade(self, grade_number):
        if grade_number in self.school:
            return sorted(self.school[grade_number])
        else:
            return []
