class Garden(object):
    PLANTS = {
    'R': 'Radishes',
    'C': 'Clover',
    'G': 'Grass',
    'V': 'Violets'
    }

    DEFAULT_STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']

    def __init__(self, diagram, students=DEFAULT_STUDENTS):
        self.diagram = [list(x) for x in diagram.split("\n")]
        self.students = sorted(students)
    
    def plants(self, student):
        student_index = self.students.index(student) * 2
        plants = [x[student_index:student_index+2] for x in self.diagram]
        return [self.PLANTS[item] for sub in plants for item in sub]

