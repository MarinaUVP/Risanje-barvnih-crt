from tkinter import *
from tkinter.colorchooser import *

class Crta():
    def __init__(self, master):


        menu = Menu(master)
        master.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Open", command = self.odpri)
        file_menu.add_command(label="Save", command = self.shrani)



        label_barva = Label(master, text = "Izberi barvo")
        label_barva.grid(row=0, column=0, columnspan = 2)

        gumb_rumena = Button(master, bg = "yellow", command = self.rumena,
                             width = 6, height = 2)
        gumb_rumena.grid(row = 1, column = 0)

        gumb_rdeca = Button(master, bg = "red", command = self.rdeca,
                            width = 6, height = 2)
        gumb_rdeca.grid(row = 2, column = 0)

        gumb_zelena = Button(master, bg = "green", command = self.zelena,
                             width = 6, height = 2)
        gumb_zelena.grid(row = 3, column = 0)

        gumb_modra = Button(master, bg = "blue", command = self.modra,
                             width = 6, height = 2)
        gumb_modra.grid(row = 1, column = 1)

        gumb_crna = Button(master, bg = "black", command = self.crna,
                             width = 6, height = 2)
        gumb_crna.grid(row = 2, column = 1)

        gumb_bela = Button(master, bg = "white", command = self.bela,
                             width = 6, height = 2)
        gumb_bela.grid(row = 3, column = 1)

        gumb_vec_barv = Button(master, command = self.vec_barv, text = 'Več barv')
        gumb_vec_barv.grid(row = 4, column = 0, columnspan = 2)
        



        label_nastavitev = Label(master, text = "Nastavi debelino")
        label_nastavitev.grid(row=0, column=3)

        self.debelina = 3

        gumb_povecaj = Button(master, command = self.povecaj, text = "+",
                              width = 6, height = 2)
        gumb_povecaj.grid(row = 1, column = 3)

        gumb_zmanjsaj = Button(master, command = self.zmanjsaj, text = "-",
                               width = 6, height = 2)
        gumb_zmanjsaj.grid(row = 3, column = 3)
        
        self.napis_debelina = StringVar(value=str(self.debelina))
        label_debelina = Label(master, textvariable=self.napis_debelina)
        label_debelina.grid(row=2, column=3)



        self.canvas = Canvas(master, width=800, height=450, bg = "white")
        self.canvas.grid(row = 5, column = 0, columnspan = 4)

        self.tocka = None

        self.canvas.bind("<Button-1>", self.zacni_crto
                         )

        self.canvas.bind("<B1-Motion>", self.nadaljuj_crto)

        self.barva = "black"

        
        label_opomba = Label(master, text = "Če miško premikaš dovolj počasi, boš dobil sklenjeno črto")
        label_opomba.grid(row=6, column=0, columnspan = 4)


    def kodiraj(self, id):
        coords = [int(i) for i in self.canvas.coords(id)]
        lastnosti = {}
        lastnosti["fill"] = self.canvas.itemcget(id, "fill")
        lastnosti["outline"] = self.canvas.itemcget(id, "outline")
        return(coords, lastnosti)


       

    def odpri(self):
        ime = filedialog.askopenfilename()
        if ime == "":
            return
        with open(ime, encoding="utf8") as f:
            self.canvas.delete(ALL)
            for v in f:
                v = v.split(',')
                v = [e.strip() for e in v]
                self.canvas.create_oval(v[0], v[1], v[2], v[3], fill = v[4], outline = v[5])



    def shrani(self):
        ime = filedialog.asksaveasfilename()
        if ime == "":
            return
        with open(ime, "wt", encoding = "utf8") as f:
            for id in self.canvas.find_all():
                coords = [int(i) for i in self.canvas.coords(id)]
                lastnosti = (self.canvas.itemcget(id, "fill"), self.canvas.itemcget(id, "outline"))
                f.write("{0}, {1}, {2}, {3}, {4}, {5}\n".format(coords[0], coords[1], coords[2], coords[3], lastnosti[0], lastnosti[1]))



    def rumena(self):
        self.barva = "yellow"

    def rdeca(self):
        self.barva = "red"

    def zelena(self):
        self.barva = "green"

    def modra(self):
        self.barva = "blue"

    def crna(self):
        self.barva = "black"

    def bela(self):
        self.barva = "white"

    def vec_barv(self):
        self.barva = askcolor()[-1]

    def povecaj(self):
        if self.debelina == 30:
            self.debelina = self.debelina
        else: self.debelina += 1
        self.napis_debelina.set(str(self.debelina))
        
    def zmanjsaj(self):
        if self.debelina == 1:
            self.debelina = self.debelina
        else: self.debelina -= 1
        self.napis_debelina.set(str(self.debelina))

    def zacni_crto(self, event):
        self.tocka = (event.x, event.y)
        self.canvas.create_oval(event.x-self.debelina, event.y-self.debelina,
                                event.x+self.debelina, event.y+self.debelina,
                                fill = self.barva, outline = self.barva)

    def nadaljuj_crto(self, event):
        if self.tocka is not None:
            (x, y) = self.tocka
            self.canvas.create_oval(event.x-self.debelina, event.y-self.debelina,
                                    event.x+self.debelina, event.y+self.debelina,
                                    fill = self.barva, outline = self.barva)
            self.tocka = (event.x, event.y)
        


root = Tk()

aplikacija = Crta(root)

root.mainloop()
