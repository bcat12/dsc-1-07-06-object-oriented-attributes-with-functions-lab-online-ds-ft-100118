
import copy
class School:
    def __init__(self, name):
        self.name = name
        self._roster = {}
    def roster(self):
        return self._roster
    def add_student(self, studentname, grade):
        if grade in self.roster:
            self._roster[grade.append(name)
        else:
            self._roster[grade]=(studentname)
        return self._roster
     
    def grade(grade):
        return self._roster[grade]
    def sort_roster:
        new_dict = copy.deepcopy(self._roster)
        for key in new_dict:
            new_dict[key].sort()
        return new_dict