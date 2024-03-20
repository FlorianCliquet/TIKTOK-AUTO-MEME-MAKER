import sys
import tkinter as tk
import threading
import os
from Scripts.User import User
from random import randint
from Scripts.afficher_attente import afficher_attente
from Scripts.upload_one_video_per_hour import upload_one_video_per_hour
from Scripts.autocropper import cropper


class TextRedirector(object):

    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def write(self, str):
        self.widget.configure(state=tk.NORMAL)
        self.widget.insert(tk.END, str, (self.tag,))
        self.widget.see(tk.END)
        self.widget.configure(state=tk.DISABLED)

    def flush(self):
        pass 


def start_output_redirector(text_widget):
    sys.stdout = TextRedirector(text_widget, "stdout")
    sys.stderr = TextRedirector(text_widget, "stderr")


def get_current_directory():
        return os.path.dirname(os.path.realpath(__file__))


current_directory = get_current_directory()
configurations = [
    {
        "name": "default_config",
        "video_directory": current_directory+"/METTREVIDEOICI",
        "output_folder": current_directory+"/VideoDirPath",
        "duration": 35,
        "attentepartie": 3600,
        "tempsattente": 86400
    },
]

selected_config = configurations[0]  


running = True  
process_thread = None 
config_dropdown = None
selected_config_var = None 


def start_process(upload_counter_label,root,current_directory):
    global running
    global process_thread

    running = True
    def update_upload_counter():
        current_value = int(upload_counter_label.cget("text"))
        upload_counter_label.config(text=str(current_value + 1))

    def process():
        global running

        while running:
            output_folder = selected_config["output_folder"]
            duration = selected_config["duration"]
            attentepartie = selected_config["attentepartie"]
            tempsattente = selected_config["tempsattente"]
            video_directory = selected_config["video_directory"]

            print("Croppage video grâce à GPT4-turbo")
            cropper(video_directory,output_folder,duration,current_directory)
            print("Vidéo découpée avec succès.")
            video_folder = f'{output_folder}/cropped/'
            print("Début de l'upload des vidéos...")
            print('video folder is ' + str(output_folder))
            upload_one_video_per_hour(User(), video_folder, attentepartie,running)
            print("Upload des vidéos terminé.")
            root.after(1, update_upload_counter)    
            tempsattente2 = randint(int(tempsattente * 0.95), int(tempsattente * 1.05))
            afficher_attente(tempsattente2, 'video')
    process_thread = threading.Thread(target=process)
    process_thread.start()

def stop_process():
    global running
    running = False

def select_config(event):
    global selected_config
    global selected_config_var
    index = configurations.index(selected_config_var.get())
    selected_config = configurations[index]

def create_new_config():
    new_config_window = tk.Toplevel()
    new_config_window.title("Nouvelle Configuration")

    new_config_name_label = tk.Label(new_config_window, text="Nom de la nouvelle configuration")
    new_config_name_label.pack()
    new_config_name_entry = tk.Entry(new_config_window)
    new_config_name_entry.pack()

    new_config_video_directory_label = tk.Label(new_config_window, text="Répertoire de vidéos")
    new_config_video_directory_label.pack()
    new_config_video_directory_entry = tk.Entry(new_config_window)
    new_config_video_directory_entry.pack()

    new_config_output_folder_label = tk.Label(new_config_window, text="Dossier de sortie")
    new_config_output_folder_label.pack()
    new_config_output_folder_entry = tk.Entry(new_config_window)
    new_config_output_folder_entry.pack()

    new_config_duration_label = tk.Label(new_config_window, text="Durée")
    new_config_duration_label.pack()
    new_config_duration_entry = tk.Entry(new_config_window)
    new_config_duration_entry.pack()

    new_config_attentepartie_label = tk.Label(new_config_window, text="Attente partie")
    new_config_attentepartie_label.pack()
    new_config_attentepartie_entry = tk.Entry(new_config_window)
    new_config_attentepartie_entry.pack()

    new_config_tempsattente_label = tk.Label(new_config_window, text="Temps attente")
    new_config_tempsattente_label.pack()
    new_config_tempsattente_entry = tk.Entry(new_config_window)
    new_config_tempsattente_entry.pack()


    def save_new_config():
        new_config_name = new_config_name_entry.get()
        new_config_video_directory = new_config_video_directory_entry.get()
        new_config_output_folder = new_config_output_folder_entry.get()
        new_config_duration = new_config_duration_entry.get()
        new_config_attentepartie = new_config_attentepartie_entry.get()
        new_config_tempsattente = new_config_tempsattente_entry.get()

        new_config = {
            "name": new_config_name,
            "video_directory": new_config_video_directory,
            "output_folder": new_config_output_folder,
            "duration": new_config_duration,
            "attentepartie": new_config_attentepartie,
            "tempsattente": new_config_tempsattente,
            }

        configurations.append(new_config)

        config_names = [config["name"] for config in configurations]
        selected_config_var.set(new_config_name)
        config_dropdown['menu'].delete(0, 'end')  
        for name in config_names:
            config_dropdown['menu'].add_command(label=name, command=lambda new_name=name: selected_config_var.set(new_name))

        index = config_names.index(new_config_name)
        config_dropdown['text'] = new_config_name

        new_config_window.destroy() 

    save_button = tk.Button(new_config_window, text="Enregistrer", command=save_new_config)
    save_button.pack()

    cancel_button = tk.Button(new_config_window, text="Annuler", command=new_config_window.destroy)
    cancel_button.pack()



def main():
    root = tk.Tk()
    root.title("Tiktok bot")
    current_directory = get_current_directory()
    configurations = [
        {"name": "default_config", "video_directory": current_directory+"/METTREVIDEOICI", "output_folder":  current_directory+"/VideoDirPath", "duration": 60, "attentepartie": 3600, "tempsattente": 86400},
    ]
    selected_config = tk.StringVar(root)
    selected_config.set(configurations[0]["name"])
    config_dropdown = tk.OptionMenu(root, selected_config, *[config["name"] for config in configurations])
    config_dropdown.pack()

    start_button = tk.Button(root, text="Démarrer", command=lambda: start_process(upload_counter_label, root,current_directory))
    start_button.pack()

    stop_button = tk.Button(root, text="Arrêter", command=stop_process)
    stop_button.pack()

    new_config_button = tk.Button(root, text="Nouvelle Configuration", command=create_new_config)
    new_config_button.pack()

    upload_counter_label = tk.Label(root, text="0")
    upload_counter_label.pack()

    terminal_output = tk.Text(root, wrap='word', state=tk.DISABLED)
    terminal_output.tag_config("stdout", foreground="black")
    terminal_output.tag_config("stderr", foreground="red")
    terminal_output.pack(expand=True, fill='both')

    start_output_redirector(terminal_output)

    root.mainloop()

if __name__ == "__main__":
    main()
