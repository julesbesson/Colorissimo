import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from platform import system

if system() == 'Darwin':
    from tkmacosx import Button as Buttonx
else:
    Buttonx = tk.Button

liste_nom_couleurs = np.array(['magenta','écarlate','rouge','orange','jaune','citron','vert','turquoise','cyan','indigo','bleu','pourpre'])
liste_couleurs = np.array(['magenta','crimson','orangered','orange','yellow','greenyellow','limegreen','aquamarine','darkturquoise','royalblue','blue','darkviolet'])

class ColorTest :
    def __init__(self, win, color_list = liste_couleurs, color_name_list = liste_nom_couleurs, rows = 12, columns = 8, withdraw_number = 4, title = 'Connerissimo', bg_color = '#26242F') :
        # La fenêtre
        self.win = win
        self.win.title(title)

        # Les int
        self.color_number = len(color_list)
        if rows * columns % self.color_number != 0:
            print('Problème de dimensions')
        self.nbc = rows * columns //self.color_number
        self.rows = rows
        self.columns = columns
        self.withdraw_number = withdraw_number

        # Les bool
        self.grid_validity = False

        # Les string
        self.bg_color = bg_color

        # Les arrays

        self.color_list = color_list
        self.color_name_list = color_name_list
        self.color_grid = self.random_grid()
        self.check_grid = np.zeros((self.rows, self.columns), dtype = bool)
        self.row_validity = np.zeros(self.rows,dtype = bool)
        self.color_count = self.nbc*np.ones(shape = self.color_number,dtype = int)
        self.buttons = np.empty((self.rows,self.columns), dtype = object)

        # Les boutons
        self.valider = tk.Button(self.win)
        #tk.Button(self.win,command = self.validation_process,text='validay').grid(row=self.rows - 2,column=self.columns)
        self.reinit = tk.Button(self.win)
        for i in range(self.rows):
            for j in range(self.columns):
                self.buttons[i,j] = Buttonx(self.win)

        # Les fonctions à lancer
        self.button_init()
        self.win.config(bg = self.bg_color)

    # Fonctions pour le test

    def random_grid (self):
        """Renvoie un mélange aléatoire des couleurs avec un nombre d'exemplaires égal pour chacune"""
        return np.random.choice(a = np.array([i % self.color_number for i in range(self.rows * self.columns)]), size = (self.rows, self.columns), replace = False)

    def button_init(self) :
        """Ordonne et crée les boutons de la grille, donne les paramètres aux autres."""
        self.win.geometry(str(2*110 + 100*self.columns) + 'x' + str(self.rows*100))
        for i in range(self.rows):
            for j in range(self.columns):
                self.buttons[i,j] = Buttonx(self.win)
                if j == 0:
                    self.buttons[i,j].grid(row=i, column=j,padx = (110,0))
                else:
                    self.buttons[i,j].grid(row=i, column=j)
                self.buttons[i,j].configure(highlightbackground = "#26242F", bg = self.color_list[self.color_grid[i,j]], width=100, height=70, command = lambda c=i , d=j: self.grid_button_command(c,d))

        self.valider.grid(row = self.rows-1 , column= self.columns)
        self.reinit.grid(row = 0 , column= self.columns)

        self.valider.configure(highlightbackground = self.bg_color,state = tk.DISABLED, command = self.validation_process,text = 'Valider')
        self.reinit.configure(highlightbackground= self.bg_color,command = self.button_reinit,text = 'Réinitialiser')

    def button_reinit (self):
        """Recommence le mélange et replace les boutons"""

        self.color_grid = np.random.randint(0,self.color_number, size = (self.rows,self.columns))
        self.check_grid = np.zeros((self.rows, self.columns), dtype = bool)
        self.row_validity = np.zeros(self.rows,dtype = bool)
        self.color_count = self.nbc*np.ones(shape = self.color_number,dtype = int)

        self.valider.configure(state = tk.DISABLED)

        for i in range(self.rows):
            for j in range(self.columns):
                self.buttons[i,j].configure(bg = self.color_list[self.color_grid[i,j]])

    def grid_button_command (self,i,j):
        """Action enclenchée lorsque l'on clique sur un des boutons de la grille"""

        if self.check_grid[i,j]: # Si la case est grisée, on la dégrise
            self.buttons[i,j].configure(bg = self.color_list[self.color_grid[i,j]])
            self.check_grid[i,j] = False
            self.color_count[self.color_grid[i,j]] += 1
            self.row_validation(i)

        elif self.row_validity[i]: # Si elle n'est pas cochée, mais qu'il y en a déjà nb_exclusions de grisées, on affiche un message d'erreur
            print("Il y a déjà "+str(self.withdraw_number)+" cases grisées")

        else: # Sinon on la grise
            self.buttons[i,j].configure(bg = 'grey')
            self.check_grid[i,j] = True
            self.color_count[self.color_grid[i,j]] -= 1
            self.row_validation(i)

    def row_validation (self,i):
        """Mise à jour de l'état de validité de la ligne i"""

        if sum(self.check_grid[i]) == self.withdraw_number:
            self.row_validity[i] = True
        else:
            self.row_validity[i] = False
        self.grid_validation()

    def grid_validation (self):
        """Mise à jour de l'état de validité de la grille"""
        if all(self.row_validity):
            self.valider.configure(state = tk.NORMAL)

    def validation_process(self):
        """Quand on clique sur valider, cela lance un plot et un histogramme"""
        fig = plt.figure(figsize = (12,7), num = 'Histogramme des couleurs gardées')
        plt.subplots_adjust(left=0.03, right=0.98,top = 0.97,bottom = 0.05)
        ax=plt.axes()
        ax.set_facecolor(self.bg_color)
        plt.bar(range(self.color_number), self.color_count, color = self.color_list)
        plt.xticks(range(self.color_number), self.color_name_list)
        plt.show()

    def disparition(self) :
        # on fait disparaître l'objet lab de type Label
        self.lab.grid_forget()


if __name__ == "__main__" :
    root = tk.Tk()
    f = ColorTest(root)
    root.mainloop()