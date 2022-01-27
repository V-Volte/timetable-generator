from typing import List
from scripts.classes import *
import random
import threading


def calculateDefect(timetable: Timetable) -> int:
    defects = 0
    subjects = {}
    for s in list(timetable.slmap.map.keys()):
        subjects[s] = 0
    for day in timetable.days:
        ss = {}
        for s in list(timetable.slmap.map.keys()):
            ss[s] = 0
        for i in range(1, 6):
            if day.hours[i].period.subject == day.hours[i - 1].period.subject:
                defects += 4
        for hour in day.hours:
            ss[hour.period.subject] += 1
        for s in ss:
            if ss[s] >= 3:
                defects += ss[s] - 2
    for day in timetable.days:
        for h in day.hours:
            subjects[h.period.subject] += 1

    for i in range(len(subjects.keys())):
        defects += 2 * abs(subjects[list(subjects.keys())[i]] -
                           getExpectedCount(list(subjects.keys())[i], timetable.slmap))

    return defects


def getExpectedCount(s: Subject, slmap: SubjectLecturerMap) -> int:
    sl = [sb for sb in slmap.map]
    sd = {}
    for subj in sl:
        sd[subj] = 6
    return sd[s]


def calculateDefects(timetables: List[Timetable]) -> int:
    defects = 0

    for timetable in timetables:
        for ott in timetables:
            if (ott == timetable):
                continue
            for i in range(len(timetable.days)):
                for j in range(len(timetable.days[i].hours)):
                    if timetable.slmap[timetable.days[i].hours[j].period.subject] == ott.slmap[ott.days[i].hours[j].period.subject]:
                        defects += 1
    for timetable in timetables:
        defects += calculateDefect(timetable)

    # for timetable in timetables:
    #     for othertimetable in timetables:
    #         if (othertimetable != timetable):
    #             for i in range(len(timetable.hours)):
    #                 if timetable.hours[i].period.lecturer == othertimetable.hours[i].period.lecturer:
    #                     defects += 1
    # return defects


def getRandom(l: list) -> object:
    return random.choice(l)


def constructRandomTimetable(sec: Class, name: str = "DefaultTimeTable", subjectList: List[Subject] = None) -> Timetable:
    if (subjectList == None):
        subjectList = sec.lectsubj.map.keys()
    days = []
    periods = []
    for subject in subjectList:
        periods.append(Period(str(subject), subject))
    for i in range(6):
        hours = []
        for j in range(6):
            hours.append(Hour("Hour", getRandom(periods)))
        days.append(Day("Day", hours))
    #     print(
    #         f"In constructRandomTimetable: length of day {i} is {len(hours)}.")
    # print(f"In constructRandomTimetable: length of days is {len(days)}.")

    # for day in days:
    #     print(f"Length of day is {len(day.hours)}")
    t = Timetable(name, days, sec.lectsubj)
    return t


def getChildTimetable(cl: Class, a: Timetable, b: Timetable, mut: float = 0.1):
    r = constructRandomTimetable(cl, "RandomTable")
    for i in range(6):
        for j in range(6):
            c = random.random()
            if c < (1 - mut) / 2:
                r.days[i].hours[j] = a.days[i].hours[j]
            elif c < (1 - mut):
                r.days[i].hours[j] = b.days[i].hours[j]
            else:
                r.days[i].hours[j] = Hour("Hour", Period(
                    "Period", getRandom(list(r.slmap.map.keys()))))
    return r


def compareTables(ta: Timetable, tb: Timetable):
    diffs = 0
    for i in range(6):
        for j in range(6):
            sa = ta.days[i].hours[j].period.subject
            sb = tb.days[i].hours[j].period.subject
            if sa != sb:
                print(f"Difference at day {i} hour {j} : {sa}, {sb}")
                diffs += 1
    return diffs


def selectiveBreed(timetables, c: Class, n=100, sampleSize=40, mut=0.1) -> list:
    tables = []
    t = timetables
    timetables.sort(key=calculateDefect)
    for i in range(n):
        t1 = [getRandom(timetables) for h in range(sampleSize)]
        t2 = [getRandom(timetables) for h in range(sampleSize)]
        t1.sort(key=calculateDefect)
        t2.sort(key=calculateDefect)
        tables.append(getChildTimetable(c, t1[0], t2[0], mut))
    tables.sort(key=calculateDefect)
    return tables


def getTimetable(c: Class, n=100, sampleSize=40, mut=0.1):
    tables = [constructRandomTimetable(
        c, f"Timetable{i}", c.lectsubj.subjectList()) for i in range(n)]
    while calculateDefect(tables[0]) != 0:
        tables = selectiveBreed(tables, c, n, sampleSize, mut)
    return tables[0]
