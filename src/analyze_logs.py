from collections import Counter

LOG_FILE = "../data/server.log"

def analyser():
    print("Analyse du fichier en cours...")

    # Ce dictionnaire servira à compter les échecs par IP
    # Ex: {"192.168.1.1": 2, "45.33.22.11": 500}
    compteur_echecs = Counter()

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            # 1. Nettoyage (on enlève le saut de ligne \n à la fin)
            line = line.strip()

            # 2. Découpage (Split)
            parts = line.split(" | ")

            # Sécurité : on vérifie qu'on a bien 4 morceaux pour éviter les bugs
            if len(parts) == 4:
                ip = parts[1]
                action = parts[3]

                # --- À TOI DE CODER ICI ---
                # Si l'action est "LOGIN_FAILED"...
                # Alors on ajoute +1 au compteur pour cette IP
                # Indice : compteur_echecs[ip] += 1
                if action == "LOGIN_FAILED":
                    compteur_echecs[ip] += 1
    
    # 3. Résultats
    print("Bilan des attaques :")
    # La méthode .most_common(1) donne le top 1
    top_hacker = compteur_echecs.most_common(1)

    if top_hacker:
        ip_suspecte, nb_echecs = top_hacker[0]
        print(f"ALERT : IP {ip_suspecte} a échoué {nb_echecs} fois !")
        return ip_suspecte
    else:
        print("Rien à signaler.")
        return None

def generer_rapport(ip_suspecte):
    print(f"Création du rapport pour {ip_suspecte}")

    source = "../data/server.log"
    destination = "../reports/rapport_suspects.csv"

    with open(source, "r", encoding="utf-8") as f_in, open(destination, "w", encoding="utf-8") as f_out:

        # 1. Écrire l'en-tête du CSV (Colonnes)
        f_out.write("Date,IP,Utilisateur,Action\n")

        # 2. Parcourir le fichier source
        for line in f_in:
            line = line.strip()
            parts = line.split(" | ")

            if len(parts) == 4:
                ip_log = parts[1]

                # --- À TOI DE CODER ICI ---
                # Si l'IP de la ligne correspond à l'IP suspecte...
                # Alors on reformate la ligne avec des virgules
                # Et on l'écrit dans f_out
                # Indice : f_out.write(f"{parts[0]},{parts[1]}... \n")
                if ip_log == ip_suspecte:
                    # new_line = line.replace('|', ',')
                    # print(new_line)
                    f_out.write(f"{parts[0]},{parts[1]},{parts[2]},{parts[3]}\n")


# --- Le Chef d'Orchestre ---
if __name__ == "__main__":
    # 1. On trouve le coupable
    ip_coupable = analyser()

    # 2. Si on a trouvé quelqu'un, on sort son dossier
    if ip_coupable:
        generer_rapport(ip_coupable)