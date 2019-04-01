from fbchat import log, Client
import re

from Bot import *
from Utils import *
from Isod import *

class Registration:

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

    #save to the end of the 'db file

    def save(text):
        with open("accounts.txt", "a") as f:
            f.write(text)

    #save to the 'db' file in sorted form (id \n pass \n login)

    def save_after(text, author_id):
        with open("accounts.txt", "r+") as in_file:
            buf = in_file.readlines()

        with open("accounts.txt", "w") as out_file:
            for line in buf:
                if line.startswith('id: ' + author_id):
                    line = line + text
                out_file.write(line)

    #check if user is registred or in progress of registraton

    def registered(author_id):
        f = open("accounts.txt", "r+")
        for line in f:
            if line.startswith('id: ' + author_id):
                try:
                    if next(f).startswith('login:'):
                        return 2
                    else:
                        return 3
                except StopIteration:
                    return 1
                

        f.close()
        return 0
        

    #registration process - if registered, use the utilities
         

    def registration_check(bot, thread_id, author_id, text):

        if Registration.registered(author_id) == 0:

            Registration.save('id: ' + author_id + '\n')
            Registration.ask_for_username(bot, thread_id)

        elif Registration.registered(author_id) == 1:

            Registration.save_after('login: ' + text + '\n', author_id)
            Registration.ask_for_password(bot, thread_id)

        elif Registration.registered(author_id) == 2:
            Registration.save_after('password: ' + text + '\n', author_id)
            login = Registration.getLogin(author_id)
            password = Registration.getPassword(author_id)
            if Isod.verifyData(login, password) == False:
                Utils.delete_my_data(bot, author_id, thread_id)
                bot.send(Message(text='Chyba podałeś/aś złe dane logowania. Podaj login jeszcze raz'), thread_id=thread_id)
                Registration.save('id: ' + author_id + '\n')
        else:
            Utils.user_recognized(bot, thread_id)
            Utils.manage_utils(bot, text, author_id, thread_id)




    def ask_for_username(bot, thread_id):
        bot.send(Message(text='Chyba jeszcze się nie znamy. Może się przedstawisz? Najlepiej loginem i hasłem do ISoD, podanymi kolejnych w 2 wiadomościach :)'), thread_id=thread_id)
   
    def ask_for_password(bot, thread_id):
        bot.send(Message(text='Teraz jeszcze hasło. Nikomu nie powiem ;)'), thread_id=thread_id)

    def registration_complete(bot, thread_id):
        bot.send(Message(text='[TUTAJ BEDZIE PROBA ZALOGOWANIA DO ISODA ZEBY SPRAWDZIC CZY DOBRE PASY]'), thread_id=thread_id)




