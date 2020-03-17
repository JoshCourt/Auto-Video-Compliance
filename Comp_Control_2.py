from datetime import datetime
import pyperclip  # handy cross-platform clipboard text handler
import pyautogui
from pyclick import HumanClicker
import os
import subprocess
from subprocess import Popen, PIPE
import os, time
import random
import os.path
from pathlib import Path
import sys
from imagesearch import *
from datetime import datetime as dt
hc = HumanClicker()
	### HOME PATHS					##############################

IFLoc = os.path.abspath(os.path.dirname(sys.argv[0]))
	### HOME PATHS					###############################
######################################################

imagLoc = "Images"
tempLoc = "Templates"
adobesurveyimg1 = "adobesurveyimg1.png"
cancelbutton1 = "cancelbutton1.png"
WT = 10

def SATR():
	satr = random.randrange(3,10,1)
	print(str(satr))
	return satr

def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts


def CUSTMF(FOLDERLOCATION):
	# Make a custom Folder Location
	if not os.path.exists(FOLDERLOCATION):
		print("Making "+str(FOLDERLOCATION)+" Folder")
		try:
			os.mkdir(FOLDERLOCATION)
		except:
			print("Could not create "+str(FOLDERLOCATION)+" \nCould be a problem with permissions or disk space...?")
			pass
	else:
		print(str(FOLDERLOCATION)+" Already exists! Continuing!!")


def medinfduration(FILELOC):
    media_info = MediaInfo.parse(FILELOC)
    for track in media_info.tracks:
        if track.track_type == 'Video':
            print(track.duration)
            return track.duration

def imagsearchcheck(imagery):
	tim = RRNum("1/5s")
	#pos = imagesearch(IFLoc+"\\"+imagery)
	pos = imagesearch(imagery)
	try:
		if pos[0] != -1:
			print("position : ", pos[0], pos[1])
			return True
		else:
			print("image "+str(imagery)+" not found")
			return False
	except:
		print("Image may be Corrupt")

def image_search_click(imagery):
	tim = RRNum("1/5s")
	#pos = imagesearch(IFLoc+"\\"+imagery)
	pos = imagesearch(imagery)
	try:
		if pos[0] != -1:
			print("position : ", pos[0], pos[1])
			hc.move((pos[0]+random.randrange(15,100,1),pos[1]+random.randrange(5,20,1)),1)

			# mouse click(left button)
			tim
			hc.click()
		else:
			print("image "+str(imagery)+" not found")
			return False
	except:
		print("Image may be Corrupt")

def image_search_click_extra_tiny(imagery):
	print("imagsearchTB2 STARTING : ")
	tim = RRNum("1/5s")
	try:
		imagloca = os.path.join(IFLoc, imagLoc, imagery)
		print("\nImagery Location of imagesearch is : "+str(imagloca))
		pos = imagesearch(imagloca)
		print("pos is : "+str(pos))
		testerr = imagsearchcenter(imagloca)
		print(str(testerr))
		if pos[0] != -1:
			print("position : ", pos[0], pos[1])
			hc.move((pos[0]+random.randrange(5,10,1),pos[1]+random.randrange(10,20,1)),1)
			# mouse click(left button)
			tim
			hc.click()
			return True
		else:
			print("image "+str(imagery)+" not found")
			return False
	except:
		print("Image may be Corrupt")
		pass

def OpenProg(ProgramName, ProgramPath):
    #ProgramName+"Path" = ProgramPath
    #RemProg(ProgramName, ProgramPathIdentifier, ):
    subprocess.Popen("\""+ProgramPath+"\"", shell=True, stdout=subprocess.PIPE)
    pinpng = ProgramName+"pinned.png"
    widpng = ProgramName+"widget.png"
    opepng = ProgramName+"opened.png"
    PinnedOpen = os.path.join(IFLoc, imagLoc, pinpng)
    WidgetOpen = os.path.join(IFLoc, imagLoc, widpng)
    FinalOpen = os.path.join(IFLoc, imagLoc, opepng)
    print("PinnedOpen is "+PinnedOpen+"\nWidgetOpen is "+WidgetOpen+"\nFinalOpen is "+FinalOpen)
    if BigCheck(PinnedOpen, WidgetOpen, FinalOpen, ProgramName) == False:
        return False
    elif BigCheck(PinnedOpen, WidgetOpen, FinalOpen, ProgramName) == True:
        return True

