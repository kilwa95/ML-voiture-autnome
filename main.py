# %%
# ============================================================================= 
# Imports
# =============================================================================

import matplotlib.pyplot as plt
import random
from matplotlib import animation
import gym

# %%
# =============================================================================
# Création de l'environnement
# =============================================================================
env = gym.make("Taxi-v3", render_mode = "rgb_array").env # création d'une instance du jeu
state, _ = env.reset() # initialisation du state de départ

# Action aléatoire
action = env.action_space.sample(env.action_mask(state)) # choix d'une action aléatoire
next_state, reward, done, _, _= env.step(action) # exécution de l'action

# Plot de l'environnement
frame = env.render() # capture d'une image de l'environnement
plt.imshow(frame) # affichage de l'image
plt.axis('off') # suppression des axes
plt.show() # affichage de l'image


# %%
# =============================================================================
# Taxi autonome avant apprentissage       
# =============================================================================

from IPython import display
from time import sleep

fig, ax = plt.subplots() # création d'une figure et d'un axe
fig.set_size_inches(8,5) # définition de la taille de la figure
frame = env.render() # capture d'une image de l'environnement
show_frame = ax.imshow(frame) # affichage de l'image

for run in range(1,6): # boucle sur les 5 runs
    state, _ = env.reset()  # réinitialisation du state de départ
    n_iters = 0 # initialisation du nombre d'itérations
    done = False # initialisation de la condition de fin de partie
    while not done and n_iters < 21: # boucle sur les itérations
        action = env.action_space.sample(env.action_mask(state)) # choix d'une action aléatoire
        next_state, reward, done, _, _= env.step(action) # exécution de l'action
        state = next_state # mise à jour du state
        display.clear_output(wait = True) # nettoyage de la sortie
        display.display(plt.gcf()) # affichage de la figure
        frame = env.render() # capture d'une image de l'environnement
        show_frame.set_data(frame) # mise à jour de l'image affichée
        ax.axis("off") # suppression des axes
        ax.set_title(f"Partie n°{run} | itération n°{n_iters}") # titre de la figure
        sleep(0.1) # met en pause l'exécution du script
        n_iters += 1 # incrément du nombre d'itérations
    sleep(0.1) # pause de 1 seconde
plt.show() # fermeture de la figure


    

# %%
# =============================================================================
# Taxi autonome pendant l'apprentissage
# =============================================================================
import numpy as np

q_table = np.zeros((env.observation_space.n, env.action_space.n)) # initialisation de la table Q
alpha = 0.1 # taux d'apprentissage
gamma = 0.6 # facteur de discount
eps = 0.1 # taux d'exploration
training_runs = 10000 # nombre de runs d'apprentissage

for taxi_run in range(training_runs): # boucle sur les runs d'apprentissage
    state, _ = env.reset() # réinitialisation du state de départ    
    done = False # initialisation de la condition de fin de partie
    while not done: # boucle sur les itérations
        if (random.random() < eps): # exploration 
            action = env.action_space.sample(env.action_mask(state)) # choix d'une action aléatoire
        else: # exploitation
            action = np.argmax(q_table[state]) # choix de l'action avec la valeur Q la plus élevée
        next_state, reward, done, _, _ = env.step(action) # exécution de l'action
        prev_q = q_table[state, action] # valeur Q précédente
        next_max_q = np.max(q_table[next_state]) # valeur Q maximale pour le next state
        new_q = prev_q + alpha * (reward + gamma * next_max_q - prev_q) # mise à jour de la valeur Q
        q_table[state, action] = new_q # mise à jour de la valeur Q
        state = next_state # mise à jour du state

        

# %%
# =============================================================================
# Taxi autonome après apprentissage
# =============================================================================
from IPython import display
from time import sleep

fig, ax = plt.subplots()
fig.set_size_inches(8,5)

frame = env.render() # capture d'une image de l'environnement
show_frame = ax.imshow(frame) # affichage de l'image

for run in range(1,11): # boucle sur les 10 runs
    state, _ = env.reset() # réinitialisation du state de départ
    n_iter = 0 # initialisation du nombre d'itérations
    done = False # initialisation de la condition de fin de partie

    while not done and n_iter < 36: # boucle sur les itérations

        action = np.argmax(q_table[state])
        next_state, reward, done, _, _ = env.step(action) # exécution de l'action
        state = next_state # mise à jour du state

        display.clear_output(wait = True) # permet d'effacer l'ancien plot dès qu'une nouvelle donnée est dispo
        display.display(plt.gcf()) # permet de sélectionner l'objet figure existant

        frame = env.render()
        show_frame.set_data(frame) # on met à jour les données du plot
        ax.axis("off")
        ax.set_title(f"Partie n°{run} | itération n°{n_iter}")
        sleep(0.1) # met en pause l'exécution du script

        n_iter += 1
    sleep(0.1)
plt.show()

# %%
