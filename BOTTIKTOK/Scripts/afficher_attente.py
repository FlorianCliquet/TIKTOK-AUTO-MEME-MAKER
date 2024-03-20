import sys
import time

def afficher_attente(temps,detail):
    while temps > 0:
        if temps/3600 < 1:
            if temps/60 < 1:
                unite = '(temps restant = '+str(round(temps))+' secondes)'
            else:
                temps2= round(temps/60,2)
                unite = '(temps restant = '+str(round(temps2))+' minutes)'
        else:
            temps2= round(temps/3600,2)
            unite = "(temps restant = "+str(temps2)+" heures)"
        sys.stdout.write(f"\rEn attente pour la prochaine {detail}..."+str(unite))
        sys.stdout.flush()
        time.sleep(1)
        temps -= 1

    sys.stdout.write("\rAttente pour la {detail} vidéo terminée.                 \n")
    sys.stdout.flush()