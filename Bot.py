from fbchat.models import *
from fbchat import Client, log

from Registration import *

class Bot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):

        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        if(author_id != self.uid):
            Registration.registration_check(self, thread_id, author_id, message_object.text)

