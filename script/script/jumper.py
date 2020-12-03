from PIL import Image
import os
import time
from utils import *
import ai
import cv2
import aircv as ac

ai.init()


def read_image():
    time.sleep(2)
    # if your OS is win
    os.system("cd D:/Program Files (x86)/Game/新建文件夹/Nox/bin && adb.exe shell screencap -p /sdcard/src.png")
    os.system("cd D:/Program Files (x86)/Game/新建文件夹/Nox/bin && adb.exe pull /sdcard/src.png D:/学习/大三/大三下/其它/scriptf")
    #im = Image.open("src.png")
    #im.save("./src.png")
    

    # if your OS is mac
    # os.system("cd ../../dependency/platform-tools-macos && ./adb shell screencap -p /sdcard/autojump.png")
    # os.system("cd ../../dependency/platform-tools-macos && ./adb pull /sdcard/autojump.png ../../example/jump_python")

    '''im = Image.open("autojump.png")
    print (im.size)
    if im.size[0] > im.size[1]:
        im = im.transpose(Image.ROTATE_270)
        im.save("./autojump.png")'''
   
def draw_circle(img, pos1,pos2):
        for i in pos1:
                cv2.circle(img, (int(i['result'][0]),int(i['result'][1])), 50, (0,255,0), 10)
        for i in pos2:
                cv2.circle(img, (int(i['result'][0]),int(i['result'][1])), 50, (0,0,255), 10)
        cv2.imshow('objDetect', img) 
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        

def click_screen(x,y,intertime = 1):
    # if your OS is win
    os.system("cd D:/Program Files (x86)/Game/新建文件夹/Nox/bin && adb.exe shell input tap " + str(x) + " "+str(y))
    time.sleep(intertime)
    # is your OS is mac
    # os.system("cd ../../dependency/platform-tools-macos && ./adb shell input swipe 50 50 50 50  "+str(int(press_time)))

def swipe_screen():
        os.system("cd D:/Program Files (x86)/Game/新建文件夹/Nox/bin && adb.exe shell input swipe 640 520 640 170 2000"
        )
        time.sleep(1)


def eatApple(apple = 3):
        read_image()
        imsrc = ac.imread("src.png")
        imapple = ac.imread("apple.png")
        pos = ac.find_template(imsrc,imapple)
        print(pos)
        if pos == None:
                time.sleep(4)
                return
        if apple == 1:
                click_screen(640,320)
        elif apple == 2:
                click_screen(640,440)
        else:
                click_screen(640,560)
        click_screen(830,570,4)

def chooseMap():
        while True:
                read_image()
                imsrc = ac.imread("src.png")
                imclose = ac.imread("close.png")
                pos = ac.find_template(imsrc,imclose)
                if pos != None:
                        break
        time.sleep(1)
        click_screen(900,182)

def chooseAssistant(Names = 0,cloth = 0):
        if cloth == 0:
                imcloth = ac.imread("cloth.png")
        elif cloth == 1:
                imcloth = ac.imread("Exp.png")
        elif cloth == 2:
                imcloth = ac.imread("QP.png")
        elif cloth == 3:
                imcloth = ac.imread("Qp_new.png")
        if Names == 0:
                imname = ac.imread("Kongming.png")
        elif Names ==1:
                imname = ac.imread("Meilin.png")
        elif Names == 2:
                imname = ac.imread("Skadi.png")
        else:
                imname = ac.imread(Names)
        while True:
                for k in range(3):
                        read_image()
                        imsrc = ac.imread("src.png")
                        if cloth != -1:
                                pos1 = ac.find_all_template(imsrc,imcloth,0.9)
                        pos2 = ac.find_all_template(imsrc,imname,0.8)
                        result = ()
                        flag1 = False
                        for j in pos2:
                                if cloth != -1:
                                        for i in pos1:
                                                if (i['result'][1] - j['result'][1] < 100 
                                                and i['result'][1] - j['result'][1] > -100):
                                                        result = (int(j['result'][0]),int(j['result'][1]))
                                                        click_screen(result[0],result[1])
                                                        #start game
                                                        click_screen(1175,655)
                                                        return True
                                        if flag1:
                                                break
                                else:
                                        result = (int(j['result'][0]),int(j['result'][1]))
                                        click_screen(result[0],result[1])
                                        #start game
                                        # click_screen(1175,655)
                                        return True
                        if k != 2:
                                swipe_screen()
                                # time.sleep(3)
                        
                click_screen(840,120)
                click_screen(840,560)
        #print(pos2)
        #draw_circle(imsrc,pos1,pos2)

def useSkill(servant,num,target = 0):
        if target == 0:
                click_screen(160 + (servant-1)*320 + (num-2)*110,580,4)
        else:
                click_screen(160 + (servant-1)*320 + (num-2)*110,580,0.3)
                click_screen(330 + (target-1)*310,460,4)


def chooseEnermy(num = 2):
        click_screen(50 + 240*(num-1),50)

def findLoc(pos,sumWeight,currentWeight):
        for i  in pos:
                x = i['result'][0]
                y = i['result'][1]
                z = 0
                if y < 300:
                        continue
                if x < 260:
                        z=0
                elif x < 510:
                        z=1
                elif x < 770:
                        z=2
                elif x < 1040:
                        z=3
                else:
                        z=4
                sumWeight[z] = sumWeight[z] + currentWeight
        return sumWeight

