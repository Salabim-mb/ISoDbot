from fbchat.models import *
from fbchat import Client, log

from Registration import *
from iisod import *

class Utils:

    def getPassword(author_id):

        with open('accounts.txt', 'r+') as f:
            buf = f.readlines()

        iterator = iter(range(0, len(buf)))
        for i in iterator:    
            if buf[i].startswith('id: ' + author_id):
                try:
                    return re.findall(r'password: (.*)', buf[i+1])
                except:
                    return None


    def getLogin(author_id):
        
        with open('accounts.txt', 'r+') as f:
            buf = f.readlines()

        iterator = iter(range(0, len(buf)))
        for i in iterator:    
            if buf[i].startswith('id: ' + author_id):
                try:
                    return re.findall(r'login: (.*)', buf[i+2])
                except:
                    return None

    #delete user's data from 'db' file

    def delete_my_data(bot, author_id, thread_id):
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
                        print(buf[i])
                        out.write(buf[i])
                except:
                    pass


        bot.send(Message(text='Kim Ty jesteś?'), thread_id=thread_id)



    def user_recognized(bot, thread_id):
        bot.send(Message(text='[JUZ SIE ZNAMY]'), thread_id=thread_id)

    def getTodayPlan(login, password):
        return plan.format_plan(login, password)



    def manage_utils(bot, text, author_id, thread_id):
        if text == 'Nie znasz mnie':
            Utils.delete_my_data(bot, author_id, thread_id)
            bot.send(Message(text='Kim Ty jesteś?'), thread_id=thread_id)
        elif text == 'Plan na dzisiaj':
            login = Utils.getLogin(author_id)[0]
            password = Utils.getPassword(author_id)[0]
            message = Utils.getTodayPlan(login, password)
            bot.send(Message(text=message), thread_id=thread_id)
        else:
            Utils.user_recognized(bot, thread_id)