def OpenProgSimple(ProgramPath):
    #ProgramName+"Path" = ProgramPath
    #RemProg(ProgramName, ProgramPathIdentifier, ):
    subprocess.Popen(ProgramPath, shell=True, stdout=subprocess.PIPE)

def return_True_if_url_is(url_to_check_for):
    PressButts2('ctrl', 'l')
    URLCOP = copytexttovariable()
    if URLCOP == url_to_check_for:
        return True
    else:
        return False


def copytexttovariable():
    print("Copying text on screen...")
    def copy_clipboard():
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1)  # ctrl-c is usually very fast but your program may execute faster
        return pyperclip.paste()

    list = []
    var = copy_clipboard()
    list.append(var)
    #print(datetime.today().strftime('%Y-%m-%d-%X')+" : Copied item is : "+str(list[0]))
    return list[0]

def EntDeets(deets):
	for char in deets:
		randfloat = random.uniform(1,3)
		pyautogui.typewrite(char, interval=random.random()/2)

def EnterURL(URL):
    print("Entering Url : "+str(URL))
    PressButts2('ctrl', 'l')
    sSt(RRNum("1/5s"))
    EntDeets(URL)
    sSt(RRNum("1/5s"))
    pyautogui.press("enter")
    sSt(RRNum("1/5s"))

def EnterURL_robot(URL):
    print("Entering Url : "+str(URL))
    PressButts2('ctrl', 'l')
    sSt(RRNum("1/5s"))
    pyautogui.write(URL)
    time.sleep(1)
    pyautogui.press("enter")
    sSt(RRNum("1/5s"))

def BigCheck(PinnedOpen, WidgetOpen, FinalOpen, ProgramName):
    if CheckSoftwareOpen(PinnedOpen, WidgetOpen) == False:
        print(datetime.today().strftime('%Y-%m-%d-%X')+" There may be a serious error. Program Hasn't opened..\nWill wait and try once more. If failed again Program will be forced to close...\n")
        sSt(120)
        if CheckSoftwareOpen(PinnedOpen, WidgetOpen) == False:
            print(datetime.today().strftime('%Y-%m-%d-%X')+" Program still hasn't opened. \n Returning False and forcing closed.")
            CloseProg(ProgramName)
            return False
        else:
            if CheckImageWait(FinalOpen) == False:
                print(datetime.today().strftime('%Y-%m-%d-%X')+" Program still hasn't opened properly yet. \nWill wait and try again.")
                sSt(30)
                if CheckImageWait(FinalOpen) == False:
                    print(datetime.today().strftime('%Y-%m-%d-%X')+" Program still hasn't opened. \nReturning False and forcing closed.")
                    CloseProg(ProgramName)
                    return False
                else:
                    return True
            else:
                return True
    else:
        if CheckImageWait(FinalOpen) == False:
            print(datetime.today().strftime('%Y-%m-%d-%X')+" Program still hasn't opened properly yet. \nWill wait and try again.")
            sSt(30)
            if CheckImageWait(FinalOpen) == False:
                print(datetime.today().strftime('%Y-%m-%d-%X')+" Program still hasn't opened. \n Returning False and forcing closed.")
                CloseProg(ProgramName)
                return False
            else:
                return True
        else:
            return True




def CheckSoftwareOpen(PinnedOpen, WidgetOpen):
    print(datetime.today().strftime('%Y-%m-%d-%X')+" Checking Software is Open in "+str(WT)+" Second Intervals.\nWaiting.....")
    while True:
        N = splitall(PinnedOpen)
        N = N[-1]
        print("N is "+N)
        sSt(WT)
        if imagsearchcenter(PinnedOpen) is None and imagsearchcenter(WidgetOpen) is None:
            Vislog(N)
            sSt(WT)
            if imagsearchcenter(PinnedOpen) is None and imagsearchcenter(WidgetOpen) is None:
                Vislog(N)
                sSt(WT)
                if imagsearchcenter(PinnedOpen) is None and imagsearchcenter(WidgetOpen) is None:
                    Vislog(N)
                    print(datetime.today().strftime('%Y-%m-%d-%X')+" Program has not opened. Sending False response")
                    return False
                    break
                else:
                    return True
                    break
            else:
                return True
                break
        else:
            return True
            break


