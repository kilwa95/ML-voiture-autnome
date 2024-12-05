# Taxi Game Simulation

Ce projet simule un jeu de taxi où le but est de transporter un client d'un point de départ à une destination en évitant les obstacles. Le jeu est basé sur l'environnement `Taxi-v3` de Gym.

## Description du jeu

Le taxi débute à une position aléatoire. Son but est d'aller chercher un client situé dans un des carrés de couleur et de l'amener à sa destination représentée par un bâtiment et qui se trouve sur un autre carré coloré. Une partie est terminée lorsque le client a été déposé quelque part. Les zones végétales représentent des zones que le taxi ne peut pas traverser donc il ne peut rouler que sur le bitume.

## State

Un état est défini par un tuple contenant 4 éléments:
- taxi_row
- taxi_col
- client_location
- destination

### State space

Il existe 500 états distincts dans cet environnement.
25 positions taxi * 5 positions client (carrés + dans taxi) * 4 destinations

## Actions

Il y a 6 actions possibles pour le taxi:
- 0 = aller vers le sud
- 1 = aller vers le nord
- 2 = aller vers l'est
- 3 = aller vers l'ouest
- 4 = faire monter le passager dans le taxi
- 5 = faire descendre le passager du taxi

## Rewards

Le système de récompenses est pré-implémenté de la manière suivante:
- Déplacement = -1  -> un déplacement entraîne toujours une pénalité pour encourager le taxi à prendre le chemin le plus court
- Faire descendre le passager au mauvais endroit = -10
- Faire descendre le passager au bon endroit = +20

## Installation

Pour exécuter ce projet, vous devez avoir Python installé sur votre machine. Vous pouvez installer les dépendances nécessaires en utilisant le fichier `requirements.txt` : 

```bash
pip install -r requirements.txt
```

## Exécution

Pour exécuter le script, utilisez la commande suivante :

```bash
python main.py
```


