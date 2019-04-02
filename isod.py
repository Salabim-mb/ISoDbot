import requests
from bs4 import BeautifulSoup
import re
from datetime import *
import os
from pathlib import Path

class plan_item:
    def __init__(self, id):
        self.id = id

class isod:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    @classmethod
    def getAPI(cls, login, password):
        cls.login = login
        cls.password = password
        login_url = 'https://isod.ee.pw.edu.pl/isod-stud/signin/?wicket:interface=:0:signInForm::IFormSubmitListener::'  # adres do logowania na isoda

        login_values = {
            'wiaUsername': cls.login,
            'wiaPassword': cls.password
        }
        s = requests.Session()  # robimy sobie sesje zeby moc zapisywac ciacha
        l = s.post(login_url, data=login_values)  # logujemy sie na isoda
        c = s.cookies
        new_api = s.get(
            'https://isod.ee.pw.edu.pl/isod-stud/person?wicket:interface=:15:person:contApikey:generateApikey::ILinkListener::',
            cookies=c)
        soup = BeautifulSoup((s.get(
            'https://isod.ee.pw.edu.pl/isod-stud/person?wicket:interface=:15:person:contApikey:showApikey::ILinkListener::',
            cookies=c)).text, 'html.parser')
        # tutaj mamy juz ladna stronke  'dane osoby', gdzie mozna znalezc swoje api
        print('Wlazlem ci na isoda...\n')
        spans = soup.find_all(
            attrs={"class": "value"});  # szukamy po klasie 'values', bo taka klase ma span, ktory zawiera api
        api = spans[len(spans) - 1].text  # ciezko mi bylo wyodrebnic samo api, na szczescie jest ostatnim spanem na stronie, wiec z tego korzystamy
        return api

    @classmethod
    def getPlan(cls, login, password):
        url = 'https://isod.ee.pw.edu.pl/isod-portal/wapi?q=myplan&username=' + login + '&apikey=' + isod.getAPI(login, password)  # adres stronki z ktorej mozna wziac indywidualny plan za pomoca api
        p = requests.post(url)
        plan = p.text
        return plan

class plan:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.plan = plan

    @classmethod
    def format_plan(cls, login, password):
        cls.login = login
        cls.password = password
        plan = isod.getPlan(login, password)
        plan_string = ''  # robimy stringa ktorego zapelniamy planem
        for i in plan:  # tutaj robimy tylko troche ladniej
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

        day = datetime.now().weekday() + 1
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
        for obj in today_act:
            print(
                obj.courseName + '\n' + obj.startTime + ' - ' + obj.endTime + '\n' + obj.building + ' ' + obj.room + '\n')
#format_plan('login', 'haslo')

