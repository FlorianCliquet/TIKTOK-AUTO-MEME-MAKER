import os
from Scripts.tri_numerique import tri_numerique
from Scripts.Upload import Upload
from Scripts.afficher_attente import afficher_attente
from random import randint
def upload_one_video_per_hour(user, video_folder,attentepartie,running):
    print(upload_one_video_per_hour)
    if running:
        print(running)
        video_extensions = ['.mp4', '.avi', '.mov', '.mkv']  
        videos = [f for f in os.listdir(video_folder) if os.path.isfile(os.path.join(video_folder, f)) and any(f.endswith(ext) for ext in video_extensions)]

        videos_trie = tri_numerique(videos,running)
        Counter = 1
        uploader = Upload(user) 
        taille_directory = len(videos_trie)
        while taille_directory > 0:
            if Counter != 1:
                attentepartie2 = randint(attentepartie*0.95,attentepartie*1.05)
                afficher_attente(attentepartie2,'partie')
            video_to_upload = video_folder+str(videos_trie[0])
            print(video_to_upload)          
            print(f"Tentative d'upload de la vidéo : {video_to_upload}")
            uploader.uploadVideo(video_to_upload,running)
            print(f"Upload de la vidéo {video_to_upload} terminé.")
            Counter += 1
            os.remove(video_to_upload)
            taille_directory -= 1
    else:
        print("Arrêt du programme")
        raise SystemExit
