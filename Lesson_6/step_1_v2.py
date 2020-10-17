import tkinter as tk


class TrafficLight(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.cnv = tk.Canvas(self, width=200, height=600, bg='white')
        self.cnv.pack()
        self.oval_r = self.cnv.create_oval(10, 10, 190, 190, fill='lightgrey', outline='white')
        self.oval_y = self.cnv.create_oval(10, 200, 190, 200 + 190, fill='lightgrey', outline='white')
        self.oval_g = self.cnv.create_oval(10, 400, 190, 400 + 190, fill='lightgrey', outline='white')

    def running(self, red, yellow, green):
        while True:
            self.after(red * 1000, self.ch_col_g())
            self.after(yellow * 1000, self.ch_col_y())
            self.after(green * 1000, self.ch_col_r())
            self.after(yellow * 1000, self.ch_col_y())

    def ch_col_r(self):
        self.cnv.itemconfigure(root.oval_g, fill="lightgrey")
        self.cnv.itemconfigure(root.oval_y, fill="lightgrey")
        self.cnv.itemconfigure(root.oval_r, fill="red")
        self.update()

    def ch_col_y(self):
        self.cnv.itemconfigure(root.oval_g, fill="lightgrey")
        self.cnv.itemconfigure(root.oval_r, fill="lightgrey")
        self.cnv.itemconfigure(root.oval_y, fill="yellow")
        self.update()

    def ch_col_g(self):
        self.cnv.itemconfigure(root.oval_r, fill="lightgrey")
        self.cnv.itemconfigure(root.oval_y, fill="lightgrey")
        self.cnv.itemconfigure(root.oval_g, fill="green")
        self.update()


root = TrafficLight()
root.running(4, 1, 4)
