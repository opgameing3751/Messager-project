import socket, os, threading, time, dotenv, pygame, random
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def GUI():
    global msgcount
    starting = True
    username = True
    password = False
    loggedin = False
    logg = False
    user = ""
    pas = ""
    input3 = ''
    rebuild = False
    res = (1024, 768)
    color = (35,40,80)
    color2 = (25,30,70)
    msgcount = 1
    pygame.init()
    wn = pygame.display.set_mode((res))
    tick = pygame.time.Clock()
    font = pygame.font.Font(None,25)
    mm = font.render((''),True,(255,255,255))
    msg = ["",]
    def chat_rev():
        global msgcount
        print("chat_rev")
        while True:
            #print("waiting")
            rev = s.recv(1024).decode('utf-8')
            #print(f"... {rev}")
            if rev == "1998":
                #print(f"... {rev}")
                #s.send(rev.encode("utf-8"))
                reve = (f"{s.recv(1024).decode('utf-8')}")
                #msgfont = font.render((reve),True,(255,255,255))
                msg.append(reve)
                msgcount = msgcount + 1
               
               
            rev = 0

    



    while True:
        pygame.draw.rect(wn, (5,10,50), (0, 0, 1024, 768))
        tick.tick()
        RGBRRR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        if starting:
            pygame.draw.rect(wn, (10,15,55),(342, 200, 372, 382))
            font = pygame.font.Font(None,30)
            login_screen = font.render(("Welcome Please Login"), True ,(255,255,255))
            pygame.draw.rect(wn, color, (395, 305, 270, 30))
            pygame.draw.rect(wn, color2, (395, 355, 270, 30))
            username_box = pygame.Rect(395, 305, 270, 30)
            Password_box = pygame.Rect(395, 355, 270, 30)
            wn.blit(login_screen, (415,245))
            userinput = font.render((user),True,(255,255,255))
            passinput = font.render((pas),True,(255,255,255))
            pygame.draw.rect(wn, (25,70,30), (490,486, 80,50 ))

            loginbox = pygame.Rect(471,486, 490,520)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                    print('game quit')
                if event.type == pygame.KEYDOWN:
                    if username:
                        if event.key == pygame.K_BACKSPACE:
                            user = user[:-1]
                        elif event.key == pygame.K_RETURN:
                            password = True
                            username = False
                            color = (25,30,70)
                            color2 = (35,40,80)
                        else:
                            user += event.unicode
                    if password:
                        if event.key == pygame.K_BACKSPACE:
                            pas = pas[:-1]
                        elif event.key == pygame.K_RETURN:
                            print("not done yet")
                        else:
                            pas += event.unicode


                if event.type == pygame.MOUSEBUTTONDOWN:
                    if username_box.collidepoint(event.pos):
                        username = True
                        password = False
                        color = (35,40,80)
                        color2 = (25,30,70)
                    if Password_box.collidepoint(event.pos):
                        password = True
                        username = False
                        color = (25,30,70)
                        color2 = (35,40,80)
                    if loginbox.collidepoint(event.pos):
                        starting = False
                        logg = True

            font = pygame.font.Font(None,25)
            
            wn.blit(userinput, (405,315))
            wn.blit(passinput, (405,365))

            
        if logg:
            host = os.getenv("ip")
            port = 80
            s = socket.socket()
            s2 = socket.socket()
            s.connect((host,port))
            print('first connect secces')
            s2.connect((host,port+1))
            print("sec connection secsss")
            input1 = user
            input2 = pas
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
            print("login secces")
            logg = False
            loggedin = True
            t2 = threading.Thread(target=chat_rev)
            t2.start()
        
        if loggedin:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    s.close()
                    s2.close()
                    return
                    print('game quit')
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        input3 = input3[:-1]
                    elif event.key == pygame.K_RETURN:
                        if input3 != "":
                            s.send("chatmsg".encode("utf-8"))
                            s2.recv(1024).decode('utf-8')
                            s.send(user.encode("utf-8"))
                            s2.recv(1024).decode('utf-8')
                            s.send(input3.encode('utf-8'))
                            s2.recv(1024).decode('utf-8')
                            input3 = ""
                    else:
                        input3 += event.unicode
            
            pygame.draw.rect(wn, (25,30,70), (0, 725, 1024, 768))
            input3font = font.render((input3),True,(255,255,255))
            wn.blit(input3font, (8,738))
            range_ = 0
            timplist = []
            timpcound = 1
            if msgcount > 35:
                for i in range(msgcount):
                    if timpcound == 1:
                        timpcound = timpcound + 1
                        msgcount = msgcount - 1
                    else:
                        timplist.append(msg[i])
                        timpcound = timpcound + 1
                rebuild = True
            if rebuild:
                msg = []
                for i in range(msgcount):
                    msg.append(timplist[i]) 
                rebuild = False
            
            for i in range(msgcount):
                range_ = range_ + 1
                ycord = 20*range_
                msgfont = font.render((f"{msg[i]}"),True,(255,255,255))
                wn.blit(msgfont,(8,ycord))
            #print(msg)
        
        font = pygame.font.Font(None,20)
        fps = font.render((f"fps - {tick.get_fps()}"), True, (255,255,255))
        wn.blit(fps, (0,0))
        
        pygame.display.update()

    


t1 = threading.Thread(target=GUI)
t1.start()