def CheckImageWait(imagelocation):
    print(datetime.today().strftime('%Y-%m-%d-%X')+" Checking for image in "+str(WT)+" Second Intervals.\nWaiting.....")
    while 1 == 1:
        N = splitall(imagelocation)
        N = N[-1]
        print("N is "+N)
        sSt(WT)
        if imagsearchcenter(imagelocation) is None:
            Vislog(N)
            sSt(WT)
            if imagsearchcenter(imagelocation) is None:
                Vislog(N)
                sSt(WT)
                if imagsearchcenter(imagelocation) is None:
                    Vislog(N)
                    print(datetime.today().strftime('%Y-%m-%d-%X')+" Image Cannot Be Found. Sending False response")
                    return False
                    break
                else:
                    return True
                    break
            else:
                return True
                break
        else:
            return True
            break

# Set Programme. Takes a programme path from RemProg. Splits ints program name and path for recall
def SetProgPaths(ProgName):
    imagLoc = "Images/"
    #ProgName+"PinOpen" = imageLoc+ProgName+"PinOpen.png"
    #ProgPath = ProgramPath
    #ProgName = splitall(ProgramPath)
    #print("Testing SetProg Funcation, ProgName is :"+ProgName)
    #return ProgPath, ProgName

def click_text_that_looks_like_this(imagelocationn, IMAGETEXT, THRESHOLD): # DIFFERENT IMAGES REQUIREDDD!!!
	try:
		print(datetime.today().strftime('%X')+" : textliekclick STARTING : \nImagelocatioon is : "+str(imagelocationn)+"\nText to search for is : "+str(IMAGETEXT))
		pos[1], h, pos[0], w = textlike("IMAGE", imagelocationn, THRESHOLD, "pos", IMAGETEXT)
		print("pos[0] is : "+str(pos[0]))
		print("pos[1] is : "+str(pos[1]))
		print("w is : "+str(w))
		print("h is : "+str(h))
		if pos[0] != -1:
			print("position : ", pos[0], pos[1])
			hc.move((pos[0]+random.randrange(5,h-5,1),pos[1]+random.randrange(1,w-10,1)),1)

			# mouse click(left button)
			tim
			hc.click()
			return True
		else:
			print("image "+str(imagery)+" not found")
			return False
	except:
		print("Image may be Corrupt")
		return False

def scroll_down_and_up_random():
    print("STARTING scroll_down_and_up_random")
    eggggz = numpy.random.randint(2,5)
    for _ in range(eggggz):
        sSt(RRNum("1/5s"))
        pyautogui.press("pagedown")
    #sSt(RRNum("1/5s"))
    for _ in range(eggggz):
        sSt(RRNum("1/5s"))
        pyautogui.press("pageup")
    sSt(RRNum("1/5s"))


def scroll_down_and_up_custom(A, B):
    print("STARTING scroll_down_and_up_custom")
    eggggz = numpy.random.randint(A,B)
    for _ in range(eggggz):
        sSt(RRNum("1/5s"))
        pyautogui.press("pagedown")
    #sSt(RRNum("1/5s"))
    for _ in range(eggggz):
        sSt(RRNum("1/5s"))
        pyautogui.press("pageup")
    sSt(RRNum("1/5s"))


def scroll_down_custom(A, B):
    print("STARTING scroll_down_custom")
    eggggz = numpy.random.randint(A,B)
    for _ in range(eggggz):
        sSt(RRNum("1s"))
        pyautogui.press("pagedown")
    sSt(RRNum("1/5s"))
#    for _ in range(eggggz):
#        sSt(RRNum("1s"))
#        pyautogui.press("pageup")
#    sSt(RRNum("1s"))



