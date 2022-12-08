import socket, os, threading, time, dotenv, pygame, random, sys
import moviepy.editor
import cv2
from codecs import ignore_errors
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

def GUI():
    global msgcount
    Version = "0.3"
    VersionDate = "12/8/2022"
    program = True
    starting = False
    username = True
    password = False
    loggedin = False
    splash_screen = True
    logg = False
    user = "Adam"
    pas = "Adam123"
    input3 = 'hello'
    rebuild = False
    res = (1024, 768)
    color = (35,40,80)
    color2 = (25,30,70)
    reg = False
    msg = []
    s = ''
    s2 = ''
    settingsgui = False
    settingsicon_ = pygame.image.load("imgs\settings.png")
    settingsicon = pygame.transform.scale(settingsicon_, (24,24))
    msgcount = int(os.getenv("msgnum"))
    BackButtonimg_ = pygame.image.load("imgs\BackButton.png")
    BackButtonimg = pygame.transform.scale(BackButtonimg_, (48,25))
    timpcount =1
    for i in range(msgcount):
        msg.append(os.getenv(f"{timpcount}"))
        timpcount = timpcount + 1
    pygame.init()
    wn = pygame.display.set_mode((res))
    tick = pygame.time.Clock()
    font = pygame.font.Font(None,25)
    mm = font.render((''),True,(255,255,255))
    rangecount = 1
    
    for i in range(rangecount):
        try:
            msg_ = os.getenv("msg")
            #print(msg_)
            if msg_ != "None":
                msg.append(msg_)
            else:
                msg_ = ""
                msg.append(msg_)
        except:
            msg_ = ""
            msg.append(msg_)
        rangecount = rangecount + 1
    rangecount = 1

    def reconnect():
        #global s, s2
        try:
            host = os.getenv("ip")
            port = 80
            s = socket.socket()
            s2 = socket.socket()
            s.connect((host,port))
            print('first connect secces')
            s2.connect((host,port+1))
            print("sec connection secsss")
            s.send("loggin".encode('utf-8'))
            print("sent loggin noti to server")
            s.recv(1024).decode("utf")
            #s.recv(1024).decode('utf-8')
            s.send(input1.encode("utf-8"))
            print("sent username")
            s.recv(1024).decode("utf")
            #s.recv(1024).decode('utf-8')
            s.send(input2.encode("utf-8"))
            s.recv(1024).decode("utf")
            print(s)
            print("sent password")
            if s.recv(1024).decode("utf-8") == "denied":
                print("incorrect login")
                time.sleep(3)
                s.close()
            print("login secces")
            time.sleep(10)
            print(s)
        except:
            reconnect()




    def save():
        
        timp = 1
        for i in range(35):
            timp = timp + 1
            count = str(f"{timp}")
            #print(f"timp - {[timp]}")
            msg_ = str(msg[i])
            os.environ[f"{count}"] = msg_
            os.environ["msgnum"] = count
            dotenv.set_key(dotenv_file, f"{count}", os.environ[f"{count}"])
            #print("saved")
            

    def chat_rev():
        global msgcount
        print("chat_rev")
        while True:
            #print(msg)
            #print("waiting")
            try:
                rev = s.recv(1024).decode('utf-8')
            except:
                print('reconnecting')
                reco = threading.Thread(target=reconnect)
                reco.start()
                reco.join()
                time.sleep(10)
            #print(f"... {rev}")
            if rev == "1998":
                #print(f"... {rev}")
                #s.send(rev.encode("utf-8"))
                reve = (f"{s.recv(1024).decode('utf-8')}")
                #msgfont = font.render((reve),True,(255,255,255))
                msg.append(reve)
                msgcount = msgcount + 1
                
                

                
                
               
               
            rev = 0

    
    loginButton_color = (25,70,30)
    loginButton_color_nohover = (25,70,30)
    loginButton_color_hover = (5, 50, 10)

    splash = cv2.VideoCapture("Splash.mp4")
    success, Video_image = splash.read()
    fps = splash.get(cv2.CAP_PROP_FPS)

    while splash_screen:
        tick.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.quit()
        
        success, video_image = splash.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
        else:
            splash_screen = False
            starting = True
            
        wn.blit(video_surf, (0, 0))
        pygame.display.update()



    while program:
        pygame.draw.rect(wn, (5,10,50), (0, 0, 1024, 768))
        
        RGBRRR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
                
            
            
        font = pygame.font.Font(None,20)
        versionblit = font.render((f"Early Access build - {VersionDate} {Version}"),True, (255,255,255))
        font = pygame.font.Font(None,30)
        if starting:
            pygame.draw.rect(wn, (10,15,55),(342, 200, 372, 382))
            tick.tick()
            login_screen = font.render(("Welcome Please Login"), True ,(255,255,255))
            loginbutton = font.render(("Login"),True, (255,255,255))
            pygame.draw.rect(wn, color, (395, 305, 270, 30))
            pygame.draw.rect(wn, color2, (395, 355, 270, 30))
            username_box = pygame.Rect(395, 305, 270, 30)
            Password_box = pygame.Rect(395, 355, 270, 30)
            wn.blit(login_screen, (415,245))
            BackButton = pygame.Rect(352,210,68,48)
            userinput = font.render((user),True,(255,255,255))
            passinput = font.render((pas),True,(255,255,255))
            pygame.draw.rect(wn, loginButton_color, (490,486, 80,50 ))
            wn.blit(loginbutton, (500,500))
            loginbox = pygame.Rect(490,486, 80,50)
            wn.blit(versionblit, (500,560))
            settinshitbox = pygame.Rect(675,210,48,24)
            if os.getenv("ip") == "":
                font = pygame.font.Font(None,20)
                Warning_ip = font.render(("WARNING NO IP ADRESS. SET AN IP AND RESTART"),True,(255,0,0))
                font = pygame.font.Font(None,30)
                wn.blit(Warning_ip, (370,450))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEMOTION:
                    
                    if loginbox.collidepoint(event.pos):
                        loginButton_color = loginButton_color_hover
                        
                    else:
                        loginButton_color = loginButton_color_nohover
                if event.type == pygame.QUIT:
                    print("quit")
                    program = False
                    save_ = threading.Thread(target=save)
                    save_.start()
                    save_.join()
                    sys.quit()
                    pygame.quit()
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
                    if settinshitbox.collidepoint(event.pos):
                        settingsgui = True
                    if settingsgui and BackButton.collidepoint(event.pos):
                        settingsgui = False
                        

            font = pygame.font.Font(None,25)
            
            wn.blit(settingsicon,(675,210))
            wn.blit(userinput, (405,315))
            wn.blit(passinput, (405,365))


        if reg:
            tick.tick()
            pygame.draw.rect(wn, (10,15,55),(342, 200, 372, 382))
            font = pygame.font.Font(None,30)
            login_screen = font.render(("Welcome Please Signup"), True ,(255,255,255))
            loginbutton = font.render(("Signup"),True, (255,255,255))
            pygame.draw.rect(wn, color, (395, 305, 270, 30))
            pygame.draw.rect(wn, color2, (395, 355, 270, 30))
            
            username_box = pygame.Rect(395, 305, 270, 30)
            Password_box = pygame.Rect(395, 355, 270, 30)
            wn.blit(login_screen, (415,245))
            
            userinput = font.render((user),True,(255,255,255))
            passinput = font.render((pas),True,(255,255,255))
           
            pygame.draw.rect((wn, loginButton_color), (490,486, 80,50 ))
            wn.blit(loginbutton, (500,500))
            loginbox = pygame.Rect(471,486, 490,520)
            BackButton = pygame.Rect(352,210,48,25)
            for event in pygame.event.get():
                if loginbox.collidepoint(event.pos):
                    loginbutton_color = loginButton_color_hover
                else:
                    loginbutton_color = loginButton_color_nohover
                if event.type == pygame.QUIT:
                    save_ = threading.Thread(target=save)
                    save_.start()
                    save_.join()
                    sys.quit()
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
                    if settingsgui and BackButton.collidepoint(event.pos):
                        print("back")
                        settingsgui = False

            font = pygame.font.Font(None,25)
            pygame.draw.rect(wn, (255,255,255),(675,210,24,24))
            wn.blit(settingsicon,(695,250))
            wn.blit(userinput, (405,315))
            wn.blit(passinput, (405,365))

        if settingsgui:
            pygame.draw.rect(wn, (10,15,55),(342, 200, 372, 382))
            wn.blit(BackButtonimg, (352,210))
            
        if logg:
            tick.tick()
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
            s.send("chatmsg".encode("utf-8"))
            s2.recv(1024).decode('utf-8')
            s.send(user.encode("utf-8"))
            s2.recv(1024).decode('utf-8')
            s.send(("has logged in").encode('utf-8'))
            s2.recv(1024).decode('utf-8')
            
        
        if loggedin:
            tick.tick()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    save_ = threading.Thread(target=save)
                    save_.start()
                    save_.join()
                    sys.quit()
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
                            print(s)
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
                font = pygame.font.Font(None,25)
                msgfont = font.render((f"{msg[i]}"),True,(255,255,255))
                wn.blit(msgfont,(8,ycord))
            
            
            #print(msg)
        
        font = pygame.font.Font(None,20)
        """fps = font.render((f"fps - {tick.get_fps()}"), True, (255,255,255))
        wn.blit(fps, (0,0))"""
        
        pygame.display.update()

    


t1 = threading.Thread(target=GUI)
t1.start()

