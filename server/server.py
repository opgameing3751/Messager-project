import socket, os, threading, dotenv, time
from dotenv import load_dotenv, find_dotenv
from codecs import ignore_errors

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def megsend(User, msg):
    
    for i in range(num):
        c_list[i].send(f"{User}: {msg}".encode("utf-8"))

def on_new_client(c,addr,c2,addr2):
    print(addr)
    while True:
        try:
            Clientrev = 0
            Clientrev = c.recv(1024).decode('utf-8')
            if Clientrev == "register":
                c.send('awaiting'.encode('utf-8'))
                username = c.recv(1024).decode('utf-8')
                print(username)
                c.send(username.encode('utf-8'))
                password = c.recv(1024).decode('utf-8')
                print(password)
                c.send(password.encode('utf-8'))
                os.environ[f'{username}'] = password
                dotenv.set_key(dotenv_file, f"{username}", os.environ[f"{username}"])
                #password = os.getenv("username")
                print("done")
                
            if Clientrev == "loggin":
                c.send("loggin".encode('utf-8')) 
                account_password = os.environ[f"{c.recv(1024).decode('utf-8')}"] #gets the username and starts waiting for password
                print(account_password)
                c.send("waiting for password".encode('utf-8'))
                password = c.recv(1024).decode('utf-8')
                c.send("password".encode('utf-8'))
                print(password)
                if account_password == password:
                    c.send("passed".encode("utf-8"))
                    print('passed')
                else:
                    print('denied')
                    c.send("denied".encode('utf-8'))
                print('done')
                #while True:
            if Clientrev == "chatmsg":
                c2.send("waiting for msg".encode("utf-8"))
                User = c.recv(1024).decode('utf-8')
                c2.send(User.encode("utf-8"))
                msg = c.recv(1024).decode('utf-8')
                c2.send(msg.encode("utf-8"))
                
                #print(f"{User}: {msg}")
                #c.send("1998".encode("utf-8"))
                #print(c)
                #time.sleep(1)
                print(f"{User}: {msg}")
                print(f"first - {num}")
                for i in range(num):
                    print(num)
                    c_list[i].send("1998".encode("utf-8"))
                    #print(f"{c_list[i].recv(1024).decode('utf-8')}")
                    time.sleep(.01)
                    c_list[i].send(f"{User}: {msg}".encode("utf-8"))
                    #print(f"{c_list[i].recv(1024).decode('utf-8')}")
                    time.sleep(.01)
                    
                #megsend(User, msg)
        except:
            ignore_errors

host = os.getenv("ip")
port = 80
port2 = 81
s = socket.socket()
s2 = socket.socket()
s.bind((host,port))
s2.bind((host,port2))
s.listen(5)
s2.listen(5)


c_list = []
c2_list = []
addr_list = []
num = 0
sending_list =[]
while True:
    c, addr = s.accept()
    time.sleep(1)
    c2, addr2 = s2.accept()
    c_list.append(c)
    c2_list.append(c2)

    num = num + 1
    #print(f"sending - {sending}")
    #print(f"sending list - {sending_list}")
    #print(num)
    #print(f"just c {c}")
    addr_list.append(addr)
    #print("Connection from: "+str(addr))
    thread = threading.Thread(target=on_new_client, args=(c,addr,c2,addr2))
    #thread.daemon = True
    thread.start()

s.close()

