from fbchat.models import *
from fbchat import Client, log

from Registration import *
from Ciphrator import *
from Isod import *
from Parser import *

class Utils:

    #if the user exists, return his password, if not return None

    def getPassword(author_id):

        with open('accounts.txt', 'r+') as f:
            buf = f.readlines()

        iterator = iter(range(0, len(buf)))
        for i in iterator:    
            if buf[i].startswith('id: ' + author_id):
                try:
                    return Ciphrator.decypher(re.findall(r'password: (.*)', buf[i+1])[0])#re.findall(r'password: (.*)', buf[i+1])[0]#
                except:
                    return None

    #if the user exists, return his login, if not return None

    def getLogin(author_id):
        
        with open('accounts.txt', 'r+') as f:
            buf = f.readlines()

        iterator = iter(range(0, len(buf)))
        for i in iterator:    
            if buf[i].startswith('id: ' + author_id):
                try:
                    return Ciphrator.decypher(re.findall(r'login: (.*)', buf[i+2])[0])#re.findall(r'login: (.*)', buf[i+2])[0]#
                except:
                    return None

    #delete user's data from 'db' file

    def delete_my_data(author_id):
        with open("accounts.txt", "r+") as in_file:
            buf = in_file.readlines()

        with open('accounts.txt', 'w') as out:
            iterator = iter(range(0, len(buf)))
            for i in iterator:
                try:    
                    if buf[i + 1].startswith('id: ' + author_id):
                        next(iterator)
                        next(iterator)
                        next(iterator) 
                        out.write(buf[i])
                except:
                    pass

    #find keywords for deleting users data

    def wantToDeleteData(text):
        if 'Nie znasz mnie' in text or 'nie znasz mnie' in text or 'nie lubię' in text or 'Nie lubię' in text or 'Spadaj' in text or 'spadaj' in text or 'nara' in text or 'Nara' in text or 'usuń' in text or 'Usuń' in text:
            return True
        return False

    #find keywords about the plan

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
            else:
                return -1
        return False

    #find keywords about the news

    def wantToGetNews(text):
        if 'Aktualności' in text or 'aktualności' in text or 'News' in text or 'news' in text:
            return True
        return False




    #message for the case when user says something we dont know how to react to

    def messageNotRecognized(bot, thread_id):
        bot.send(Message(text='Chyba nie rozumiem. Przepraszam, ale w tej chwili umiem tylko parę zdań na temat planu zajęć i ogłoszeń. Kiepski ze mnie partner do konwersacji :('), thread_id=thread_id)


    #return todays plan

    def getTodayPlan(login, password):
        return plan.format_plan(login, password)

    #decide how to replay

    def manage_utils(bot, text, author_id, thread_id):

        login = Utils.getLogin(author_id)
        password = Utils.getPassword(author_id)
        plan = Isod.getPlan(login, password)
        news = Isod.getNews(login, password)

        #user data deletion

        if Utils.wantToDeleteData(text):
            Utils.delete_my_data(author_id)
            bot.send(Message(text='Kim Ty jesteś?'), thread_id=thread_id)

        #plan section

        elif Utils.wantToGetPlan(text) == 1:
            bot.send(Message(text=Parser.getplandaily(plan, 1)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 2:
            bot.send(Message(text=Parser.getplandaily(plan, 2)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 3:
            bot.send(Message(text=Parser.getplandaily(plan, 3)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 4:
            bot.send(Message(text=Parser.getplandaily(plan, 4)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 5:
            bot.send(Message(text=Parser.getplandaily(plan, 5)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 6:
            bot.send(Message(text='W weekend nie masz zajęć :)'), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == 7:
            bot.send(Message(text=Parser.getplanweekly(plan)), thread_id=thread_id)
        elif Utils.wantToGetPlan(text) == -1:
            bot.send(Message(text='Może to ja niedomagam, ale nie wiem na kiedy chcesz ten plan. Wyrażaj się jaśniej proszę'), thread_id=thread_id)

        #News section

       
        elif Utils.wantToGetNews(text) == True:
            bot.send(Message(text=Parser.getlastnews(news)[0]), thread_id=thread_id)
            bot.send(Message(text=Parser.getlastnews(news)[1]), thread_id=thread_id)
            bot.send(Message(text=Parser.getlastnews(news)[2]), thread_id=thread_id)
            bot.send(Message(text=Parser.getlastnews(news)[3]), thread_id=thread_id)
            bot.send(Message(text=Parser.getlastnews(news)[4]), thread_id=thread_id)

        else:
            Utils.messageNotRecognized(bot, thread_id)

