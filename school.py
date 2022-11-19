class School:

    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster
        
    def add_student(self, name, grade_level):
        if grade_level in self.roster.keys():
            self.roster[grade_level].append(name)
        else:
            self.roster.update({grade_level: [name]})
            
    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        sorted_roster = {}
        for k, v in self.roster.items():
            sorted_roster[k] = sorted(v)
        return sorted_roster
    
    def __repr__(self):
        return f'Class: School, {self.name}'