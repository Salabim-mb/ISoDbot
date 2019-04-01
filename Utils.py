from fbchat.models import *
from fbchat import Client, log

from Bot import *

class Utils:

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



    def manage_utils(bot, text, author_id, thread_id):
        if text == 'Nie znasz mnie':
            Utils.delete_my_data(bot, author_id, thread_id)
            bot.send(Message(text='Kim Ty jesteś?'), thread_id=thread_id)
        else:
            Utils.user_recognized(bot, thread_id)
