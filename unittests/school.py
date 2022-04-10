class Students:

    def __init__(self, surname: str, group_number: int, estimates: list):
        self.surname = surname
        self.group_number = group_number
        self.estimates = estimates


class School:

    def __init__(self):
        self.students = list()

    def add_student(self, student):
        self.students.append(student)

    def marks(self, *marks):
        answer = ''
        for student in self.students:
            if all([mark in marks for mark in student.estimates]):
                answer += student.surname + ' '
        return answer

    def group(self, group: int):
        answer = ''
        for student in self.students:
            if student.group_number == group:
                answer += student.surname + ' '
        return answer

    def automat(self, automat: int):
        answer = ''
        students_with_automat = [
                student for student in self.students
                if sum(student.estimates) / len(student.estimates) >= automat]
        for student in students_with_automat:
            answer += student.surname + ' '
        return answer