def CloseProg(ProgramName):
    if ProgramName == "Premiere":
        ProgramName = "Adobe Premiere Pro.exe"
    elif ProgramName == "MediaEnc":
        ProgramName = "Adobe Media Encoder.exe"
        print("ProgramName is : "+ProgramName)
    elif ProgramName == "AfterEffects":
        ProgramName = "AfterFX.exe"
        print("ProgramName is : "+ProgramName)
    else:
        print("ERROR : ProgramName is not defined. CANNOT CLOSE ")
        ForceError()
    print("Starting CLOSE PROG")
    P = splitall(ProgramName)
    P = P[-1]
    print("Program last part of path is "+"\""+P+"\"")
    print("Sending CLOSE PROG")
    os.system("taskkill /IM \""+P+"\" /F")
"""
MODULAR FUNCTIONS
"""


# Clear Name Box
def CnamB():
	pyautogui.keyDown('ctrl')
	sSt(1)
	pyautogui.keyDown('a')
	sSt(1)
	pyautogui.keyUp('ctrl')
	sSt(1)
	pyautogui.keyUp('a')
	sSt(1)
	pyautogui.press('delete')

# Visual Log - Give quoted descriptor so can identify what screenshot is of
def Vislog(descriptor):
    print("Vislog : Taking Screenshot")
    screenLoc = "Screenshots"
    screenshotPATH = os.path.join(IFLoc, screenLoc)
    screenshot = pyautogui.screenshot()
    savename = "Vislog"+time.strftime('%I-%M-%S', time.localtime())+".png"
    screenshot.save(os.path.join(screenshotPATH, savename))

# Maximise Window
def MAXWIN():
	print(datetime.today().strftime('%X')+" : Maximising Window")
	pyautogui.keyDown('alt')
	sSt(1)
	pyautogui.keyDown('space')
	pyautogui.keyUp('alt')
	sSt(1)
	pyautogui.keyUp('space')
	sSt(1)
	pyautogui.press('down')
	sSt(1)
	pyautogui.press('down')
	sSt(1)
	pyautogui.press('down')
	sSt(1)
	pyautogui.press('down')
	sSt(1)
	pyautogui.press('down')
	sSt(1)
	pyautogui.press('enter')

def MAXWINmedenc():
	print(datetime.today().strftime('%X')+" : Maximising Window")
	pyautogui.keyDown('alt')
	sSt(1)
	pyautogui.keyDown('space')
	pyautogui.keyUp('alt')
	sSt(1)
	pyautogui.keyUp('space')
	sSt(1)
	pyautogui.press('down')
	sSt(1)
	pyautogui.press('down')
	sSt(1)
	pyautogui.press('down')
	sSt(1)
	pyautogui.press('down')
	sSt(1)
	pyautogui.press('enter')

# Move Mouse at varying speeds HUMAN
def MMH(X, Y, SPEED):
    if SPEED == "fast":
        tim = RRnum("1/5s")
    elif SPEED == "medium":
        tim = RRnum("1s")
    hc.move((X,Y),tim)
    time.sleep(random.randrange(1,5,1))
    hc.click()

# Move Mouse at varying speeds COMPUTER (NOT HUMAN LIKE)
def MMC(X, Y, SPEED):
    if SPEED == "fast":
        tim = time.sleep(1)
    elif SPEED == "medium":
        tim = time.sleep(3)
    elif SPEED == "slow":
        tim = time.sleep(5)
    elif SPEED == "vslow":
        tim = time.sleep(10)

    pyautogui.moveTo(X,Y)
    tim
    pyautogui.click()

#
def RRNum(timeframe):
    def returnit():
        return a, b
    if timeframe == "1/5s":
        a = 1
        b = 5
        #returnit()
    elif timeframe == "1s":
        a = 1
        b = 10
        #returnit()
    elif timeframe == "10s":
        a = 10
        b = 60
        #returnit()
    elif timeframe == "1m":
        a = 60
        b = 600
        #returnit()
    elif timeframe == "10m":
        a = 600
        b = 1800
        #returnit()
    elif timeframe == "30m":
        a = 1800
        b = 3600
        #returnit()
    else:
        print(datetime.today().strftime('%Y-%m-%d-%X')+" Timeframe arg has not been set, or has been set wrong.\n Options are : 1/5s | 1s | 10s | 1m | 10m | 30m")
    c = random.randrange(a,b,1)
    return c

