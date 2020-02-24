import tkinter as tk
import pandas as pd

filename = 'JueguizadorBD.csv'
default_text = """El camino del hombre recto está por todos lados rodeado por las injusticias de los egoístas y la tiranía de los
hombres malos. Bendito sea aquel pastor que, en nombre de la caridad y de la buena voluntad, saque a los 
débiles del Valle de la Oscuridad. Porque es el autentico guardián de su hermano y el descubridor de los 
niños perdidos. ¡Y os aseguro que vendré a castigar con gran venganza y furiosa cólera a aquéllos que 
pretendan envenenar y destruir a mis hermanos! ¡Y tú sabrás que mi nombre es Yahveh, cuando caiga mi venganza sobre ti!
"""

"""
AÑADIR BOTON REFRESH. DONE
AÑADIR HISTORICO (5 ULTIMOS). DONE
AÑADIR FILTRO TEMATICA
"""

class JueguizadorGUI():
    def __init__(self, verbose = False):
        self.verbose = verbose
        self.db = pd.read_csv(filename, encoding='latin-1', sep=';')
        self.lastentries = []

        self.window = tk.Tk()
        self.window.title('Jueguizador v3.0 FINAL')
        self.window.geometry('1000x370')

        self.upper_frame = tk.Frame(self.window, width=300, height=150)
        self.lower_frame = tk.Frame(self.window, width=300, height=250)

        self.window.grid_columnconfigure(1, weight=1)
        self.upper_frame.grid(row=0, column=0, sticky="nsew")
        self.lower_frame.grid(row=1, column=0, sticky="nsew")

        # textbox
        self.db_box_text = tk.Text(self.lower_frame, height=5, width=120, wrap=tk.NONE)
        self.db_box_text.grid(column=0, row=1)

        self.history_box_text = tk.Text(self.lower_frame, height=5, width=40, wrap=tk.WORD, font=('courier', 15, 'bold'))
        self.history_box_text.grid(column=0, row=0)
        
        self.title_box_text = tk.Text(self.lower_frame, height=2, width=40, wrap=tk.WORD, font=('courier', 15, 'bold'))
        self.title_box_text.grid(column=0, row=3)

        self.db_box_scrollbar = tk.Scrollbar(self.lower_frame, orient=tk.HORIZONTAL)
        self.db_box_scrollbar.grid(column=0, row=2, sticky=tk.N+tk.S+tk.E+tk.W)
        self.db_box_scrollbar.config(command=self.db_box_text.xview)
        self.db_box_text.config(xscrollcommand=self.db_box_scrollbar.set)

        # difficulty
        self.difficulty = tk.Entry(self.upper_frame, width=10)
        self.difficulty.grid(column=0, row=0, pady=5)
        # label
        self.difflbl = tk.Label(self.upper_frame, text="Dificultad")
        self.difflbl.grid(column=0, row=1)

        # time
        self.time = tk.Entry(self.upper_frame, width=10, text='Tiempo de juego')
        self.time.grid(column=1, row=0, pady=5)
        # label
        self.timelbl = tk.Label(self.upper_frame, text="Tiempo de juego")
        self.timelbl.grid(column=1, row=1)

        # players
        self.players = tk.Entry(self.upper_frame, width=10)
        self.players.grid(column=2, row=0, pady=5)
        # label
        self.plylbl = tk.Label(self.upper_frame, text="Jugadores")
        self.plylbl.grid(column=2, row=1)

        # set time
        self.settime = tk.Entry(self.upper_frame, width=10)
        self.settime.grid(column=3, row=0, pady=5)
        # label
        self.settimelbl = tk.Label(self.upper_frame, text="Tiempo de preparación")
        self.settimelbl.grid(column=3, row=1)

        # explanation time
        self.explanationtime = tk.Entry(self.upper_frame, width=10)
        self.explanationtime.grid(column=4, row=0, pady=5)
        # label
        self.expltimelbl = tk.Label(self.upper_frame, text='Tiempo de explicación')
        self.expltimelbl.grid(column=4, row=1)

        # opMode droplist and button
        coop = [
            "Sí",
            "No",
            "Indiferente"
        ]

        self.coopdroplist = tk.StringVar(self.lower_frame)
        self.coopdroplist.set(coop[2])  # default value

        w = tk.OptionMenu(self.upper_frame, self.coopdroplist, *coop)
        w.grid(column=5, row=0, padx=5)
        # label
        self.cooplbl = tk.Label(self.upper_frame, text='Cooperativo')
        self.cooplbl.grid(column=5, row=1)

        comp = [
            "Sí",
            "No",
            "Indiferente"
        ]

        self.compdroplist = tk.StringVar(self.lower_frame)
        self.compdroplist.set(comp[2])  # default value

        w = tk.OptionMenu(self.upper_frame, self.compdroplist, *comp)
        w.grid(column=6, row=0, padx=5)
        # label
        self.complbl = tk.Label(self.upper_frame, text='Competitivo')
        self.complbl.grid(column=6, row=1)

        exp = [
            "Sí",
            "No",
            "Indiferente"
        ]

        self.expdroplist = tk.StringVar(self.lower_frame)
        self.expdroplist.set(exp[2])  # default value

        w = tk.OptionMenu(self.upper_frame, self.expdroplist, *exp)
        w.grid(column=7, row=0, padx=5)
        # label
        self.explbl = tk.Label(self.upper_frame, text='Expansión')
        self.explbl.grid(column=7, row=1)

        # magic button
        self.magicbutton = tk.Button(self.upper_frame, text="¡A Jugar!", command=self.magic)
        self.magicbutton.grid(column=8, row=0, pady=10)

        # refresh button
        self.refreshbutton = tk.Button(self.upper_frame, text="Refrescar BD", command=self.refresh)
        self.refreshbutton.grid(column=9, row=0, pady=10)

        # clear button
        self.clearbutton = tk.Button(self.upper_frame, text="Limpiar", command=self.clean)
        self.clearbutton.grid(column=10, row=0, pady=10)

        self.window.mainloop()

    def refresh(self):
        self.db = pd.read_csv(filename, encoding='latin-1', sep=';')

    def clean(self):
        self.lastentries = []
        self.db_box_text.delete('1.0', tk.END)
        self.history_box_text.delete('1.0', tk.END)
        self.title_box_text.delete('1.0', tk.END)

    def magic(self):
        difficulty = self.difficulty.get()
        time = self.time.get()
        players = self.players.get()
        settime = self.settime.get()
        exptime = self.explanationtime.get()
        coop = self.coopdroplist.get()
        comp = self.compdroplist.get()
        exp = self.expdroplist.get()

        try:
            db_filtered = self.db[self.db['Dificultad'].astype(int) <= int(difficulty)]
        except ValueError:
            db_filtered = self.db
            if self.verbose:
                print("difficulty error")
                print(difficulty)
                print(self.db)

        try:
            db_filtered = db_filtered[db_filtered['Duración real'].astype(int) <= int(time)]
        except ValueError:
            try:
                db_filtered = db_filtered[db_filtered['Duración teórica'].astype(int) <= int(time)]
            except ValueError:
                pass
            if self.verbose:
                print("time error")
                print("time var: {}".format(time))
                print(db_filtered)
            pass

        try:
            db_filtered = db_filtered[db_filtered['Jugadores Min'].astype(int) <= int(players)]
        except ValueError:
            if self.verbose:
                print("players error")
                print(players)
                print(db_filtered)
            pass

        try:
            db_filtered = db_filtered[db_filtered['Tiempo de preparación'].astype(int) <= int(settime)]
        except ValueError:
            if self.verbose:
                print("settime error")
                print(settime)
                print(db_filtered)
            pass

        try:
            db_filtered = db_filtered[db_filtered['Tiempo de explicación'].astype(int) <= int(exptime)]
        except ValueError:
            if self.verbose:
                print("exptime error")
                print(exptime)
                print(db_filtered)
            pass

        if coop != 'Indiferente':
            try:
                db_filtered = db_filtered[db_filtered['Coop']  == coop]
                if self.verbose:
                    print(db_filtered)
            except ValueError:
                if self.verbose:
                    print("coop error")
                    print(coop)
                    print(db_filtered)
                pass

        if comp != 'Indiferente':
            try:
                db_filtered = db_filtered[db_filtered['Competitivo']  == comp]
                if self.verbose:
                    print(db_filtered)
            except ValueError:
                if self.verbose:
                    print("comp error")
                    print(comp)
                    print(db_filtered)
                pass

        if exp != 'Indiferente':
            try:
                db_filtered = db_filtered[db_filtered['Expansión']  == exp]
                if self.verbose:
                    print(db_filtered)
            except ValueError:
                if self.verbose:
                    print("exp error")
                    print(exp)
                    print(db_filtered)
                pass

        if db_filtered.empty:
            game = default_text
            title = ''
            #self.lastentries = self.lastentries[:-1]
        else:
            game = db_filtered.sample()
            title = game['Nombre'].values.tolist()[0]

            if len(self.lastentries) < 5:
                #self.lastentries = self.lastentries[1:]
                self.lastentries.append(title)

        self.db_box_text.delete('1.0', tk.END)
        self.history_box_text.delete('1.0', tk.END)
        self.title_box_text.delete('1.0', tk.END)

        #print(self.db)
        #print(db_filtered)

        if self.verbose:
            print(self.lastentries)

        if type(game) != str:
            self.db_box_text.insert(tk.END, game.to_string())
        else:
            self.db_box_text.insert(tk.END, game)

        #self.history_box_text.insert(tk.END, title)
        s = ''.join([str(i + 1) + ' ' + self.lastentries[i] + '\n' for i in range(0, len(self.lastentries))])
        self.history_box_text.insert(tk.END, s)

        self.title_box_text.insert(tk.END, title)

JueguizadorGUI()
