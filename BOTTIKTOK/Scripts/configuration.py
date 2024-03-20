class Configuration:
    def __init__(self, video_directory, output_folder, duration, attentepartie,tempsattente):
        self.video_directory = video_directory
        self.output_folder = output_folder
        self.duration = duration
        self.attentepartie = attentepartie
        self.tempsattente = tempsattente
        
    def getVideoDirectory(self):
        return self.video_directory
    
    def getOutputFolder(self):
        return self.output_folder
    
    def getDuration(self):
        return self.duration
    
    def getAttentePartie(self):
        return self.attentepartie

    def getTempsAttente(self):
        return self.tempsattente