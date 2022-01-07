# Entity is the base class for all other entities to inherit from
# Provides methods to implement the str() function, the tostring() function,
#   the repr() function, and a basic constructor
# Has one attribute: name

class Entity:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return self.name

    def tostring(self):
        return self.name

    def __repr__(self) -> str:
        return self.name

# Class to represent a specific Subject
# Lacks any attributes, is just present for convenience


class Subject(Entity):
    def __init__(self, name):
        super().__init__(name)

    def __str__(self) -> str:
        return super().__str__()

# Class to represent a specific lecturer or professor
# Has one attribute, subjects, which is a list of Subjects that are taught by this Lecturer


class Lecturer(Entity):
    def __init__(self, name, subjects=[]):
        super().__init__(name)
        self.subjects = subjects

    def __str__(self) -> str:
        return self.name

# Class to represent a specific period
# Has one attribute: a subject


class Period(Entity):
    def __init__(self, name, subject=None):
        super().__init__(name)
        self.subject = subject

    def __str__(self) -> str:
        return str(self.subject)

# Class to represent a single day in a Timetable
# Has one attribute, hours, a list of Hours that constitute this Day, usually of a length of 6.


class Day(Entity):
    def __init__(self, name, hours=[]):
        super().__init__(name)
        self.hours = hours

    def __str__(self) -> str:
        return super().__str__()

# Class to represent a timetable
# Contains a list of days in the timetable.


class Timetable(Entity):
    def __init__(self, name, days=[], slmap = None):
        super().__init__(name)
        self.days = days
        self.slmap = slmap

    def __str__(self) -> str:
        return self.name

    def print(self):
        i = 0
        for day in self.days:
            print(f"Day {i}: ")
            j = 0
            for hour in day.hours:
                print(f"{hour} {j}: {hour.period.subject}")
                j += 1
            i += 1


# Class to represent a specific class, or section, with one shared timetable.
# Has two attributes:
#   LectSubj: a SubjectLecturerMap containing maps between subjects and lecturers
#   timetable: the timetable shared by this specific Class


class Class(Entity):
    def __init__(self, name, lectsubj, timetable=None):
        super().__init__(name)
        self.lectsubj = lectsubj
        self.timetable = timetable

    def __str__(self) -> str:
        return super().__str__()

# Class to represent an hour in a Day
# Has one attribute: the period taking up the hour


class Hour(Entity):
    def __init__(self, name, period=None):
        super().__init__(name)
        self.period = period

# Class to implement a lecturer-subject map mapping lecturers to subjects


class SubjectLecturerMap(Entity):
    def __init__(self, subj, lect):
        self.map = dict()
        for lectsub in zip(subj, lect):
            self.map[lectsub[0]] = lectsub[1]

    def __getitem__(self, key):
        return self.map[key]
