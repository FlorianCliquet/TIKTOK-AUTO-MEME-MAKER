import time
from Scripts.Bot import Bot
from Scripts.Browser import Browser
from Scripts.Cookies import Cookies
from Scripts.utils import randomTimeQuery
import pyautogui
import pyperclip
import tkinter as tk
from selenium.webdriver.common.by import By



PROTECTED_FILES = ["processed.mp4", "VideosSaveHere.txt"]

class Upload:
    def __init__(self, user):
        self.bot = None
        self.lang = "en"
        self.url = f"https://www.tiktok.com/upload?lang={self.lang}"
        self.cookies = None
        self.userRequest = {"dir": "", "cap": "", "vidTxt": ""}
        self.video = None
        self.videoFormats = ["mov", "flv", "avi"]
        self.userPreference = user

    def uploadVideo(self, video_dir,running):
        if running:
            if self.bot is None:
                self.bot = Browser().getBot()
                self.webbot = Bot(self.bot)
            self.userRequest["dir"] = video_dir
            self.checkFileExtensionValid()
            self.bot.get(self.url)
            self.cookies = Cookies(self.bot)
            self.bot.refresh()
            time.sleep(5)
            print(video_dir)
            self.inputVideo(video_dir,running)
            randomTimeQuery()
            self.inputdl(running)
        else:
            print("Arrêt du programme")
            raise SystemExit

    def RecupDimension(self):
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.destroy()
        return screen_width,screen_height
    
    def checkFileExtensionValid(self):
        if self.userRequest["dir"].endswith('.mp4'):
            pass
        else:
            self.bot.close()
            exit(f"File: {self.userRequest['dir']} has wrong file extension.")

    def inputdl(self,running):
        if running:
            pyautogui.click(x=1607, y=1030)
            print("Decline cookies")
            time.sleep(2)
            pyautogui.click(x=1024,y=384)
            pyautogui.press('pagedown')
            time.sleep(1)
            pyautogui.click(x=879, y=844)
            print("video upload")
            time.sleep(10)
            self.bot.close()
        else:
            print("Arrêt du programme")
            raise SystemExit
    def inputVideo(self, video_dir, running):
        if running:
            width = self.RecupDimension()[0]
            height = self.RecupDimension()[1]
            click_width = width/3.157894737
            click_height = height/2.776349614
            time.sleep(60)
            pyautogui.click(width//2,height//2)
            print("Boite de dialogue ouverte")
            print(f"File path to be uploaded: {video_dir}")
            time.sleep(4)
            pyautogui.click(click_width,click_height)
            time.sleep(1)
            pyautogui.hotkey('ctrl','l')
            time.sleep(1)
            pyperclip.copy(video_dir)
            pyautogui.hotkey('ctrl','v')
            for _ in range(3):
                time.sleep(5)
                pyautogui.hotkey('enter')
            time.sleep(180)
            pyautogui.click(width/2.427307206,height/2.199592668)
            description_plusieurs_parties =""
            hashtag = "#youtube #youtuber #instagram #music #love #spotify #tiktok #follow #like #explorepage #youtubers #youtubechannel #gaming #twitch #video #instagood #hiphop #memes #viral #subscribe #gamer #rap #facebook #explore #ps #art #soundcloud #k #artist #trending #fyp #foryou #viral #explorepage #explore #foryoupage #tiktok #instagram #love #like #follow #ke #fypage #trending #instagood #likeforlikes #followforfollowback #fy #lfl #fet #k #reels #fashion #photography #memes #likes #art #music #foryourpage #fff"
            pyautogui.keyDown('ctrl')
            pyautogui.keyDown('a')       
            pyperclip.copy('->')
            pyautogui.hotkey('ctrl','v')
            pyautogui.keyUp('ctrl')
            pyautogui.keyUp('a')
            pyperclip.copy(description_plusieurs_parties)
            pyautogui.hotkey('ctrl','v')
            for _ in range(11):
                pyautogui.hotkey('enter')
            pyperclip.copy(hashtag)
            pyautogui.hotkey('ctrl','v')
        else:
           print("Arrêt du programme")
           raise SystemExit
            