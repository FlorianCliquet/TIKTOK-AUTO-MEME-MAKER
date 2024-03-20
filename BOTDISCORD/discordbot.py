import discord
from discord.ext import commands, tasks
import os
from datetime import datetime, timedelta
from discord import Intents

intents = Intents.default()
intents.messages = True 
intents.guilds = True    
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)
chemin_fichier = 'path_to/ytb_vid_to_dl.txt'
contenu_precedent = []
nombre_lignes_ajoutees = 0
nombre_videos_upload = 0

def check_file():
    if not os.path.exists(chemin_fichier):
        with open(chemin_fichier, 'w') as file:
            file.write('')


@tasks.loop(seconds=60)
async def check_file_changes():
    global contenu_precedent, nombre_videos_upload
    check_file()

    with open(chemin_fichier, 'r') as file:
        contenu_actuel = file.readlines()

    lignes_supprimees = [ligne for ligne in contenu_precedent if ligne not in contenu_actuel]

    for ligne in lignes_supprimees:
        url, titre = ligne.strip().split(' ', 1)
        channel = bot.get_channel(1194006198714892429) 
        if channel:
            await channel.send(f"Une vidéo a été uploadée : {titre}")
            nombre_videos_upload += 1

    contenu_precedent = contenu_actuel

@bot.command()
async def addfichier(ctx, url, titre):
    global nombre_lignes_ajoutees
    check_file()
    with open(chemin_fichier, 'a') as file:
        file.write(f'{url} {titre}\n')
        nombre_lignes_ajoutees += 1
    await ctx.send('Fichier mis à jour avec succès!')

@tasks.loop(hours=24)
async def envoyer_recapitulatif_journalier():
    global nombre_lignes_ajoutees, nombre_videos_upload
    channel = bot.get_channel(1194006099846774905)  
    if channel:
        await channel.send(f"Récapitulatif du jour : {nombre_lignes_ajoutees} lignes ajoutées, {nombre_videos_upload} vidéos uploadées.")
    nombre_lignes_ajoutees = 0
    nombre_videos_upload = 0

@envoyer_recapitulatif_journalier.before_loop
async def avant_envoyer_recapitulatif_journalier():
    heure_envoi = datetime.now().replace(hour=20, minute=0, second=0)  
    if heure_envoi < datetime.now():
        heure_envoi += timedelta(days=1)
    await discord.utils.sleep_until(heure_envoi)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    check_file_changes.start()
    envoyer_recapitulatif_journalier.start()

@bot.command()
async def affichertitres(ctx):
    check_file() 
    with open(chemin_fichier, 'r') as file:
        lignes = file.readlines()

    if not lignes:
        await ctx.send("Il n'y a pas de vidéos dans le fichier.")
        return

    titres = [ligne.split(' ', 1)[1] for ligne in lignes if ligne.strip()] 
    reponse = "\n".join(f"{i+1}. {titre.strip()}" for i, titre in enumerate(titres))

    nombre_videos = len(titres)
    reponse += f"\n\nNombre total de vidéos : {nombre_videos}"

    if len(reponse) > 2000:
        await ctx.send("La liste est trop longue pour être affichée ici. Envoi sous forme de fichier...")
        with open("titres_temp.txt", "w") as temp_file:
            temp_file.write(reponse)
        await ctx.send(file=discord.File("titres_temp.txt", filename="titres.txt"))
        os.remove("titres_temp.txt")
    else:
        await ctx.send(reponse)


@bot.command(name="customhelp")
async def customhelp(ctx):
    em = discord.Embed(title="Help", description="Liste des commandes disponibles:", color=ctx.author.color)
    em.add_field(name="/addfichier", value="Ajoute une URL et un titre au fichier.")
    em.add_field(name="/customhelp", value="Affiche ce message d'aide.")
    em.add_field(name="/affichertitres", value="Affiche tous les titres du fichier.txt")
    await ctx.send(embed=em)

bot.run('YOUR TOKEN')