def chooseCard(ULT = None,servant = False,ezType=True):
        click_screen(1146,617)
        k = 3
        gate = [130,380,630,880,1130]
        loc = [120,380,630,890,1140]
        num = [0,1,2,3,4]
        time.sleep(1)
        if ULT != None:
                for i in ULT:
                        click_screen(380 + (i-1)*250,200,0.3)
                        k = k - 1
        if k != 0:
                if ezType == False:
                        read_image()
                        imsrc = ac.imread("src.png")
                        imBuster = ac.imread("buster.png")
                        imStrong = ac.imread("Strong.png")
                        imweak = ac.imread("weak.png")
                        posBuster = ac.find_all_template(imsrc,imBuster)
                        if servant:
                                imServant = ac.imread("servant.png")
                                posServant = ac.find_all_template(imsrc,imServant,0.9)
                        else:
                                posServant = None
                        posStrong = ac.find_all_template(imsrc,imStrong,0.6)
                        posWeak = ac.find_all_template(imsrc,imweak,0.6)
                        weight = [0,0,0,0,0]
                        if posBuster != None :
                                if  ULT == None:
                                        weight = findLoc(posBuster,weight,5)
                                else:
                                        weight = findLoc(posBuster,weight,1)
                        #print(weight)
                        if posServant != None :
                                weight = findLoc(posServant,weight,10)
                        #print(posServant)
                        #print(weight)
                        if posStrong != None:
                                weight = findLoc(posStrong,weight,2)
                        #print(weight)
                        if posWeak != None:
                                weight = findLoc(posWeak,weight,-6)
                        #print(weight)
                        #print(posServant)
                        #print(posStrong)
                        #draw_circle(imsrc,posServant,posStrong)
                        for i in range(k):
                                index = weight.index(max(weight))
                                #print(weight,num,index)
                                click_screen(loc[num[index]],500,0.3)
                                weight.pop(index)
                                num.pop(index)
                else:
                        for i in range(k):
                                click_screen(loc[i],500,0.3)


                          




def clothSkill(num,changeFlag = False,target = 0):
        click_screen(1200,320,0.3)
        if changeFlag:
                click_screen(800+num*100,320)
                click_screen(550,350,0.3)
                click_screen(750,350,0.3)
                click_screen(650,630,5)
                return
        elif target != 0:
                click_screen(800+num*100,320,0.3)
                click_screen(330 + (target-1)*310,460,3)
        else:
                click_screen(800+num*100,320,3)


def fight():
        imbattle = (ac.imread("battle1.png"),ac.imread("battle2.png"),
                ac.imread("battle3.png"),ac.imread("result.png"))
        immenu = ac.imread("menu.png")
        imresult = ac.imread("result.png")
        for k in range(3):
                flag = True
                
                while flag:
                        read_image()
                        imsrc = ac.imread("src.png")
                        #pos = ac.find_template(imsrc,imbattle[k],0.9)
                        pos = ac.find_template(imsrc,immenu,0.9)
                        print(k,pos)
                        if pos != None:
                                flag = False
                                time.sleep(2)
                if k == 0:
                        useSkill(servant=3,num=1,target = 2)
                        useSkill(servant=1,num=1,target = 2)
                        # clothSkill(num=3,changeFlag = True,target = 0)
                        # clothSkill(num=1,changeFlag = False,target = 0)
                        chooseCard([2],servant=False,ezType=True)
                elif k == 1:
                        useSkill(1,3,2)
                        useSkill(2,3)
                        clothSkill(2,False,2)
                        chooseCard([2],servant=False,ezType=True)
                else:
                        useSkill(1,2)
                        useSkill(3,2)
                        useSkill(3,3,2)
                        chooseCard([2],servant=False,ezType=True)
                time.sleep(15)


        #补刀，结算，连续出击                        
        while True:
                read_image()
                imsrc = ac.imread("src.png")
                pos = ac.find_template(imsrc,immenu,0.9)
                pos1  = ac.find_template(imsrc,imresult,0.9)
                if pos != None:
                        chooseCard(servant=True)
                elif pos1 != None:
                        flag = False
                        time.sleep(4)
                        for i in range(5):
                                click_screen(1100,680,1)
                        click_screen(856,560,1)
                        return
                
                      

def autoPlay(n,apple):
        for i  in range(n):
                print(i)
                # chooseMap(apple)
                # name:0-孔明 1-梅林 2-紫发
                # cloth:0-活动 1-午餐 2-大番茄 3-小番茄 -1-任意
                chooseAssistant(Names = 2,cloth = 0)
                time.sleep(5)
                fight()
                eatApple(apple)
                                        

                                
def buyLottery():
        for i in range(9):
                for j in range(100):
                        click_screen(420,455,0.2)
                click_screen(1170,245,1)
                click_screen(840,560,2)
                click_screen(640,565,1)




                                
                        




def jumper():

    # ai.init()
    # print(screenShot)
    distance = 0.0
    screenShot = Image.open('./autojump.png')

    # ******************
    # start your code here
    piece_x, piece_y, board_x, board_y = find_piece_and_board(screenShot)
    distance = math.sqrt((board_x - piece_x) ** 2 + (board_y - piece_y) ** 2)
    return distance
    # ******************


if __name__ == '__main__':
        # read_image()
        # autoPlay(25,3)
        # autoPlay(60,2)
        # buyLottery()
        autoPlay(n=30,apple=1)
