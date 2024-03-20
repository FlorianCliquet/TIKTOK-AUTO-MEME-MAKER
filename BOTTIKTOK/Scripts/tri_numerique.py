import re

def tri_numerique(element,running):
    if running:
        def convertir(s):
            try:
                return int(s)
            except ValueError:
                return s

        def cle_tri(cle):
            return [convertir(c) for c in re.findall(r'\d+|\D+', cle)]

        return sorted(element, key=cle_tri)
    else:
        print("Arrêt du programme")
        raise SystemExit