# Return Image location on screens center.
def imagsearchcenter(imagerypath):
    while True:
        if pyautogui.locateOnScreen(imagerypath) is not None:
            imagscreenloc = pyautogui.locateOnScreen(imagerypath)
            print("imagscreenloc is : "+str(imagscreenloc))
            if pyautogui.center(imagscreenloc) is not None:
                imagscreenpoint = pyautogui.center(imagscreenloc)
                print("imagscreenpoint is : "+str(imagscreenpoint))
                return imagscreenpoint.x, imagscreenpoint.y
                break
            else:
                print("imagsearchcenter ERROR 2 : cant find image...")
                return None
                break
        else:
            print("imagsearchcenter ERROR 1 : cant find image...")
            return None
            break






def message(message, string_to_print):
	#timap = Time at present
	timap = dt.today().strftime('%X')
	print("MESSAGE : "+str(timap)+" "+message+" "+str(string_to_print))


# Sleep with sleeping message
def sSt(sleeptime):
	#print("Starting sSt..")
	#print(datetime.today().strftime('%Y-%m-%d-%X')+" Sleeping "+str(sleeptime)+" Seconds")
	time.sleep(sleeptime)

def ForceError(FORCER):
    print("If no FORCER has been specified the program will exit")

def PressButts2(key1, key2):
    pyautogui.keyDown(key1)
    pyautogui.keyDown(key2)
    time.sleep(1)
    pyautogui.keyUp(key1)
    pyautogui.keyUp(key2)

def PressButts3(key1, key2, key3):
    pyautogui.keyDown(key1)
    pyautogui.keyDown(key2)
    pyautogui.keyDown(key3)
    time.sleep(1)
    pyautogui.keyUp(key1)
    pyautogui.keyUp(key2)
    pyautogui.keyUp(key3)

def MultiPressButt(butt, times):
    def dothis(butt):
        pyautogui.press(butt)

    for _ in range(times):
        time.sleep(1)
        dothis(butt)

""" PREMIERE PRO PARTS """
impch = "Importcheck.png"
Importchk = os.path.join(IFLoc, imagLoc, impch)
def checkimport():
    sSt(20)
    if imagsearchcenter(Importchk) is None:
        print("Import Succesfull")
        #Vislog("Import Succesfull")
    else:
        print("import Failed")
        return False

def closeeffectsiwndow():
    PressButts3("alt", "shift", "0")

def MakeEdits(FilePath, FileDestination, scaler, Template, NewFileName):
    while 1 == 1:
        ImportFile(str(FilePath))
        if checkimport() == False:
            closeeffectsiwndow()
            continue
        AddToSequence()
        GoToTimeline()
        SetRenderLength()
        Scale(scaler)
        while 1 == 1:
            time.sleep(10)
            # This loop may need to be edited so that if a certain amount of errors happen. Then a whole restart? OR email?
            if not AddToRenderQueu(FileDestination, NewFileName) == False:
                StartAndWatchRender()
                #Quitting Media Encoder
                QuitProg()
                #Saving And QuittiFailng Premiere Pro
                Save()
                QuitProg()
                return True
            else:
                print("Add to render queu function has returned false. Closing Media Encoder and Starting Again")
                CloseProg("MediaEnc")
                time.sleep(10)
                continue

def mvit(from11, to11):
    print("Moving "+from11+" TOO "+to11)
    shutil.move(from11, to11)

def cpit(from22, to22):
    print("Copying "+from22+" TOO "+to22)
    shutil.copy(from22, to22)

def ImportFile(FilePath):
    sSt(10)
    PressButts2("shift", "3")
    time.sleep(2)
    pyautogui.press("home")
    time.sleep(2)
    print(datetime.today().strftime('%X')+" : IMPORT FILE : STARTING ")
    PressButts2("ctrl", "i")
    time.sleep(1)
    MultiPressButt("tab", 5)
    time.sleep(1)
    pyautogui.press("space")
    time.sleep(1)
    pyautogui.typewrite(FilePath, interval=0.25)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    MultiPressButt("tab", 4)
    time.sleep(2)
    pyautogui.press("space")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(30)

