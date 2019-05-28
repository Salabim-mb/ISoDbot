from fbchat import log, Client
import re

from Bot import *
from Utils import *
from Isod import *
from Ciphrator import *

class Registration:

    def fileExists(author_id):
        try:
            f = open('accounts/' + author_id, 'r')
        except:
            return False
        return True

    def fileSize(author_id):
        with open('accounts/' + author_id) as f:
            for i, l in enumerate(f):
                pass
        return i + 1

    # save to the end of the 'db file
    def save(text, author_id):
        with open('accounts/' + author_id, 'a') as f:
            f.write(text)

    # check if user is registered or in progress of registraton

    def registered(author_id):
        if(Registration.fileExists(author_id) == False): #file with this user's data doesnt exist yet, it's 1st message from this user
            return 0
        elif(Registration.fileSize(author_id) == 1): #file with this user's data has only 1 line - user already passed login
            return 1
        elif(Registration.fileSize(author_id) == 2): #file with this user's data has 2 lines - user already passed password - need to verify that data
            return 2
        else:   #none of the above, user is registered and verified
            return -1

    # registration process - if registered, use the utilities

    def registration_check(bot, thread_id, author_id, text):

        ciphrator = Ciphrator()

        if Registration.registered(author_id) == 0:
            f = open('accounts/' + author_id, "w+")
            f.close()
            Registration.save(author_id + '\n', author_id)
            Registration.ask_for_username(bot, thread_id)

        elif Registration.registered(author_id) == 1:
            text = ciphrator.encrypt(text)
            Registration.save(text + '\n', author_id)
            Registration.ask_for_password(bot, thread_id)

        elif Registration.registered(author_id) == 2:
            text = ciphrator.encrypt(text)
            Registration.save(text + '\n', author_id)
            login = Utils.getLogin(author_id)
            password = Utils.getPassword(author_id)
            if Isod.verifyData(login, password) == False:
                Utils.delete_my_data(author_id)
                bot.send(Message(text='Chyba podales zle dane logowania. Podaj login jeszcze raz'), thread_id=thread_id)
                Registration.save(author_id + '\n', author_id)
            else:
                bot.send(Message(text='Rejestracja udana'), thread_id=thread_id)
        else:
            Utils.manage_utils(bot, text, author_id, thread_id)




    def ask_for_username(bot, thread_id):
        bot.send(Message(text='Chyba jeszcze sie nie znamy. Moze sie przedstawisz? Najlepiej loginem i haslem do ISoD, podanymi kolejnych w 2 wiadomosciach :)'), thread_id=thread_id)
   
    def ask_for_password(bot, thread_id):
        bot.send(Message(text='Teraz jeszcze haslo. Nikomu nie powiem ;)'), thread_id=thread_id)


