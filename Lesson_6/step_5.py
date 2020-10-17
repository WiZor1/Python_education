class Stationery:
    title = 'stationery'

    def draw(self):
        print('Start drawing', end='')


class Pen(Stationery):
    title = 'pen'

    def draw(self):
        super().draw()
        print(' with ' + self.title)


class Pencil(Stationery):
    title = 'pencil'

    def draw(self):
        super().draw()
        print(' with ' + self.title)


class Handle(Stationery):
    title = 'handle'

    def draw(self):
        super().draw()
        print(' with ' + self.title)


pen = Pen()
pen.draw()
print('------')
pencil = Pencil()
pencil.draw()
print('------')
handle = Handle()
handle.draw()
