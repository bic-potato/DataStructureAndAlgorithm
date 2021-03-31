class People():
    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(People):
    def __init__(self, name, age, sno):
        super().__init__(name, age)
        self.sno = sno

    def getSno(self):
        return self.sno


class Xdict(dict):
    def __init__(self, func, *iterables):
        super().__init__(func, *iterables)

    def getKeys(self, value):
        list1 = []
        for i in self.keys():
            if type(self[i]) == str or type(self[i]) == int:
                if value == self[i]:
                    list1.append(i)
            else:
                if value in self[i]:
                    list1.append(i)
        return list1

