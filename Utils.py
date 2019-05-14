from fbchat.models import *
from fbchat import Client, log
import os

from Registration import *
from Ciphrator import *
from Plan import *
from News import *
import random


class Utils:
    #if the user exists, return his password, if not return None

    @staticmethod
    def getPassword(author_id):
        ciphrator = Ciphrator()
        f = open('accounts/' + author_id)
        lines = f.readlines()
        return (ciphrator.decrypt(lines[2]))

    #if the user exists, return his login, if not return None

    @staticmethod
    def getLogin(author_id):
        ciphrator = Ciphrator()
        f = open('accounts/' + author_id)
        lines = f.readlines()
        return ciphrator.decrypt(lines[1])

    #delete user's data from 'db' file
    @staticmethod
    def delete_my_data(author_id):
        os.remove('accounts/' + author_id)

    #find keywords for deleting users data
    @staticmethod
    def wantToDeleteData(text):
        if 'Nie znasz mnie' in text or 'nie znasz mnie' in text or 'nie lubię' in text or 'Nie lubię' in text or 'Spadaj' in text or 'spadaj' in text or 'nara' in text or 'Nara' in text or 'usuń' in text or 'Usuń' in text:
            return True
        return False

    # find keyword about fun facts
    def wantToHearFunFact(text):
        if 'ciekawostka' in text or 'żart' in text or 'żarcik' in text or 'lol' in text or 'xD' in text or 'XD' in text:
            return True
        return False

    #find keywords about the plan
    @staticmethod
    def wantToGetPlan(text):
        if 'plan' in text or 'zajęcia' in text or 'Plan' in text or 'Zajęcia' in text:
            if 'dziś' in text or 'dzisiaj' in text or 'Dziś' in text or 'Dzisiaj' in text:
                return datetime.now().weekday() + 1
            elif 'jutro' in text or 'Jutro' in text:
                return datetime.now().weekday() + 2
            elif 'poniedziałek' in text or 'Poniedziałek' in text:
                return 1
            elif 'wtorek' in text or 'Wtorek' in text:
                return 2
            elif 'środa' in text or 'Środa' in text or 'środę' in text or 'Środę' in text:
                return 3
            elif 'czwartek' in text or 'Czwartek' in text:
                return 4
            elif 'piątek' in text or 'Piątek' in text:
                return 5
            elif 'sobota' in text or 'Sobota' in text or 'Niedziela' in text or 'niedziela' in text or 'sobotę' in text or 'Sobotę' in text or 'Niedzielę' in text or 'niedzielę' in text:
                return 6
            elif 'cały' in text or 'Cały' in text or 'tydzień' in text or 'Tydzień' in text:
                return 7
            elif 'następne' in text or 'Następne' in text or 'najbliższe' in text or 'Najbliższe' in text or 'zaraz' in text or 'teraz' in text or 'Zaraz' in text or 'Teraz' in text:
                return 8
            else:
                return -1
        return False

    #find keywords about the news
    @staticmethod
    def wantToGetNews(text):
        if 'Aktualności' in text or 'aktualności' in text or 'News' in text or 'news' in text:
            return True
        return False




    #message for the case when user says something we dont know how to react to
    @staticmethod
    def messageNotRecognized(bot, thread_id):
        bot.send(Message(text='Chyba nie rozumiem. Przepraszam, ale w tej chwili umiem tylko parę zdań na temat planu zajęć i ogłoszeń. Kiepski ze mnie partner do konwersacji :('), thread_id=thread_id)



    #return todays plan
    #@staticmethod
    #def getTodayPlan(login, password):
    #    return plan.format_plan(login, password)

    #decide how to replay
    @staticmethod
    def manage_utils(bot, text, author_id, thread_id):

        login = Utils.getLogin(author_id)
        password = Utils.getPassword(author_id)
        plan = Plan(login, password)
        news = News(login, password)

        #user data deletion

        if Utils.wantToDeleteData(text):
            Utils.delete_my_data(author_id)
            bot.send(Message(text='Kim Ty jesteś?'), thread_id=thread_id)

        # fun facts
        elif Utils.wantToHearFunFact(text):
            x = random.randint(0, 10)
            if x is 0:
                bot.send(Message(text='Jakie papierosy palą studenci EE?'), thread_id=thread_id)
                bot.send(Message(text='Elektryczne!'), thread_id=thread_id)
            elif x is 1:
                bot.send(Message(text='Na lekcji programowania obiektowego student łapie koleżankę obok za pierś. Na to ona: „To prywatne!!!”, a on odpowiada: „Myślałem że jesteśmy w tej samej klasie :D „'), thread_id=thread_id)
            elif x is 2:
                bot.send(Message(text='Javoviec jakimś cudem spłodził dziecko. Miał wymyślić imię dla dziecka. Na wszelki wypadek przygotował 2, jakby urodziły się bliźniaki. Na nieszczęście urodziły się trojaczki i dostały imiona: Jaś, Staś, ArrayIndexOutOfBoundsException'), thread_id=thread_id)
            elif x is 3:
                bot.send(Message(text='Spotyka się dwóch programistów:\n– Słyszałem, że straciłeś pracę. Jak to jest być bezrobotnym?\n– To było najgorsze pół godziny mojego życia!'), thread_id=thread_id)
            elif x is 4:
                bot.send(Message(text='Doktorze, każdej nocy śni mi się jeden i ten sam koszmar. Jestem na Antarktydzie a wokół pełno pingwinów. I ciągle przybywają i przybywają. Zbliżają się do mnie, napierają na mnie, przepychają mnie do urwiska i za każdym razem spychają mnie do lodowatej wody.\n– Normalnie leczymy takie przypadki w jeden dzień. Ale z Panem możemy mieć większe problemy, Panie Gates…'), thread_id=thread_id)
            elif x is 5:
                bot.send(Message(text='Jadą samochodem 3 koledzy i jeden z nich był programistą. Samochód się psuje, pasażerowie siedzą w środku i dywagują: świece, rozrusznik, benzyna, skończył sie olej… Nagle programista mówi: a może wyjdźmy z samochodu poczekajmy chwilę i potem wejdźmy :D'), thread_id=thread_id)
            elif x is 6:
                bot.send(Message(text='Z programowaniem jak z budową katedry, budujesz,budujesz a potem się modlisz (żeby wszystko działało)'), thread_id=thread_id)
            elif x is 7:
                bot.send(Message(text='Programista otwiera lodówkę, sięga po masło i patrząc na napis „82%” mówi:\n– a to jeszcze chwilka i będzie gotowe.'), thread_id=thread_id)
            elif x is 8:
                bot.send(Message(text='Na świecie jest 10 rodzajów ludzi: ci, którzy rozumieją system binarny i ci, którzy go nie rozumieją.'), thread_id=thread_id)
            elif x is 9:
                bot.send(Message(text='Żona do programisty: idź do sklepu kup 5 bułek, a jak będą jajka kup 10.\nProgramista będąc w sklepie: – Są jajka?\nSprzedawczyni: – Tak, są.\nProgramista: To poproszę 10 bułek.'), thread_id=thread_id)
            elif x is 10:
                bot.send(Message(text='Dlaczego programiści mylą Boże Narodzenie z Halloween ?\nBo 25 Dec = 31 Oct'), thread_id=thread_id)
            else:
                return -1

        #plan section

        elif Utils.wantToGetPlan(text) == 1:
            bot.send(Message(text=plan.get_plan_daily(1)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 2:
            bot.send(Message(text=plan.get_plan_daily(2)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 3:
            bot.send(Message(text=plan.get_plan_daily(3)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 4:
            bot.send(Message(text=plan.get_plan_daily(4)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 5:
            bot.send(Message(text=plan.get_plan_daily(5)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 6:
            bot.send(Message(text='W weekend nie masz zajęć :)'), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 7:
            weekplan = plan.get_plan_weekly()
            for i in weekplan:
                bot.send(Message(text=i), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 8:
            bot.send(Message(text=plan.get_next_class()), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == -1:
            bot.send(Message(text='Może to ja niedomagam, ale nie wiem na kiedy chcesz ten plan. Wyrażaj się jaśniej proszę'), thread_id=thread_id)

        #News section

       
        elif Utils.wantToGetNews(text) == True:
            news_list = news.getlastnews()
            for obj in news_list:
                bot.send(Message(text=obj), thread_id=thread_id)

        else:
            Utils.messageNotRecognized(bot, thread_id)
