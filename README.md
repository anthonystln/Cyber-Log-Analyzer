# 🛡️ Cyber Log Analyzer

Ce projet est un outil d'analyse forensique automatisé développé en Python.
Il simule des logs serveurs, détecte des attaques par force brute et génère des rapports d'incidents (CSV).

## 📂 Structure du projet
- `src/generate_logs.py` : Génère de fausses données de logs pour simuler une activité serveur (utilisateurs légitimes + attaquants).
- `src/analyze_logs.py` : Analyse le fichier de logs, identifie l'IP réalisant une attaque par force brute et extrait ses actions.
- `reports/` : Dossier contenant les rapports d'extraction au format CSV (preuves).
- `data/` : Dossier contenant les logs bruts (générés par le script).

## 🚀 Comment lancer le projet

### 1. Prérequis
- Python 3.x installé.
- Aucune librairie tierce requise (utilise uniquement la librairie standard).

### 2. Installation
Clonez ce dépôt :
```bash
git clone [https://github.com/anthonystln/Cyber-Log-Analyzer.git](https://github.com/anthonystln/Cyber-Log-Analyzer.git)
cd Cyber-Log-Analyzer
```

### 3. Utilisation
Étape A : Générer les données Lancez le script de génération pour créer un faux fichier de logs (server.log) :
```bash
python3 src/generate_logs.py
```

Étape B : Lancer l'analyse Lancez le script d'analyse pour détecter le pirate et générer le rapport :
```bash
python3 src/analyze_logs.py
```

Le script affichera l'IP suspecte dans le terminal et créera un fichier rapport_suspects.csv dans le dossier reports/.

## 🛠️ Stack Technique

- Langage : Python 3
- Concepts : Manipulation de fichiers (I/O), Traitement de chaînes (String Manipulation), Dictionnaires, Automatisation.
- Format de sortie : CSV (Comma Separated Values).