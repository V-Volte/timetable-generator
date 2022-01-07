from classes import *
import json


def TimetableToJSON(tt: Timetable) -> str:
    s = ""
    s += '{\n"name" : "' + tt.name + '",\n"days" : [\n'
    i = 0
    for day in tt.days:
        s += DayToJSON(day)
        i += 1
        if i != len(tt.days):
            s += ",\n"
    v: dict = tt.slmap.map

    ks = [str(p) for p in v.keys()]
    vs = [str(p) for p in v.values()]

    v = dict(zip(ks, vs))

    s += '],\n"slmap" : ' + json.dumps(v) + '\n}'
    return s


def DayToJSON(dy: Day) -> str:
    s = ""
    s += '{\n"name" : "' + dy.name + '",\n"hours" : [\n'
    i = 0
    for hour in dy.hours:
        s += HourToJSON(hour)
        i += 1
        if i != len(dy.hours):
            s += ",\n"
    s += "]}"
    return s


def HourToJSON(h: Hour) -> str:
    s = ""
    s += '{\n"name" : "' + h.name + '",\n"period" : \n'
    s += PeriodToJSON(h.period)
    s += "}"
    return s


def SubjectLecturerMapToJSON(slmap):
    s = "{"
    i = 0
    for key in list(slmap.keys):
        i += 1
        s += f'"{str(key)}" : "{str(slmap.map[key])}"'
        if i == len(list(slmap.keys)):
            s += ','
        s += '\n'
    s += "}"
    return s


def PeriodToJSON(p: Period) -> str:
    s = ""
    s += '{\n"name" : "' + p.name + \
        '",\n"subject" : "' + str(p.subject) + '"\n}'
    return s


def putToJSON(s: str, fname: str):
    f = open(fname + ".json", "w")
    f.write(s)
    f.close()
