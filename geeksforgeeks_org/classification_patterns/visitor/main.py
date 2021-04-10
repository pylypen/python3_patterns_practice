class Courses_At_GFG:
    def accept(self, visitor):
        visitor.visit(self)

    def teaching(self, visitor):
        print(self, "Taught by ", visitor)

    def studying(self, visitor):
        print(self, "studied by ", visitor)

    def __str__(self):
        return self.__class__.__name__


class SDE(Courses_At_GFG):
    pass


class STL(Courses_At_GFG):
    pass


class DSA(Courses_At_GFG):
    pass


class Visitor:
    def __str__(self):
        return self.__class__.__name__


class Instructor(Visitor):
    def visit(self, crop):
        crop.teaching(self)


class Student(Visitor):
    def visit(self, crop):
        crop.studying(self)


if __name__ == "__main__":
    sde = SDE()
    stl = STL()
    dsa = DSA()

    instructor = Instructor()
    student = Student()

    sde.accept(instructor)
    sde.accept(student)

    stl.accept(instructor)
    stl.accept(student)

    dsa.accept(instructor)
    dsa.accept(student)
