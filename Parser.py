from Isod import *
from bs4 import *

class plan_item:
        def __init__(self, id):
            self.id = id

class Parser:
    def parseplan(text):  # przetwarza plan na taki, ktory nadaje sie do getplandaily oraz getplanweekly
        plan_string = ''  # robimy stringa ktorego zapelniamy planem
        for i in text:  # tutaj robimy tylko troche ladniej
            plan_string += i
            if i == '{' or i == '[' or i == ',':
                plan_string += "\n"
        plan_array = plan_string.split('\n')

        n = 3
        m = 0
        activities = []
        g = 0
        while not re.match(r'.*username.*', plan_array[n]):
            activity = plan_item(m)
            while not re.match(r'(.*)\}', plan_array[n]):
                lin = re.search(r'"(.*)":(.*),', plan_array[n])
                if lin:
                    typ = lin.group(1)
                    val = lin.group(2)
                    val = val[1:-1]
                    setattr(activity, typ, val)
                    n += 1
                else:
                    n += 1
            n += 1
            if (plan_array[n] == '{'):
                n += 1
            activities.append(activity)
            m += 1
        return activities

    def getplandaily(plan, day):
        activities = Parser.parseplan(plan)
        today_act = []
        for obj in activities:
            if int(obj.dayOfWeek) == day:
                today_act.append(obj)
        today_act.sort(key=lambda x: x.startTime, reverse=True)
        for obj in today_act:
            t = datetime.strptime(obj.startTime, "%I:%M:%S %p")
            obj.startTime = datetime.strftime(t, "%H:%M")
            t = datetime.strptime(obj.endTime, "%I:%M:%S %p")
            obj.endTime = datetime.strftime(t, "%H:%M")
        today_act.sort(key=lambda x: x.startTime)
        res = ""
        for obj in today_act:
            res += obj.courseName + '\n' + obj.startTime + ' - ' + obj.endTime + '\n' + obj.building + ' ' + obj.room + '\n' + 'Cykl: ' + obj.cycle + '\n\n'
        if not res:
            res = 'Wolne\n'
        return res.rstrip()

    def getplanweekly(plan):
        week = ''
        activities = Parser.parseplan(plan)
        for day in range (1, 6):
            if day == 1:
                week += 'PONIEDZIAŁEK:\n'
            if day == 2:
                week += 'WTOREK:\n'
            if day == 3:
                week += 'ŚRODA\n'
            if day == 4:
                week += 'CZWARTEK\n'
            if day == 5:
                week += 'PIĄTEK\n'
            res = ''
            res = Parser.getplandaily(plan, day)
            week += res + '\n\n'
        week = week.rstrip()
        return week

    def parsenews(text):  # przetwarza newsy na takie, ktore nadaja sie do getlastnews i getnewsno
        news_string = ''  # robimy stringa ktorego zapelniamy planem
        for index, i in enumerate(text):  # tutaj robimy tylko troche ladniej
            news_string += i
            # if index - 1 < len(text):
            if (i == '{' or i == '[' or i == ',') and (text[index+1] < 'A' or text[index+1] > 'z'):
                news_string += "\n"
        plan_array = news_string.split('\n')
        n = 3
        m = 0
        activities = []
        while not re.match(r'.*username.*', plan_array[n]):
            activity = plan_item(m)
            while not re.match(r'(.*)\}', plan_array[n]):
                lin = re.search(r'"(.*)":(.*),', plan_array[n])
                if lin:
                    typ = lin.group(1)
                    val = lin.group(2)
                    val = val[1:-1]
                    setattr(activity, typ, val)
                    n += 1
                else:
                    n += 1
            n += 1
            if (plan_array[n] == '{'):
                n += 1
            activities.append(activity)
            m += 1
        return activities

    def getlastnews(text):  # daje naglowki 5 ostatnich newsow
        news = Parser.parsenews(text)
        list = []
        for i in range(0, 5):
            list.append(news[i].subject)
        return list

    def getnewsno(text, n):  # daje naglowek numer n, zaczynajac od 0
        news = Parser.parsenews(text)
        return news[n].subject
