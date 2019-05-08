# -*- coding: utf-8 -*-
#creator: laps3(@answermebitch)

import telepot
import os
import re
from classbot import coke

os.system('clear')

token = ''
bot = telepot.Bot(token)

def handle(msg):
    uid = msg['from']['id']
    firstname = msg['from']['first_name']
    chat_id = msg['chat']['id']
    chat_type = msg['chat']['type']
    msgid = msg['message_id']
    user_message = msg.get('text')
    try:
        user = '@' + msg['from']['username']
    except:
        user = firstname
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'document':
        pdfile = open('pdfile.txt', 'a')
        pdfile_read = open('pdfile.txt', 'r')
        pdfile_readed = pdfile_read.read()
        if msg['document']['mime_type'] == 'application/pdf':
            if msg['document']['file_name'] in pdfile_readed:
                bot.sendMessage(chat_id, 'Exists.', reply_to_message_id=msgid)
            else:
                bot.sendMessage(chat_id, 'Uploading....', reply_to_message_id=msgid)
                pdfile.write(msg['document']['file_name'])
                bot.sendMessage('@yourchannel', 'File name: ' + msg['document']['file_name'])
                bot.sendDocument('@yourchannel', msg['document']['file_id'])
                print 'Document sended!'
    elif msg.get('new_chat_member'):
        bot.sendMessage(chat_id, 'Bem-vindo!', reply_to_message_id=msgid)
        print 'new user'
    elif msg.get('text'):
        coke_object = coke(bot, chat_id, msg)
        texto = msg['text'].split()[0]
        coke_object.check_command(texto)

bot.message_loop(handle)
print '*ONLINE BITCH!'
while 1:
    pass
