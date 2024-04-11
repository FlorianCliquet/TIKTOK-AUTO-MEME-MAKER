----------------------------------------------------------------- # TikTok Auto Meme Maker[FR]----------------------------------------------------------------------------
## Aperçu du Projet

Ce projet automatise le processus de création et de téléchargement de memes sur TikTok. Il se compose de deux composants principaux :

1. **Bot Discord** : Surveille un fichier texte pour les nouveaux URL de memes et leurs titres, puis envoie des notifications dans un canal Discord. Il fournit également des commandes pour ajouter des URL et des titres au fichier et afficher la liste des titres.

2. **Bot TikTok** : Télécharge des vidéos YouTube, les segmente en sections dignes de devenir des memes à l'aide de l'IA, crée des vidéos compatibles avec TikTok et les télécharge sur TikTok.

## Structure du Dossier

```
TIKTOK-AUTO-MEME-MAKER/
│
├── BOTDISCORD/
│ ├── discordbot.py
│
├── BOTTIKTOK/
│ ├── CookiesDir/
│ ├── Scripts/
│ │ ├── afficher_attente.py
│ │ ├── autocropper.py
│ │ ├── Bot.py
│ │ ├── Browser.py
│ │ ├── configuration.py
│ │ ├── Cookies.py
│ │ ├── montage.py
│ │ ├── tri_numerique.py
│ │ ├── Upload.py
│ │ ├── upload_one_video_per_hour.py
│ │ └── User.py
│ ├── main.py
│ ├── SPAMVIDEO/
│ ├── VideoDirPath/
│ ├── VideoUploadQueue/
│ └── ytb_vid_to_dl.txt
│
└── README.md
```

## Instructions d'Installation

1. Clonez ce dépôt : `git clone https://github.com/FlorianCliquet/TIKTOK-AUTO-MEME-MAKER.git`
2. Installez les dépendances requises avec dependencies.txt.
3. Configurez le jeton du bot Discord et les identifiants de l'API TikTok.
4. Exécutez le bot Discord en utilisant `python discordbot.py`.
5. Exécutez le bot TikTok en utilisant `python main.py`.

## Utilisation

- Utilisez les commandes Discord pour ajouter des URL de memes et leurs titres.
- Surveillez le canal Discord pour les notifications concernant les vidéos téléchargées.
- Vérifiez le compte TikTok pour les nouveaux memes téléchargés.

## Contribution

Les contributions sont les bienvenues ! N'hésitez pas à ouvrir des problèmes ou à soumettre des demandes de tirage (pull requests).

## WARNING

Tiktok ayant un problème avec le botting, ils ne permettent pas d'accèder au boutton avec les xpath, il faut donc changer les coordonnées en fonction des dispositions des bouttons de votre compte tiktok , car cela change en fonction du compte.

## Licence

Ce projet est sous licence MIT - voir le fichier [MIT](LICENSE) pour plus de détails.

----------------------------------------------------------------- # TikTok Auto Meme Maker[EN]----------------------------------------------------------------------------
## Project Overview

This project automates the process of creating and uploading memes to TikTok. It consists of two main components:

1. **Bot Discord**: Monitors a text file for new meme URLs and titles, then sends notifications to a Discord channel. It also provides commands to add URLs and titles to the file and display the list of titles.

2. **Bot TikTok**: Downloads YouTube videos, segments them into meme-worthy sections using AI, creates TikTok-compatible videos, and uploads them to TikTok.

## Folder Structure

```
TIKTOK-AUTO-MEME-MAKER/
│
├── BOTDISCORD/
│ ├── discordbot.py
│
├── BOTTIKTOK/
│ ├── CookiesDir/
│ ├── Scripts/
│ │ ├── afficher_attente.py
│ │ ├── autocropper.py
│ │ ├── Bot.py
│ │ ├── Browser.py
│ │ ├── configuration.py
│ │ ├── Cookies.py
│ │ ├── montage.py
│ │ ├── tri_numerique.py
│ │ ├── Upload.py
│ │ ├── upload_one_video_per_hour.py
│ │ └── User.py
│ ├── main.py
│ ├── SPAMVIDEO/
│ ├── VideoDirPath/
│ ├── VideoUploadQueue/
│ └── ytb_vid_to_dl.txt
│
└── README.md
```

## Setup Instructions

1. Clone this repository: `git clone https://github.com/FlorianCliquet/TIKTOK-AUTO-MEME-MAKER.git`
2. Install the required dependencies stored in dependencies.txt
3. Set up the Discord bot token and TikTok API credentials.
4. Run the Discord bot using `python discordbot.py`.
5. Run the TikTok bot using `python main.py`.

## Usage

- Use Discord commands to add meme URLs and titles.
- Monitor the Discord channel for notifications about uploaded videos.
- Check the TikTok account for newly uploaded memes.

## WARNING

Due to TikTok's issue with botting, they do not allow access to the button with XPath. Therefore, you need to adjust the coordinates based on the layout of the buttons on your TikTok account, as it varies depending on the account.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License - see the [MIT](LICENSE) file for details.

