---

🚀 DDoS Attack Script - HACKER2108

⚠️ Avertissement

> Ce script est uniquement destiné à des fins éducatives et de test sur des environnements contrôlés (comme des machines virtuelles ou des réseaux locaux). L'utilisation de ce script pour attaquer des systèmes sans autorisation est illégale et peut entraîner des poursuites judiciaires.




---

📌 Description

Ce script Python permet de simuler une attaque par DDoS (Distributed Denial of Service) en envoyant des paquets UDP de manière continue vers une cible (IP ou domaine) sur un ou plusieurs ports.


---

🔥 Fonctionnalités

Résolution automatique des domaines en IP.

Attaque simultanée sur plusieurs ports (plage de ports prise en charge).

Affiche la progression et le nombre de paquets envoyés.

Peut être arrêté proprement avec CTRL + C.

Bannières stylées avec Figlet.



---

⚙️ Prérequis

Installe les outils nécessaires sous Termux :

pkg update -y && pkg upgrade -y
pkg install python -y
pkg install figlet -y
pip install socket requests


---

🚀 Utilisation

1. Clone le repo ou crée un fichier :



nano ddos_attack.py

2. Colle le script dans le fichier.


3. Exécute le script :



python ddos_attack.py


---

🛠️ Options

Target : IP ou domaine de la cible.

Port(s) : Port unique (ex : 80) ou plage (ex : 80-443).

Interruption : Utilise CTRL + C pour stopper proprement l’attaque.



---

⚠️ Avertissement légal

N’utilise jamais ce script sur un système sans autorisation. Il est destiné uniquement à des fins d’apprentissage. Toute utilisation malveillante est sous ta responsabilité.


---

🛡️ Auteur

👤 HACKER2108
📌 Projet éducatif pour comprendre les attaques DDoS et la gestion des paquets réseau en Python.


---

✅ Ce README est clair, structuré et met en avant la légalité et les instructions d'utilisation.