def AddToSequence():
    print(datetime.today().strftime('%X')+" : STARTING : Add To Sequence")
    time.sleep(2)
    pyautogui.press(",")
    time.sleep(1)

def GoToTimeline():
    print(datetime.today().strftime('%X')+" : STARTING : Go To Timeline")
    time.sleep(1)
    PressButts2("shift", "3")

def SetRenderLength():
    print(datetime.today().strftime('%X')+" : STARTING : Set Render Length")
    PressButts2("ctrl", "a")
    time.sleep(1)
    print("PRESSING FORWARD SLASH")
    pyautogui.press("/")
    time.sleep(1)

def Scale(Scaler):
    """ PREMIERE SCALER """
    print(datetime.today().strftime('%X')+" : STARTING : Scale")
    ## Opens Efects Windows
    PressButts2("shift", "5")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.press("tab")
    time.sleep(1)
    pyautogui.typewrite(Scaler, interval=1)
    time.sleep(1)
    pyautogui.press("enter")

def checkforadobesurvey():
	print("Starting Check for Adobe Survey PopUp")
	tim = SATR()
	adobimg = os.path.join(IFLoc, imagLoc, adobesurveyimg1)
	cancelbut1 = os.path.join(IFLoc, imagLoc, cancelbutton1)
	pos = imagesearch(adobimg)
	print("IF statement starting. Finding "+str(adobimg))
	if pos[0] != -1:
		print("ERROR: Found adobesurvey image. clicking cancel")
		pyautogui.click(cancelbut1)
	else:
		print("Didnt find image....")
		pass

def AddToRenderQueu(FileDestination, NewFileName):
    print(datetime.today().strftime('%X')+" : STARTING : Add To Rendere Queu")
    ### Enter name straightawau£
    ### 7  tabs to OUTPUT NAME BOX
    ### 6 tabs to folder path
    pinpng = "Mediaencoderpinned.png"
    pinpng2 = "Mediaencoderpinned2.png"
    widpng = "Mediaencoderwidget.png"
    opepng = "Mediaencoderopened.png"
    PinnedOpen = os.path.join(IFLoc, imagLoc, pinpng)
    Pinned = os.path.join(IFLoc, imagLoc, pinpng2)
    WidgetOpen = os.path.join(IFLoc, imagLoc, widpng)
    FinalOpen = os.path.join(IFLoc, imagLoc, opepng)
    MPEG2 = os.path.join(IFLoc, imagLoc, "Formatmpeg2.png")
    Arqivawide = os.path.join(IFLoc, imagLoc, "Presetarqivawide.png")
    ExportWindowImage = os.path.join(IFLoc, imagLoc, "Exportsettings.png")
    PressButts2("shift", "3")
    time.sleep(3)
    PressButts2("ctrl", "m")
    time.sleep(3)
    print(datetime.today().strftime('%X')+" : ADDTOREND 1 : Checking for export window image in premiere")
    if CheckImageWait(ExportWindowImage) == False:
        print(datetime.today().strftime('%X')+" : ADDTOREND ERROR 1 : AddToRenderQueu Could not find Prempiere Pro Export Window. Returning False")
        Vislog("AddToRenderQueu")
        return False
    else:
        time.sleep(3)
        checkforadobesurvey()
        if CheckImageWait(MPEG2) and CheckImageWait(Arqivawide) == True:
            EnterPathAndNameOpenPrem()
            GGGG = os.path.splitext(NewFileName)[0]
            GGGG = splitall(GGGG)
            GGGG = GGGG[-1]
            time.sleep(4)
            pyautogui.typewrite(GGGG, interval=0.5)
            MultiPressButt("tab", 6)
            time.sleep(2)
            pyautogui.press("space")
            pyautogui.typewrite(FileDestination, interval=0.5)
            time.sleep(2)
            pyautogui.press("enter")
            MultiPressButt("tab", 8)
            time.sleep(2)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.press("enter")

        elif BigCheck(PinnedOpen, WidgetOpen, FinalOpen, "MediaEnc") == False:
            print(datetime.today().strftime('%X')+" : ADDTOREND ERRO 2 : Media Encoder didn't open... Trying Click on Pin and try again")
            pyautogui.click(Pinned)
            if BigCheck(PinnedOpen, WidgetOpen, FinalOpen, "MediaEnc") == False:
                print(datetime.today().strftime('%X')+" : ADDTOREND ERROR 3 : Media Encoder didn't open... returning False and creating Vis Log")
                Vislog("MediaEncOpenFAILED-"+NewFileName)
                return False
            else:
                if BigCheck(PinnedOpen, WidgetOpen, FinalOpen, "MediaEnc") == True:
                    MAXWINmedenc()
                    print(datetime.today().strftime('%X')+" : ADDTOREND 2 : Media Encoder Opened succesfully. Creating Vis Log")
                    time.sleep(2)
                    Vislog("MediaEncOpenSuccesfull-"+NewFileName)
                    return True
        else:
            if BigCheck(PinnedOpen, WidgetOpen, FinalOpen, "MediaEnc") == True:
                MAXWINmedenc()
                print(datetime.today().strftime('%X')+" : ADDTOREND 2 : Media Encoder Opened succesfully. Creating Vis Log")
                time.sleep(2)
                Vislog("MediaEncOpenSuccesfull-"+NewFileName)
                return True

