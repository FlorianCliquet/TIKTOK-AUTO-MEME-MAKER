from selenium.webdriver.common.action_chains import ActionChains
class Bot:
    def __init__(self, bot):
        self.bot = bot

    def getBot(self):
        return self.bot

    def getVideoUploadInput(self):
        try:
            self.click_at_coordinates(x=772, y=438)
        except Exception as e:
            print(f"Erreur inattendue: {e}")
            return None
        
    def click_at_coordinates(self, x, y):
        try:
            action = ActionChains(self.bot)
            action.move_by_offset(x, y).click().perform()
        except Exception as e:
            print(f"Erreur lors du clic aux coordonnées ({x}, {y}): {e}")
