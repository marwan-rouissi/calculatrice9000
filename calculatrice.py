from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

### Fenêtre de la calculatrice

root = Tk()
root.title("Calculatrice")
root.geometry("480x400")
root.resizable(False, False)


### les fonctions 

# permet d'afficher les touches numériques 0-9 ansi que la decimale "."
def insert_num(num):
    if Affichage_var.get() == "0" or Affichage_var.get() == "Erreur":
        clear()
        Affichage.insert(END, num)
    else:
        Affichage.insert(END, num)

# permet d'afficher les opérateurs de base
def insert_op(op):
    txt = Affichage.get()
    if txt == "Erreur":
        messagebox.showerror(title="ERREUR", message="Opération invalide. Veuillez entrer une valeur avant d'utiliser un opérateur.")
        Affichage.delete(0,op)
    if txt =="":
        messagebox.showerror(title="ERREUR", message="Veuillez entrer une valeur avant d'utiliser un opérateur.")
        Affichage.delete(0,op)
    if txt[-1] == "+" or txt[-1] == "-" or txt[-1] == "*" or txt[-1] == "/":
        messagebox.showerror(title="ERREUR", message="Ces opérateurs ne sont pas compatibles l'un à la suite de l'autre.")
    else:
        Affichage.insert(END, op)

# permet d'afficher la décimale
def insert_point():
    txt = Affichage.get()
    if txt[-1] == ".":
            messagebox.showwarning(title="Attention", message="La décimale a déjà été selectionnée.")
            clear()
            Affichage.insert(END, ".")
    else:
        Affichage.insert(END, ".")

# permet de switch la valeur souhaitée en négative ou positive
def p_n():
    txt = Affichage_var.get()
    if txt != "0":
        if txt[0] != "-":
            Affichage.insert(0, "-")
        else:
            Affichage.delete(0,1)

# permet de donner le carré
def carre():
    total = float(Affichage_var.get())
    Affichage_var.set(total*total)

# permet de donner la racine carré
def r_carre():
    total = float(Affichage_var.get())
    Affichage_var.set(pow(total, 0.5))
    
#permet de donner la valeur de pi
def pi():
    p = 3.14159
    Affichage_var.set(p)

# permet d'effacer seuleuement la dernière valeur
def effacer():
    Affichage.delete(len(Affichage.get())-1)

#permet d'effacer entièrement la zone d'affichage
def clear():
    Affichage.delete(0,END)

# permet d'avoir le %
def percent():
    txt = float(Affichage.get())
    total = txt/100
    Affichage_var.set(total)

# permet d'afficher le resultat de l'opération souhaitée mais également de le stocker dans un ficher txt (aka l'historique)
def egal():
        try:
            txt = Affichage.get()
            total = str(eval(txt))
            fichier = open("Historique.txt", "a")
            fichier.write(txt)
            fichier.write("\n")
            fichier.write("=" + total)
            fichier.write("\n")
            fichier.close()
            Affichage_var.set(total)
        except:
            clear()
            Affichage_var.set("Erreur")

# permet d'ouvrir l'historique sous forme d'une nouvelle fenêtre 
def open_history():
    history = Toplevel()
    history.title("Historique")
    global history_label
    history_label = Label(history,text="Pas d'historique.", font=("arial",15))
    history_label.grid(row=1)
    history.geometry("300x300")
    clear_history_btn = ttk.Button(history, text="Effacer", command=clear_history)
    clear_history_btn.grid(row=0, column=0, pady=5)
    close_btn = ttk.Button(history, text="Fermer", command=history.destroy)
    close_btn.grid(row=0, column=1)
    file= open("Historique.txt",'r')
    txt= file.read()
    history_label.config(text=txt, font=("arial",15))
    file.close()
    history.mainloop()

# permet d'effacer le contenu de l'historique    
def clear_history():
    f = open("historique.txt","w")
    f.close()
    # Actualiser l'historique après avoir effacé 
    history_label.config(text="", font=("arial",15))

# permet de supprimer le fichier "historique.txt"
def delete_history():
    os.remove("historique.txt")


### l'interface graphique

# Zone Affichage
calculatrice = ttk.Frame(root)
calculatrice.grid(row=0, column=0, pady=20)
Affichage_var = StringVar()
Affichage_var.set("0")
Affichage = ttk.Entry(calculatrice, font= 10, justify=RIGHT, textvariable=Affichage_var)
Affichage.grid(ipadx=127, ipady=16)

