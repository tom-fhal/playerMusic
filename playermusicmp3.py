from tkinter import *
import tkinter as tk
from tkmacosx import Button
#essentiel pour l'import de couleur de fond d'écran de bouton sur mac 
import pygame
from tkinter.filedialog import askdirectory
from tkinter import filedialog
import os
from pygame import mixer
import tkinter as tkr
from tkinter.filedialog import askopenfilename
#création de la fenêtre du player music
fenetreplayer = tk.Tk()
fenetreplayer.title('Playerlaplateforme')
fenetreplayer.geometry("700x700")
pygame.init()
pygame.mixer.init()
#création de la frame principale
princframe = tk.Frame(fenetreplayer)
princframe.pack(fill='both', expand=True, pady=20, padx=20)
princframe.configure(bg="white")



#fonctionnalités attribuées aux boutons,echelle... 
def supprimermusique():
    musiquechoisie = Lb1.curselection()

    if musiquechoisie:
        Lb1.delete(musiquechoisie)
        if not Lb1.size():
            Label(Lb1, text="Ajouter une musique à votre playlist !", font=('TkheadingFont, 20')).place(x=180,y=50)
    pygame.mixer.music.stop()
    
def volumemusique(x):
    pygame.mixer.music.set_volume(echelvol.get())

def ajouter():
    global nomfichier
    #ouverture du fichier 
    nomfichier=filedialog.askopenfilenames(title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    #boucle sur chaque élément de la liste à insérer dans la boîte de liste
    for m in nomfichier:
        Lb1.insert(END,m)

def recommencer():
    pygame.mixer.music.play(-1)

def jouermusique():  
    music = Lb1.get(tk.ACTIVE)
    music = f'/Users/murdockclifford/Desktop/mp3python/{music}'
    pygame.mixer.music.load(music)
    pygame.mixer.music.play()

is_paused = False

def pausemusique(): 
    global is_paused
    if is_paused:
        pygame.mixer.music.pause()
        is_paused=False
    else:
        pygame.mixer.music.unpause()
        is_paused=True
    
def stop():
    pygame.mixer.music.stop()


#Imports des images nécessaires 


#Création des widgets

boutonajouter = Button(princframe,text = "Ajouter",fg = 'red',bg = 'blue',
                      command=lambda: ajouter())
boutonajouter.place(x=300, y=400)
boutonpause = Button(princframe,fg = 'red',bg = 'blue',text = "Pause",
                      command=lambda: pausemusique())
boutonpause.place(x=300, y=300)
boutonjouer = Button(princframe,text = "Jouer",fg = 'red',bg = 'blue',
                      command=jouermusique)
boutonjouer.place(x=505, y=400)
boutonstop = Button(princframe,fg = 'red',bg = 'blue',text="Stop",
                      command=lambda: stop())
boutonstop.place(x=505, y=300)

boutonrecommencer = Button(princframe,text = "Recommencer",fg = 'red',bg = 'blue',
                      command=lambda: recommencer())
boutonrecommencer.place(x=15, y=400)
boutonsupprimer = Button(princframe,text="Suprrimer",fg = 'red',bg = 'blue',
                      command= supprimermusique)
boutonsupprimer.place(x=15, y=300)

echelvol = Scale(princframe, from_=0,to=1,orient = HORIZONTAL ,
    resolution = .1,length=600,label="Volume",command=volumemusique)
echelvol.place(x=15, y=540)
echelvol.set(1)

#creation d'une listbox qui liste des musiques 
Lb1 = Listbox(princframe,font=30,bg="black",fg="white",selectmode=tkr.SINGLE,)
Lb1.grid(ipadx=600, ipady=1)

fenetreplayer.mainloop()
