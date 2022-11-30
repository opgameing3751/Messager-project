import socket, os, threading, time, dotenv
from codecs import ignore_errors
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

host = os.getenv("ip")
port = 80
s = socket.socket()
s2 = socket.socket()
s.connect((host,port))
print('first connect secces')
s2.connect((host,port+1))
print("sec connection secsss")


print("Hello!!")
time.sleep(1)
print("are you logging in, or making an account")
input1 = input()

def chat_sending():
    print("chat_send")
    while True:
        msg = input("")
        s.send("chatmsg".encode("utf-8"))
        #print("yes")
        s2.recv(1024).decode('utf-8')
        #print('recv1')
        s.send(Username.encode("utf-8"))
        s2.recv(1024).decode('utf-8')
        #print('recv2')
        s.send(msg.encode('utf-8'))
        s2.recv(1024).decode('utf-8')
        #print('recv3')
def chat_rev():
    #print("chat_rev")
    while True:
        #print("waiting")
        rev = s.recv(1024).decode('utf-8')
        #print(f"... {rev}")
        if rev == "1998":
            #print(f"... {rev}")
            #s.send(rev.encode("utf-8"))
            print(f"{s.recv(1024).decode('utf-8')}")
            #s.send("done".encode("utf-8"))
        rev = 0

if input1 == "making an account":
    input1 = input("Username - ")
    input2 = input("Password - ")
    s.send("register".encode('utf-8'))
    s.recv(1024).decode('utf-8')
    #print('recv1')
    s.send(input1.encode('utf-8'))
    s.recv(1024).decode('utf-8')
    #print('recv2')
    s.send(input2.encode('utf-8'))
    s.recv(1024).decode('utf-8')
    #print('recv3')
    s.close()
if input1 == "logging in" or "Logging in" or "l" or "L":
    input1 = input("Username - ")
    input2 = input("Password - ")
    s.send("loggin".encode('utf-8'))
    #print("sent loggin noti to server")
    s.recv(1024).decode("utf")
    #s.recv(1024).decode('utf-8')
    s.send(input1.encode("utf-8"))
    #print("sent username")
    s.recv(1024).decode("utf")
    #s.recv(1024).decode('utf-8')
    s.send(input2.encode("utf-8"))
    s.recv(1024).decode("utf")
    print("sent password")
    if s.recv(1024).decode("utf-8") == "denied":
        print("incorrect login")
        time.sleep(3)
        s.close()
    Username = input1
    t1 = threading.Thread(target=chat_rev)
    t2 = threading.Thread(target=chat_sending)
    t1.start()
    t2.start()
while True:
    time.sleep(1)
