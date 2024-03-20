import os, pickle
from os.path import exists


class Cookies:
    def __init__(self, bot):
        self.bot = bot
        self.cookies_dir = os.path.join(os.getcwd(), "CookiesDir")
        if not exists(self.cookies_dir):
            os.mkdir(self.cookies_dir)
        self.selectCookie()


    def selectCookie(self):
        if len(os.listdir(self.cookies_dir)) > 0:
            selected_cookie = os.listdir(self.cookies_dir)[0]  
            self.loadCookies(selected_cookie)
        else:
            print("No cookies stored on save directory!")
            self.createCookie()


    def loadCookies(self, selected_cookie):
        cookie_path = os.path.join(self.cookies_dir, selected_cookie)
        cookie_data = pickle.load(open(cookie_path, "rb"))
        for cookie in cookie_data:
            if 'sameSite' in cookie:
                if cookie['sameSite'] == 'None':
                    cookie['sameSite'] = 'Strict'
            self.bot.add_cookie(cookie)


    def createCookie(self):
        print("Your browser currently shows the tiktok login page, please login in.")
        input("After you have logged in fully, please press any button to continue...")
        print("#####")
        filename = input("Please enter a name for the cookie to be stored as::: ")
        cookie_path = os.path.join(self.cookies_dir, filename+".cookie")
        pickle.dump(self.bot.get_cookies(), open(cookie_path, "wb+"))
        print("Cookie has been created successfully, resuming upload!")