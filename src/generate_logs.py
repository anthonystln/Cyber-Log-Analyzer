import random
import time
from datetime import datetime, timedelta

# Configuration
LOG_FILE = "../data/server.log"
NUM_LINES = 5000  # On va générer 5000 lignes de logs

# Fausses données
IPS = {
    "normal": ["192.168.1.10", "192.168.1.11", "10.0.0.5"],
    "suspect": ["45.33.22.11", "185.22.33.44", "203.0.113.5"]  # IPs "étrangères"
}
USERS = ["alice", "bob", "charlie", "admin", "root"]
ACTIONS = ["LOGIN_SUCCESS", "LOGIN_FAILED", "LOGOUT", "PAGE_VIEW", "DOWNLOAD"]

def generate():
    print(f"🔨 Génération de {NUM_LINES} lignes de logs dans {LOG_FILE}...")
    
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        current_time = datetime.now() - timedelta(days=1)
        
        for _ in range(NUM_LINES):
            # On avance le temps aléatoirement
            current_time += timedelta(seconds=random.randint(1, 60))
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            
            # Scénario : 5% de chance d'attaque massive (Brute Force)
            if random.random() < 0.05:
                ip = random.choice(IPS["suspect"])
                user = "admin"
                action = "LOGIN_FAILED"
                # Une attaque c'est plein de tentatives rapides !
                for _ in range(random.randint(5, 20)):
                    f.write(f"{timestamp} | {ip} | {user} | {action}\n")
            else:
                # Comportement normal
                ip = random.choice(IPS["normal"] + IPS["suspect"])
                user = random.choice(USERS)
                action = random.choice(ACTIONS)
                f.write(f"{timestamp} | {ip} | {user} | {action}\n")
    
    print("✅ Terminé ! Fichier généré.")

if __name__ == "__main__":
    generate()