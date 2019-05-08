import telepot

class coke:
    def __init__(self, bot, chat_id, msg):
        self.bot = bot
        self.chat_id = chat_id
        self.msg = msg

    def check_command(self, msg):
        log = open('log_commands.txt', 'a')
        links = open('links.txt', 'a')
        adm_id = []

        try:
            user = '@' + self.msg['from']['username']
        except:
            user = self.msg['from']['first_name']

        if msg == '/start@coke':
            self.bot.sendMessage(self.chat_id, 'Hello sir.', reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /start@coke'
        elif msg == '/test@coke':
            self.bot.sendMessage(self.chat_id, 'Say.', reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /test@coke'
        elif msg == '/unpin@coke':
            self.bot.unpinChatMessage(self.chat_id)
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /unpin@coke'
        elif msg == '/fix@coke':
            self.bot.pinChatMessage(self.chat_id, self.msg['reply_to_message']['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /fix@coke'
        elif msg == '/ban@coke':
            try:
                usern = '@' + self.msg['reply_to_message']['from']['username']
            except:
                usern = self.msg['reply_to_message']['from']['first_name']
            self.bot.kickChatMember(self.chat_id, self.msg['reply_to_message']['from']['id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /ban@coke'
            print str(user.encode('utf-8')) + ' has banned ' + str(usern.encode('utf-8'))
        elif msg == '/rt':
            try:
                reply_user = '@' + self.msg['reply_to_message']['from']['username']
            except:
                reply_user = self.msg['reply_to_message']['from']['first_name']
            self.bot.sendMessage(self.chat_id, user + ' concorda com ' + reply_user, reply_to_message_id=self.msg['message_id'])
        elif msg == '/help@coke':
            self.bot.sendMessage(self.chat_id, '[+]User commands[+]\n/myid@drugsoverdose_bot\n/id@coke\n/onionlink@coke\n/test@coke\n[+]Admin commands[+]\n/ban@coke\n/fix@coke\n/unpin@coke\n/addlink@coke\n/unban@coke\n/promote@coke', reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /help@coke'
        elif msg == '/src@coke':
            self.bot.sendMessage(self.chat_id, 'https://github.com/laps3l/CokeBot', reply_to_message_id=self.msg['message_id'])
        elif msg == '/pin@coke':
            if self.msg['from']['id'] == 749087933:
                self.bot.forwardMessage('@bypassedltda', self.chat_id, self.msg['reply_to_message']['message_id'])
                self.bot.sendMessage(self.chat_id, 'Ok sir.', reply_to_message_id=self.msg['message_id'])
                log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
                print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /forward@coke'
            else:
                self.bot.sendMessage(self.chat_id, 'Fuck you bitch!', reply_to_message_id=self.msg['message_id'])
        elif msg == '/banid@coke':
            fw = self.msg.get('text').split()
            self.bot.kickChatMember(self.chat_id, fw[1])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /banid@coke'
            print str(user.encode('utf-8')) + ' has banned ' + str(usern.encode('utf-8'))
        elif self.msg.get('text').startswith('/addlink@coke'):
            if self.msg['from']['id'] in adm_id:
                damn = self.msg.get('text').split()
                damn2 = damn[1]
                links_reading = open('links.txt', 'r')
                links_read = links_reading.read()
                if '.onion' in damn2:
                    if damn2.encode('utf-8') in links_read:
                        self.bot.sendMessage(self.chat_id, 'Exists.', reply_to_message_id=self.msg['message_id'])
                    else:
                        fuck = links.write(damn[1])
                        fuckk = links.write(str('  | ' + ' '.join(damn[2:]).encode('utf-8') + ' |\n'))
                        self.bot.sendMessage(self.chat_id, 'Ok sir.', reply_to_message_id=self.msg['message_id'])
                        log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
                        print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /addlink@coke'
                else:
                    self.bot.sendMessage(self.chat_id, 'Fuck you bitch!', reply_to_message_id=self.msg['message_id'])
            else:
                self.bot.sendMessage(self.chat_id, 'Fuck you bitch!', reply_to_message_id=self.msg['message_id'])
        elif msg == '/id@coke':
            self.bot.sendMessage(self.chat_id, self.msg['reply_to_message']['from']['id'], reply_to_message_id=self.msg['message_id'])
        elif msg == '/onionlink@coke':
            opn = open('links.txt', 'r')
            opn_read = opn.read()
            self.bot.sendMessage(self.chat_id, opn_read, reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /onionlink@coke'aki&w=600', reply_to_message_id=self.msg['message_id'])
        elif msg == '/myid@drugsoverdose_bot':
            self.bot.sendMessage(self.chat_id, self.msg['from']['id'], reply_to_message_id=self.msg['message_id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' + str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /myid@coke'
        elif msg == '/unban@coke':
            try:
                fodeu = '@' + self.msg['reply_to_message']['from']['username']
            except:
                fodeu = self.msg['reply_to_message']['from']['first_name']
            self.bot.unbanChatMember(self.chat_id, self.msg['reply_to_message']['from']['id'])
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /unban@coke'
            print str(user.encode('utf-8')) + ' has unbanned ' + str(fodeu.encode('utf-8'))
        elif msg == '/promote@coke':
            try:
                promoted = '@' + self.msg['reply_to_message']['from']['username']
            except:
                promoted = self.msg['reply_to_message']['from']['first_name']
            self.bot.promoteChatMember(self.chat_id, self.msg['reply_to_message']['from']['id'], can_change_info=True, can_post_messages=False, can_edit_messages=False, can_delete_messages=True, can_invite_users=True, can_restrict_members=True, can_pin_messages=True, can_promote_members=True)
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /promote@coke'
            print str(user.encode('utf-8')) + ' has promoted ' + str(promoted.encode('utf-8'))
        elif self.msg.get('text').startswith('/title@coke'):
            mensagem = self.msg.get('text').split()
            mensagem2 = mensagem[1:]
            self.bot.setChatTitle(self.chat_id, ' '.join(mensagem2).encode('utf-8'))
            log.write('Name: ' + str(self.msg['from']['first_name'].encode('utf-8')) + ' |Chat: ' + str(self.msg['chat']['id']) + '|User: ' + str(user.encode('utf-8')) + ' |Text: ' +str(self.msg.get('text').encode('utf-8')) + '\n')
            print 'Name: ' + str(self.msg['from']['first_name']) + ' |Chat: ' + str(self.msg['chat']['id']) + ' |User: ' + str(user) + ' - /title@coke'
            print str(user.encode('utf-8')) + ' has changed the name of ' + str(self.chat_id)
