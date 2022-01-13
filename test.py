from algo import *
from jsonhelpers import putToJSON

subjectnames = ["COA", "DM", "DS", "Python",
                "BEFA", "MSF", "DS Lab", "Python Lab"]
subjectlist = [Subject(name) for name in subjectnames]

lecturernames = ["A", "B", "C", "D", "E", "F"]

lecturerslist = [Lecturer(name) for name in lecturernames]

lectsubjmap = {}

i = 0

for subject, lecturer in zip(subjectlist, lecturerslist):
    lectsubjmap[subject] = lecturer

slmap = SubjectLecturerMap(subjectlist, lecturerslist)

# lectsubjmap[subjectlist[-2]] = lecturerslist[2]
# lectsubjmap[subjectlist[-1]] = lecturerslist[3]

# print(lectsubjmap)

daynames = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", 'Saturday']

c1 = Class("AI ML", slmap)

# tt1 = constructRandomTimetable(c1)
# tt2 = constructRandomTimetable(c1)
# tt3 = getChildTimetable(c1, tt1, tt2)

# print(tt1)

# print(compareTables(tt1, tt3))
# print(compareTables(tt2, tt3))

t = [constructRandomTimetable(c1) for i in range(50)]
ta = t

for i in range(50):
    ta = selectiveBreed(ta, c1, mut=0.05)

ta[0].print()
print(calculateDefect(ta[0]))

putToJSON(ta[0].toJSON(), "tables")


# t = []
# for i in range(6):
#     t.append(constructRandomTimetable(c1, f"Timetable {i}"))

# print(calculateDefect(tt1))

# for tt in t:
#     print(f"{tt.name} has {calculateDefect(tt)} defects.")