def StartAndWatchRender():
    time.sleep(WT)
    checkforadobesurvey()
    print(datetime.today().strftime('%X')+" : STARTING : Start And Watch Render")
    media1 = 'Mediaencodergo.png'
    media2 = 'Mediaencoderfin.png'
    popup1 = 'Mediaencpopup1.png'
    encgo = os.path.join(IFLoc, imagLoc, media1)
    encfin = os.path.join(IFLoc, imagLoc, media2)
    print("encfin is : "+encfin)
    print("encgo is : "+encgo)
    print("Pyautogui . click starting")
    pyautogui.moveTo(100, 200)
    while True:
        pyautogui.moveTo(100, 200)
        try:
            pyautogui.click(encgo)
        except Exception as e:
            print("Exception raised : "+str(e))
        sSt(20)
        print(datetime.today().strftime('%X')+" : START/WATCHREND 1 LOOP : Checking if queue has finished yet...")
        if imagsearchcenter(encfin) is None:
            print(datetime.today().strftime('%X')+" : START/WATCHREND 2 LOOP : Couldnt find media encoder finish signal. Waiting again")
            checkforadobesurvey()
            continue
        else:
            print(datetime.today().strftime('%X')+" : START/WATCHREND 3 : Media Encoder has finished. Closing Media Encoder")
            CnamB()
            time.sleep(3)
            pyautogui.press('enter')
            time.sleep(2)
            return True



def Save():
    print(datetime.today().strftime('%X')+" : Saving")
    PressButts2("ctrl", "s")
    sSt(2)

def QuitPremiere():
    print(datetime.today().strftime('%X')+" : Quitting Premiere Pro")
    PressButts3("ctrl", "shift", "w")
    sSt(10)

def QuitMediaEnc():
    print(datetime.today().strftime('%X')+" : Quitting Media Enc")
    PressButts2("ctrl", "q")
    sSt(10)

def QuitProg():
    print(datetime.today().strftime('%X')+" : Quitting GENERIC")
    PressButts2("ctrl", "q")
    sSt(10)

def EnterPathAndNameOpenPrem():
    MultiPressButt("tab", 8)
    time.sleep(2)
    pyautogui.press("space")



"""
shift+1 = project Panel
shift+2 = timeline Panel
shift+5 = Effects Panel


Exception replace video in timeline Ctrl+Shift+2 (Reveal in explorer) Ctrl+Shift+1 (ReplaceFootage) (6 tabs to get too url)
open video in source Editorset in and out points with home i end o
Come out of source monitor
select all and press /
ctrl m + Enter?
    Then set encoder settings?
    Check Encoder Settings?
    Hit enter>?????

1920X1080 footage - scale = 55.3

"""
