import undetected_chromedriver as uc
from fake_useragent import UserAgent, FakeUserAgentError
class Browser:
    def __init__(self):
        try:
            ua = UserAgent()
            self.user_agent = ua.random
        except FakeUserAgentError:
            self.user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        options = uc.ChromeOptions()
        self.bot = uc.Chrome(options=options)
        self.bot.delete_all_cookies()

    def getBot(self):
        return self.bot
