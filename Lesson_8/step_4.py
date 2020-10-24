class Store:
    product_list = dict()

    def __init__(self, name):
        self.name = name
        print(name + ' added\n----------')

    def __str__(self):
        return 'The ' + self.name + ' includes ' + str(len(self.product_list)) + ' position(s):\n\t' + '\n\t' \
            .join([str(i) + '. ' + new_store.product_list[i].name + ' worth ' + str(new_store.product_list[i]._cost) +
                   ' ' + new_store.product_list[i].currency + ' in the amount of ' + str(new_store.product_list[i].cnt)
                   + ' ' + new_store.product_list[i].unit for i in new_store.product_list])

    def remove_product(self, pos: int):
        self.product_list[pos].remove_product()
        self.product_list.pop(pos)
        for i in range(pos, len(self.product_list) + 1):
            self.product_list.update({i: self.product_list[i + 1]})
            self.product_list.pop(i+1)
        print('Product in store removed\n')

    def analytics(self):
        print('The store has ' + str(len(self.product_list)) + ' position(s), sum worth is ' +
              str(sum([new_store.product_list[i]._cost * new_store.product_list[i].cnt for i in new_store.product_list])))


class OfficeEq:
    product_cnt = 0

    def __init__(self, name, cost: float, cnt: int, currency='rub', unit='item(s)'):
        self.name, self._cost, self.cnt, self.unit, self.currency = name, int(cost), int(cnt), unit, currency

    @classmethod
    def add_product(cls, obj, name, cost: float, cnt: int, currency='rub', unit='item(s)'):
        OfficeEq.product_cnt += 1
        obj.product_list[OfficeEq.product_cnt] = cls(name, cost, cnt, currency, unit)
        print(name + ' added.')

    @staticmethod
    def remove_product():
        OfficeEq.product_cnt -= 1

    def show(self):
        print(self)


class Printer(OfficeEq):

    @classmethod
    def add_product(cls, obj, cost: float, cnt: int, name='printer', currency='rub', unit='item(s)'):
        OfficeEq.product_cnt += 1
        obj.product_list[OfficeEq.product_cnt] = cls(name, cost, cnt)
        print(name + ' added.')


class Monitor(OfficeEq):
    def __init__(self, cost: float, cnt: int, name='monitor'):
        super().__init__(name, cost, cnt)

    @classmethod
    def add_product(cls, obj, cost: float, cnt: int, name='monitor', currency='rub', unit='item(s)'):
        OfficeEq.product_cnt += 1
        obj.product_list[OfficeEq.product_cnt] = cls(cost, cnt)
        print(name + ' added.')


class Chair(OfficeEq):
    def __init__(self, cost: float, cnt: int, name='chair'):
        super().__init__(name, cost, cnt)

    @classmethod
    def add_product(cls, obj, cost: float, cnt: int, name='chair', currency='rub', unit='item(s)'):
        OfficeEq.product_cnt += 1
        obj.product_list[OfficeEq.product_cnt] = cls(cost, cnt)
        print(name + ' added.\n')


new_store = Store('Office store')

while exit_point := True:
    choice = input(
        '\n\nWhat do you want?\n\t1. Show products\n\t2. Add product\n\t3. Delete product\n\t4. Show'
        ' analytics\n\t5. Close dial window\n\n')

    if choice == '1':
        print(new_store)
    elif choice == '2':
        typo = input('What do you want to add?\n\t1. Printer\n\t2. Monitor\n\t3. Chair\n\t4. Your type\n')
        try:
            if typo == '1':
                Printer.add_product(new_store, int(input('Input the price:\n')), int(input('Input quantity:\n')))
            elif typo == '2':
                Monitor.add_product(new_store, int(input('Input the price:\n')), int(input('Input quantity:\n')))
            elif typo == '3':
                Chair.add_product(new_store, int(input('Input the price:\n')), int(input('Input quantity:\n')))
            elif typo == '4':
                OfficeEq.add_product(new_store, input('Input type:\n'), int(input('Input the price:\n'))
                                     , int(input('Input quantity:\n')))
            print(new_store)
        except ValueError:
            print('You must enter a numeric parameter\n')
    elif choice == '3':
        print(new_store)
        try:
            new_store.remove_product(int(input('Which position to delete?\n')))
        except KeyError:
            print('Position not found.\n')
    elif choice == '4':
        new_store.analytics()
    elif choice == '5':
        break
    else:
        print('Please repeat. I don\'t understand')
    input()