# Touches
touches = ttk.Frame(root)
touches.grid(row=2, sticky="w")

# Opérateurs scientifique
r_carree_btn = ttk.Button(touches, text="√", command=r_carre).grid(row=0, column=0, ipadx=10, ipady=10)
carree_btn = ttk.Button(touches, text="²", command=carre).grid(row=0, column=1, ipadx=10, ipady=10)
pourcentage_btn = ttk.Button(touches, text="%", command=percent).grid(row=2, column=4, ipadx=10, ipady=10)
pi_btn = ttk.Button(touches, text="π", command=pi).grid(row=3, column=4, ipadx=10, ipady=10)

# Pad numérique
touche_7_btn = ttk.Button(touches, text="7", command=lambda: insert_num(7)).grid(row=1, column=0, ipadx=10, ipady=10)
touche_8_btn = ttk.Button(touches, text="8", command=lambda: insert_num(8)).grid(row=1, column=1, ipadx=10, ipady=10)
touche_9_btn = ttk.Button(touches, text="9", command=lambda: insert_num(9)).grid(row=1, column=2, ipadx=10, ipady=10)
touche_4_btn = ttk.Button(touches, text="4", command=lambda: insert_num(4)).grid(row=2, column=0, ipadx=10, ipady=10)
touche_5_btn = ttk.Button(touches, text="5", command=lambda: insert_num(5)).grid(row=2, column=1, ipadx=10, ipady=10)
touche_6_btn = ttk.Button(touches, text="6", command=lambda: insert_num(6)).grid(row=2, column=2, ipadx=10, ipady=10)
touche_1_btn = ttk.Button(touches, text="1", command=lambda: insert_num(1)).grid(row=3, column=0, ipadx=10, ipady=10)
touche_2_btn = ttk.Button(touches, text="2", command=lambda: insert_num(2)).grid(row=3, column=1, ipadx=10, ipady=10)
touche_3_btn = ttk.Button(touches, text="3", command=lambda: insert_num(3)).grid(row=3, column=2, ipadx=10, ipady=10)
touche_0_btn = ttk.Button(touches, text="0", command=lambda: insert_num(0)).grid(row=4, column=1, ipadx=10, ipady=10)
# Point pour décimales
point_btn = ttk.Button(touches, text=',', command=insert_point).grid(row=4, column=2, ipadx=10, ipady=10)
# Valeur +/-
p_n_btn = ttk.Button(touches, text="+/-", command=p_n).grid(row=4, column=0, ipadx=10, ipady=10)
#parenthèses
p_ouvrante_btn = ttk.Button(touches, text="(", command=lambda:insert_num("(")).grid(row=0, column=2, ipadx=10, ipady=10)
p_fermante_btn = ttk.Button(touches, text=")", command=lambda:insert_num(")")).grid(row=0, column=3, ipadx=10, ipady=10)

# Opérateurs de base
add_btn = ttk.Button(touches, text="+", command=lambda: insert_op("+")).grid(row=1, column=3, ipadx=10, ipady=10)
soustra_btn = ttk.Button(touches, text="-", command=lambda: insert_op("-")).grid(row=2, column=3, ipadx=10, ipady=10)
multi_btn = ttk.Button(touches, text="x", command=lambda: insert_op("*")).grid(row=3, column=3, ipadx=10, ipady=10)
div_btn = ttk.Button(touches, text="÷", command=lambda: insert_op("/")).grid(row=4, column=3, ipadx=10, ipady=10)
# Egal
egal_btn = ttk.Button(touches, text="=", command=egal).grid(row=4, column=4, ipadx=10, ipady=10)

# Effacer la dernière entrée
effacer_btn = ttk.Button(touches, text="⇐", command=effacer).grid(row=0, column=4, ipadx=10, ipady=10)
# Effacer l'intégralité des elements de la zone d'affichage
C_btn = ttk.Button(touches, text="C", command=clear).grid(row=1, column=4, ipadx=10, ipady=10)

#Historique
history_btn = ttk.Button(touches, text="Historique", command=open_history).grid(row=5, column=0, pady=20)
delete_btn = ttk.Button(touches, text="Supprimer", command=delete_history).grid(row=5, column=1, pady=20)

root.mainloop()