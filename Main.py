from threading import Thread
import telepot, socket, time, string


bot = telepot.Bot('YOUR TOKEN')

HOST = "irc.nlog.net"
PORT = 6667
NICK = "snigebagent"
readbuffer = ""
Ident = "snigebagent!~Mayer@ghosts"
GECOS = "Bot Master"
Channel = "#BotnTest telegram"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
s.send(bytes("/JOIN #BotnTest telegram\r\n", "UTF-8"));




while 1:

	readbuffer = s.recv(1024)
	print(readbuffer)


def check_command(txt):
	
	txt = txt.split(' ')

	if txt[0][0] != '/':
		return		
	elif txt[0] == '/ping':
		time.sleep(3)
		targ_ip = txt[1]
		ping(targ_ip)
		return str('Resposta de ' + str(uid) + ' \n' + '~> Pingando ' + txt[1] + '...')

	elif txt[0] == '/list':
		time.sleep(2)
		return str(uid + '\nAguardando ordens!')
	else:
		pass




def handler(msg):
	
	text = msg['text']
	Message = check_command(text)
	groupID = msg['chat']['id']
	try:
		bot.sendMessage(groupID, Message)
	except:
		time.sleep(2)
		pass


def receive():

    bot.message_loop(handler)


t_receive = Thread(target=receive())
t_receive.start()


while True:

    pass
