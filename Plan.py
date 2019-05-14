import Isod as Isod, re
from datetime import *

'''
Obiekt Plan tworzymy deklarując go za pomocą loginu oraz hasła danego użytkownika, np:
plan = Plan('login', 'hasło')

Plan na dany dzień uzyskujemy z metody Plan.get_plan_daily(day), np:
plan_na_poniedziałek = plan.get_plan_daily(1) < wynik w formacie string

Plan na cały tydzień dostajemy metodą Plan.get_plan_weekly(), np:
plan_na_tydzień = plan.get_plan_weekly() < wynik w postaci listy string, jeden element listy to nazwa dnia
oraz plan na ten dzień

Najbliższe nierozpoczęte zajęcia(mierzone od chwili uruchomienia skryptu) otrzymujemy metodą Plan.get_next_class(), np:
następne_zajęcia = plan.get_next_class() < wynik w formacie string
'''
class Plan:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.plan_string = Isod.getPlan(self.login, self.password)
        self.classes = []
        self.parse_plan(self.plan_string)

    class PlanItem:

        def __init__(self, id):
            self.id = id
            self.time = 0

        def get_class_info(self):
            res = self.courseName + '\n' + self.startTime + ' - ' + self.endTime + '\n' + self.building + ' ' + self.room + '\n' + 'Cykl: ' + self.cycle
            return res

        def start_time(self):
            return int(self.startTime[:2]+self.startTime[-2:])

        def set_time(self):
            self.time = int(str(self.dayOfWeek) + self.startTime[:2] + self.startTime[-2:])

    class Day:
        def __init__(self, day_number, classes):
            self.day_number = day_number
            self.classes = classes
            self.day_classes = []
            for obj in self.classes:
                if int(obj.dayOfWeek) == self.day_number:
                    self.day_classes.append(obj)
            self.day_classes.sort(key=lambda x: x.startTime)
            if day_number == 1:
                self.day_name = 'PONIEDZIAŁEK'
            if day_number == 2:
                self.day_name = 'WTOREK'
            if day_number == 3:
                self.day_name = 'ŚRODA'
            if day_number == 4:
                self.day_name = 'CZWARTEK'
            if day_number == 5:
                self.day_name = 'PIĄTEK'

        def get_classes(self):
            day_name = self.day_name + '\n\n'
            res = ''
            for obj in self.day_classes:
                res += obj.get_class_info()+'\n\n'
            if not res.rstrip():
                return day_name + 'WOLNE'
            return day_name + res.rstrip()

        def get_last_class(self):
            if not self.day_classes:
                return 0
            else:
                return self.day_classes[len(self.day_classes) - 1]

        def get_first_class(self):
            if not self.day_classes:
                return 0
            else:
                return self.day_classes[0]

    def parse_plan(self, text):
        plan_string = ''
        for i in text:
            plan_string += i
            if i == '{' or i == '[' or i == ',':
                plan_string += "\n"
        plan_array = plan_string.split('\n')

        n = 3
        m = 0
        activities = []
        while not re.match(r'.*username.*', plan_array[n]):
            activity = self.PlanItem(m)
            while not re.match(r'(.*)\}', plan_array[n]):
                lin = re.search(r'"(.*)":(.*),', plan_array[n])
                if lin:
                    typ = lin.group(1)
                    val = lin.group(2)
                    val = val[1:-1]
                    if typ == 'startTime' or typ == 'endTime':
                        t = datetime.strptime(val, "%I:%M:%S %p")
                        val = datetime.strftime(t, "%H:%M")
                    setattr(activity, typ, val)
                    n += 1
                else:
                    n += 1
            n += 1
            if plan_array[n] == '{':
                n += 1
            activities.append(activity)
            m += 1
        for obj in activities:
            self.classes.append(obj)

    def is_day_over(self):
        now = datetime.now()
        today_plan = self.Day(now.weekday() + 1, self.classes)
        if not today_plan.get_first_class():
            return True
        else:
            last_class = today_plan.get_last_class()
            last_start_hour = last_class.start_hour()
            if int(now.hour) < last_start_hour or (int(now.hour) == last_start_hour and int(now.minute) < 16):
                return False
            else:
                return True

    def get_class_list(self):
        res = []
        b = 1
        for i in range(1, 6):
            today = self.Day(i, self.classes)
            for obj in today.classes:
                obj.set_time()
                res.append(obj)
            b += 1
        res.sort(key=lambda x: x.time)
        return res

    def get_next_class(self):
        t = datetime.now()
        day = t.weekday() + 1
        if t.hour < 10:
            now_time = int(str(day) + '0' + str(t.hour) + str(t.minute))
        else:
            now_time = int(str(day) + str(t.hour) + str(t.minute))
        classes = self.get_class_list()
        for i, obj in enumerate(classes):
            if i == len(classes) - 1:
                return classes[0]
            if now_time >= obj.time and now_time < classes[i+1].time:
                return classes[i+1]

    def get_plan_daily(self, day):
        day = self.Day(day, self.classes)
        return day.get_classes()

    def get_plan_weekly(self):
        res = []
        for i in range(1, 6):
            day = self.Day(i, self.classes)
            res.append(day.get_classes())
        return res

